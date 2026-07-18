#!/usr/bin/env python3
"""Run an independent editorial and rendered-visual review of a Colab data story."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import nbformat

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from validate_notebook import execute_notebook, notebook_errors, source_fingerprint  # noqa: E402


PLOTLY_MIME = "application/vnd.plotly.v1+json"
DIALOGUE = re.compile(r"\*\*([^*:\n]{1,48}):\*\*")
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD)\b|(?i:\blorem ipsum\b)")
CARTESIAN_TRACES = {"bar", "box", "histogram", "histogram2d", "scatter", "violin"}
THREE_D_TRACES = {"cone", "isosurface", "mesh3d", "scatter3d", "streamtube", "surface", "volume"}
DEFAULT_PLOTLY_COLORS = {
    "#636efa",
    "#ef553b",
    "#00cc96",
    "#ab63fa",
    "#ffa15a",
    "#19d3f3",
    "#ff6692",
    "#b6e880",
    "#ff97ff",
    "#fecb52",
}


def has_output(cell: Any) -> bool:
    return any(
        output.get("output_type") == "stream" and str(output.get("text", "")).strip()
        or output.get("output_type") in {"display_data", "execute_result"} and bool(output.get("data"))
        for output in cell.get("outputs", [])
    )


def plotly_figures(cell: Any) -> list[dict[str, Any]]:
    figures: list[dict[str, Any]] = []
    for output in cell.get("outputs", []):
        data = output.get("data", {})
        if PLOTLY_MIME in data and isinstance(data[PLOTLY_MIME], dict):
            figures.append(data[PLOTLY_MIME])
    return figures


def axis_title(layout: dict[str, Any], axis: str) -> str:
    title = layout.get(axis, {}).get("title", {})
    return str(title.get("text", "")) if isinstance(title, dict) else str(title or "")


def has_figure_control(layout: dict[str, Any]) -> bool:
    if layout.get("updatemenus") or layout.get("sliders"):
        return True
    return any(
        str(key).startswith("xaxis") and isinstance(value, dict) and value.get("rangeslider", {}).get("visible")
        for key, value in layout.items()
    )


def explicit_trace_colors(figure: dict[str, Any]) -> set[str]:
    colors: set[str] = set()
    for trace in figure.get("data", []):
        for container in (trace.get("marker", {}), trace.get("line", {}), trace):
            color = container.get("color") if isinstance(container, dict) else None
            if isinstance(color, str) and color.startswith("#"):
                colors.add(color.casefold())
    return colors


def quality_errors(notebook: Any) -> tuple[list[str], list[dict[str, Any]]]:
    errors = notebook_errors(notebook)
    figures_reviewed: list[dict[str, Any]] = []
    if errors:
        return errors, figures_reviewed

    code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
    for cell in code_cells:
        if cell.execution_count is None:
            errors.append(f"cell {cell.id} was not executed in the reviewed run")

    roles: dict[str, list[Any]] = {}
    for cell in notebook.cells:
        roles.setdefault(str(cell.metadata.get("narrative_role", "")), []).append(cell)

    for cell in roles.get("learner-code", []):
        if not has_output(cell):
            errors.append(f"learner cell {cell.id} has no visible executed result")

    for cell in roles.get("visualization", []):
        figures = plotly_figures(cell)
        if len(figures) != 1:
            errors.append(f"visual cell {cell.id} must render exactly one Plotly figure; found {len(figures)}")
            continue
        figure = figures[0]
        layout = figure.get("layout", {})
        traces = figure.get("data", [])
        title = str(layout.get("title", {}).get("text", ""))
        trace_types = {str(trace.get("type", "scatter")) for trace in traces}
        if not title:
            errors.append(f"visual cell {cell.id} needs a visible chart title")
        elif "<sup>" not in title:
            errors.append(f"visual cell {cell.id} title needs a contextual subtitle using <sup>")
        if not traces:
            errors.append(f"visual cell {cell.id} rendered no traces")
        if trace_types & THREE_D_TRACES:
            errors.append(f"visual cell {cell.id} uses a misleading 3D chart")
        if trace_types & CARTESIAN_TRACES:
            if not axis_title(layout, "xaxis"):
                errors.append(f"visual cell {cell.id} needs an x-axis title with units or meaning")
            if not axis_title(layout, "yaxis"):
                errors.append(f"visual cell {cell.id} needs a y-axis title with units or meaning")
        if not has_figure_control(layout):
            errors.append(f"visual cell {cell.id} needs its own dropdown, slider, button, or range slider")
        if not any(trace.get("hovertemplate") or trace.get("hovertext") or trace.get("text") for trace in traces):
            errors.append(f"visual cell {cell.id} needs informative hover or direct labels")
        colors = explicit_trace_colors(figure)
        if not colors:
            errors.append(f"visual cell {cell.id} needs an explicit palette")
        elif colors <= DEFAULT_PLOTLY_COLORS:
            errors.append(f"visual cell {cell.id} still uses only Plotly's default palette")
        figures_reviewed.append(
            {
                "cell_id": str(cell.id),
                "concept": str(cell.metadata.get("concept", "")),
                "title": title,
                "trace_types": sorted(trace_types),
                "palette": sorted(colors),
            }
        )

    narrative_cells = roles.get("story-intro", []) + roles.get("concept-prompt", [])
    narrative_source = "\n".join(str(cell.source) for cell in narrative_cells)
    speakers = {match.casefold() for match in DIALOGUE.findall(narrative_source)}
    dialogue_turns = len(DIALOGUE.findall(narrative_source))
    if dialogue_turns < 4 or len(speakers) < 2:
        errors.append("condensed story needs at least four dialogue turns across two characters")
    if PLACEHOLDER.search("\n".join(str(cell.source) for cell in notebook.cells)):
        errors.append("notebook contains an editorial placeholder")

    interpretations = []
    for cell in roles.get("visualization", []):
        match = re.search(r"\*\*Lo que muestra:\*\*\s*(.+?)\"\)\)?\s*$", str(cell.source), re.DOTALL)
        if match:
            interpretations.append(re.sub(r"\s+", " ", match.group(1)).strip())
    if interpretations and len(set(interpretations)) != len(interpretations):
        errors.append("each concept needs a distinct interpretation tied to its own evidence")

    metrics = notebook.metadata.narrative_colab.get("metrics", [])
    learner_by_id = {str(cell.id): cell for cell in roles.get("learner-code", [])}
    for metric in metrics:
        cell = learner_by_id.get(str(metric.get("cell_id", "")))
        if cell is not None and not has_output(cell):
            errors.append(f"metric {metric.get('name')!r} has no executed output to support the story")

    return errors, figures_reviewed


def stamp_review(notebook: Any, figures_reviewed: list[dict[str, Any]]) -> None:
    checks = [
        "all code cells executed in a fresh pass",
        "learner metrics produced visible outputs",
        "one labeled interactive Plotly figure per concept",
        "titles include context and figures use explicit non-default colors",
        "condensed story contains dialogue, a data turn, and distinct interpretations",
        "review stamp is bound to notebook sources and narrative metadata",
    ]
    notebook.metadata.narrative_colab["quality_review"] = {
        "status": "passed",
        "reviewed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "reviewer": "create-colab-data-story/scripts/review_notebook.py",
        "checks": checks,
        "figures": figures_reviewed,
    }
    notebook.metadata.narrative_colab.quality_review["source_sha256"] = source_fingerprint(notebook)


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", type=Path)
    parser.add_argument("--execute", action="store_true", help="rerun the notebook before editorial review")
    parser.add_argument("--stamp", action="store_true", help="write a source-bound PASS stamp into notebook metadata")
    parser.add_argument("--timeout", type=int, default=180)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = make_parser().parse_args(argv)
    notebook = nbformat.read(args.notebook, as_version=4)
    if args.execute:
        try:
            notebook = execute_notebook(notebook, timeout=args.timeout)
        except Exception as exc:
            print(f"ERROR: independent notebook execution failed: {exc}", file=sys.stderr)
            return 1
    errors, figures_reviewed = quality_errors(notebook)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.stamp:
        stamp_review(notebook, figures_reviewed)
        nbformat.write(notebook, args.notebook)
    print(
        f"PASS: {args.notebook} ({len(figures_reviewed)} reviewed figures; "
        f"source {source_fingerprint(notebook)[:12]})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
