#!/usr/bin/env python3
"""Validate structure, provenance, live sources, and execution of a data-story notebook."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
from unittest.mock import patch
from pathlib import Path
from typing import Any

import nbformat


WORD = re.compile(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ'-]+\b", re.UNICODE)
PARAM = re.compile(r"#\s*@param\b")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
INTERACTIVE_MARKERS = ("updatemenus", "sliders", "animation_frame", "buttons", "rangeslider")
MAX_DOWNLOAD = 25 * 1024 * 1024
COLAB_GITHUB = re.compile(r"^https://colab\.research\.google\.com/github/[^/]+/[^/]+/blob/[^/]+/.+\.ipynb$")


def nonblank_lines(source: str) -> int:
    return sum(bool(line.strip()) for line in source.splitlines())


def source_fingerprint(notebook: Any) -> str:
    """Bind an editorial-review stamp to cell sources and narrative metadata."""
    narrative_metadata = dict(notebook.metadata.get("narrative_colab", {}))
    narrative_metadata.pop("quality_review", None)
    payload = {
        "cells": [
            {
                "id": str(getattr(cell, "id", "")),
                "cell_type": str(cell.cell_type),
                "source": str(cell.source),
                "narrative_role": str(cell.metadata.get("narrative_role", "")),
            }
            for cell in notebook.cells
        ],
        "narrative_colab": narrative_metadata,
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def notebook_errors(notebook: Any) -> list[str]:
    errors: list[str] = []
    try:
        nbformat.validate(notebook)
    except Exception as exc:  # nbformat exposes several validation exception types
        errors.append(f"invalid nbformat: {exc}")
        return errors

    metadata = notebook.metadata.get("narrative_colab")
    if not isinstance(metadata, dict):
        return ["missing notebook metadata.narrative_colab"]

    sequence = metadata.get("concept_sequence")
    if not isinstance(sequence, list) or not 1 <= len(sequence) <= 5:
        errors.append("concept_sequence must contain between one and five concepts")
        sequence = []
    concept_names = [str(item.get("name", "")) for item in sequence if isinstance(item, dict)]
    if len(concept_names) != len(sequence) or any(not name for name in concept_names):
        errors.append("every concept_sequence item must have a name")
    if concept_names and metadata.get("primary_concept") != concept_names[0]:
        errors.append("primary_concept must equal the first concept in concept_sequence")
    for index, concept in enumerate(sequence[1:], start=1):
        connection = str(concept.get("connection_from_previous", ""))
        previous = concept_names[index - 1]
        if not connection or previous.casefold() not in connection.casefold():
            errors.append(f"concept {concept_names[index]!r} must explicitly connect to {previous!r}")

    count = len(sequence)
    minimum_cells = 7 + 3 * count if count else 0
    maximum_cells = min(27, 7 + 4 * count) if count else 27
    if count and not minimum_cells <= len(notebook.cells) <= maximum_cells:
        errors.append(
            f"cell count {len(notebook.cells)} is outside the allowed {minimum_cells}-{maximum_cells} range"
        )

    roles: dict[str, list[Any]] = {}
    ids: set[str] = set()
    for cell in notebook.cells:
        role = str(cell.metadata.get("narrative_role", ""))
        roles.setdefault(role, []).append(cell)
        cell_id = str(getattr(cell, "id", ""))
        if not cell_id:
            errors.append("every cell must have an id")
        elif cell_id in ids:
            errors.append(f"duplicate cell id: {cell_id}")
        ids.add(cell_id)

    for role in ("title", "central-question", "story-intro", "source", "synthesis", "conclusion"):
        if len(roles.get(role, [])) != 1:
            errors.append(f"notebook must contain exactly one {role} cell")
    colab_url = str(metadata.get("colab_url") or "")
    if colab_url:
        if not COLAB_GITHUB.fullmatch(colab_url):
            errors.append("metadata.colab_url must be a Colab GitHub notebook URL")
        title_source = roles.get("title", [None])[0]
        if not title_source or colab_url not in title_source.source or "colab-badge.svg" not in title_source.source:
            errors.append("title cell must include an Open in Colab badge linked to metadata.colab_url")

    markdown_words = sum(
        len(WORD.findall(cell.source))
        for cell in notebook.cells
        if cell.cell_type == "markdown" and cell.metadata.get("narrative_role") != "source"
    )
    word_max = 250 + 100 * (count - 1) if count else 250
    if markdown_words > word_max:
        errors.append(f"narrative Markdown has {markdown_words} words; maximum is {word_max}")

    setup_cells = roles.get("setup", [])
    if len(setup_cells) != 1:
        errors.append("notebook must contain exactly one setup cell")
    elif not PARAM.search(setup_cells[0].source):
        errors.append("setup cell must include a Colab # @param control")

    hidden_cells = setup_cells + roles.get("visualization", [])
    for cell in hidden_cells:
        if cell.metadata.get("cellView") != "form":
            errors.append(f"cell {cell.id} with role {cell.metadata.get('narrative_role')} must use cellView=form")
        if not cell.source.lstrip().startswith(("# @title", "#@title")):
            errors.append(f"hidden cell {cell.id} must start with # @title")

    learner_cells = roles.get("learner-code", [])
    if count and len(learner_cells) != count:
        errors.append("notebook must expose exactly one learner-code cell per concept")
    dataframe_name = str(metadata.get("dataframe_name", "df"))
    for cell in learner_cells:
        if nonblank_lines(cell.source) > 8:
            errors.append(f"learner cell {cell.id} exceeds eight nonblank lines")
        if dataframe_name not in cell.source:
            errors.append(f"learner cell {cell.id} does not reuse dataframe {dataframe_name!r}")
        if cell.metadata.get("cellView") == "form":
            errors.append(f"learner cell {cell.id} must remain visible")

    visual_cells = roles.get("visualization", [])
    if count and len(visual_cells) != count:
        errors.append("notebook must contain exactly one visualization cell per concept")
    visual_source = "\n".join(cell.source for cell in visual_cells)
    setup_source = "\n".join(cell.source for cell in setup_cells)
    if "plotly" not in (setup_source + visual_source).casefold():
        errors.append("notebook must use Plotly for interactive evidence")
    if not any(marker in visual_source for marker in INTERACTIVE_MARKERS):
        errors.append("visualizations need a figure-native dropdown, slider, animation, button, or range slider")

    metrics = metadata.get("metrics")
    if not isinstance(metrics, list) or len(metrics) != count:
        errors.append("metadata.metrics must contain exactly one traceable metric per concept")
        metrics = []
    learner_ids = {str(cell.id) for cell in learner_cells}
    learner_sources = {str(cell.id): cell.source for cell in learner_cells}
    metric_concepts: set[str] = set()
    for metric in metrics:
        if not isinstance(metric, dict):
            errors.append("every metric must be a mapping")
            continue
        for field in ("concept", "name", "expression", "cell_id"):
            if not metric.get(field):
                errors.append(f"metric is missing {field}")
        metric_concepts.add(str(metric.get("concept", "")).casefold())
        metric_cell_id = str(metric.get("cell_id", ""))
        if metric_cell_id not in learner_ids:
            errors.append(f"metric {metric.get('name', '')!r} does not reference a learner cell")
        elif str(metric.get("expression", "")) not in learner_sources[metric_cell_id]:
            errors.append(f"metric {metric.get('name', '')!r} expression is absent from its learner cell")
    if concept_names and metric_concepts != {name.casefold() for name in concept_names}:
        errors.append("metrics must cover every concept exactly once")

    dataset = metadata.get("dataset")
    required_dataset = (
        "title",
        "publisher",
        "landing_url",
        "data_url",
        "license",
        "accessed_at",
        "format",
        "bytes",
        "rows",
        "columns",
        "sha256",
        "supports_concepts",
    )
    if not isinstance(dataset, dict):
        errors.append("missing dataset provenance metadata")
    else:
        for field in required_dataset:
            if dataset.get(field) in (None, "", []):
                errors.append(f"dataset metadata is missing {field}")
        for field in ("landing_url", "data_url"):
            if dataset.get(field) and not str(dataset[field]).startswith("https://"):
                errors.append(f"dataset {field} must use HTTPS")
        if dataset.get("sha256") and not SHA256.fullmatch(str(dataset["sha256"])):
            errors.append("dataset sha256 is invalid")
        if not isinstance(dataset.get("bytes"), int) or not 0 < dataset.get("bytes", 0) <= MAX_DOWNLOAD:
            errors.append("dataset bytes must be a positive integer no greater than 25 MB")
        if not isinstance(dataset.get("rows"), int) or dataset.get("rows", 0) <= 0:
            errors.append("dataset rows must be a positive integer")
        if str(dataset.get("format", "")).casefold() == "zip" and not dataset.get("member"):
            errors.append("zip dataset metadata must declare member")
        supported = {str(value).casefold() for value in dataset.get("supports_concepts", [])}
        if concept_names and supported != {name.casefold() for name in concept_names}:
            errors.append("dataset supports_concepts must match concept_sequence")
        columns = {str(value) for value in dataset.get("columns", [])}
        for concept in sequence:
            missing = {str(value) for value in concept.get("required_columns", [])} - columns
            if missing:
                errors.append(f"concept {concept.get('name')!r} requires undeclared columns: {sorted(missing)}")

    story = metadata.get("story")
    if not isinstance(story, dict):
        errors.append("missing story provenance metadata")
    else:
        for field in ("case_id", "title", "source_path", "created_by_pipeline", "adaptations"):
            if field not in story or story[field] in (None, ""):
                errors.append(f"story metadata is missing {field}")
        if not isinstance(story.get("created_by_pipeline"), bool):
            errors.append("story created_by_pipeline must be boolean")
        if not isinstance(story.get("adaptations"), list):
            errors.append("story adaptations must be a list")

    image = metadata.get("image")
    if image:
        for field in ("url", "source_url", "license", "credit", "alt"):
            if not image.get(field):
                errors.append(f"image metadata is missing {field}")
        for field in ("url", "source_url"):
            if image.get(field) and not str(image[field]).startswith("https://"):
                errors.append(f"image {field} must use HTTPS")

    quality_review = metadata.get("quality_review")
    if quality_review is not None:
        if not isinstance(quality_review, dict):
            errors.append("metadata.quality_review must be a mapping")
        else:
            if quality_review.get("status") != "passed":
                errors.append("metadata.quality_review.status must be passed")
            if not SHA256.fullmatch(str(quality_review.get("source_sha256", ""))):
                errors.append("metadata.quality_review.source_sha256 is invalid")
            elif quality_review["source_sha256"] != source_fingerprint(notebook):
                errors.append("quality review is stale because notebook sources or metadata changed")
            checks = quality_review.get("checks")
            if not isinstance(checks, list) or not checks:
                errors.append("metadata.quality_review.checks must be a non-empty list")

    return errors


def fetch_bytes(url: str, *, limit: int = MAX_DOWNLOAD, timeout: int = 30) -> tuple[bytes, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "colab-data-story-validator/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > limit:
            raise ValueError(f"source is {int(content_length)} bytes; limit is {limit}")
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = response.read(min(1024 * 1024, limit - total + 1))
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            if total > limit:
                raise ValueError(f"source exceeds {limit} bytes")
        return b"".join(chunks), response.headers.get("Content-Type", "")


def network_errors(notebook: Any) -> list[str]:
    errors: list[str] = []
    metadata = notebook.metadata.get("narrative_colab", {})
    dataset = metadata.get("dataset", {})
    try:
        fetch_bytes(str(dataset["landing_url"]), limit=2 * 1024 * 1024)
    except (KeyError, OSError, ValueError, urllib.error.URLError) as exc:
        errors.append(f"dataset landing page is unavailable: {exc}")
    try:
        payload, _ = fetch_bytes(str(dataset["data_url"]))
        digest = hashlib.sha256(payload).hexdigest()
        if digest != dataset.get("sha256"):
            errors.append(f"dataset SHA-256 changed: expected {dataset.get('sha256')}, got {digest}")
        if dataset.get("bytes") not in (None, len(payload)):
            errors.append(f"dataset byte size changed: expected {dataset.get('bytes')}, got {len(payload)}")
        try:
            import pandas as pd

            data_format = str(dataset.get("format", "")).casefold()
            tabular_payload = payload
            if data_format == "zip":
                member = str(dataset.get("member", ""))
                if not member:
                    raise ValueError("zip datasets must declare dataset.member")
                with zipfile.ZipFile(io.BytesIO(payload)) as archive:
                    if member not in archive.namelist():
                        raise ValueError(f"zip member {member!r} is unavailable")
                    tabular_payload = archive.read(member)
                suffix = Path(member).suffix.casefold()
                data_format = "csv" if suffix == ".csv" else "json" if suffix == ".json" else suffix.lstrip(".")
            if data_format == "csv":
                frame = pd.read_csv(io.BytesIO(tabular_payload))
            elif data_format in {"json", "jsonl", "ndjson"}:
                frame = pd.read_json(io.BytesIO(tabular_payload), lines=data_format != "json")
            else:
                raise ValueError(f"unsupported validation format {data_format!r}; use csv or json")
            if len(frame) != dataset.get("rows"):
                errors.append(f"dataset row count changed: expected {dataset.get('rows')}, got {len(frame)}")
            expected_columns = {str(value) for value in dataset.get("columns", [])}
            missing_columns = expected_columns - {str(value) for value in frame.columns}
            if missing_columns:
                errors.append(f"dataset is missing declared columns: {sorted(missing_columns)}")
        except (ImportError, OSError, TypeError, ValueError, zipfile.BadZipFile) as exc:
            errors.append(f"dataset could not be parsed and checked: {exc}")
    except (KeyError, OSError, ValueError, urllib.error.URLError) as exc:
        errors.append(f"dataset download is unavailable: {exc}")

    image = metadata.get("image")
    if image:
        try:
            _, content_type = fetch_bytes(str(image["url"]), limit=10 * 1024 * 1024)
            if not content_type.casefold().startswith("image/"):
                errors.append(f"image URL returned non-image content type: {content_type}")
        except (KeyError, OSError, ValueError, urllib.error.URLError) as exc:
            errors.append(f"image is unavailable: {exc}")
        try:
            fetch_bytes(str(image["source_url"]), limit=2 * 1024 * 1024)
        except (KeyError, OSError, ValueError, urllib.error.URLError) as exc:
            errors.append(f"image source page is unavailable: {exc}")
    return errors


def execute_notebook(notebook: Any, timeout: int = 180) -> Any:
    try:
        from nbclient import NotebookClient
    except ImportError as exc:  # pragma: no cover - environment-dependent message
        raise RuntimeError("nbclient is required for --execute") from exc
    kernel_name = notebook.metadata.get("kernelspec", {}).get("name", "python3")
    with tempfile.TemporaryDirectory(prefix="colab-story-jupyter-") as runtime_dir:
        environment = {
            "IPYTHONDIR": os.path.join(runtime_dir, "ipython"),
            "JUPYTER_CONFIG_DIR": os.path.join(runtime_dir, "config"),
            "JUPYTER_DATA_DIR": os.path.join(runtime_dir, "data"),
            "JUPYTER_RUNTIME_DIR": os.path.join(runtime_dir, "runtime"),
        }
        with patch.dict(os.environ, environment):
            client = NotebookClient(notebook, timeout=timeout, kernel_name=kernel_name, allow_errors=False)
            return client.execute()


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", type=Path)
    parser.add_argument("--check-network", action="store_true")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--timeout", type=int, default=180)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = make_parser().parse_args(argv)
    notebook = nbformat.read(args.notebook, as_version=4)
    errors = notebook_errors(notebook)
    if args.check_network and not errors:
        errors.extend(network_errors(notebook))
    if args.execute and not errors:
        try:
            notebook = execute_notebook(notebook, timeout=args.timeout)
            nbformat.write(notebook, args.notebook)
        except Exception as exc:
            errors.append(f"notebook execution failed: {exc}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {args.notebook} ({len(notebook.cells)} cells)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
