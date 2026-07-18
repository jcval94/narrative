#!/usr/bin/env python3
"""Render a Colab-ready narrative notebook from a compact YAML specification."""

from __future__ import annotations

import argparse
import copy
import html
import json
import re
import subprocess
from pathlib import Path
from typing import Any
from urllib.parse import quote

import nbformat
import yaml


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = SKILL_ROOT / "assets" / "colab-data-story-template.ipynb"
SHA256 = re.compile(r"^[0-9a-f]{64}$")
WORD = re.compile(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ'-]+\b", re.UNICODE)
GITHUB_HTTPS = re.compile(r"^https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/.]+)(?:\.git)?/?$")
GITHUB_SSH = re.compile(r"^(?:git@github\.com:|ssh://git@github\.com/)(?P<owner>[^/]+)/(?P<repo>[^/.]+)(?:\.git)?/?$")


def require(mapping: dict[str, Any], key: str, context: str = "spec") -> Any:
    value = mapping.get(key)
    if value is None or value == "" or value == []:
        raise ValueError(f"{context}.{key} is required")
    return value


def nonblank_lines(source: str) -> int:
    return sum(bool(line.strip()) for line in source.splitlines())


def titled_code(source: str, title: str) -> str:
    source = source.strip()
    if source.startswith("# @title") or source.startswith("#@title"):
        return source
    return f'# @title {title} {{ display-mode: "form" }}\n{source}'


def git_output(args: list[str], cwd: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip()


def normalize_github_repo(remote_url: str) -> str | None:
    for pattern in (GITHUB_HTTPS, GITHUB_SSH):
        match = pattern.match(remote_url.strip())
        if match:
            return f"{match.group('owner')}/{match.group('repo')}"
    return None


def build_colab_url(output_path: Path | None, github_repo: str | None, branch: str | None) -> str | None:
    if not output_path:
        return None
    resolved_output = output_path.resolve()
    cwd = output_path.parent if output_path.parent.exists() else Path.cwd()
    git_root_text = git_output(["rev-parse", "--show-toplevel"], cwd)
    if not git_root_text:
        return None
    git_root = Path(git_root_text).resolve()
    try:
        relative_path = resolved_output.relative_to(git_root).as_posix()
    except ValueError:
        return None
    repo = github_repo
    if not repo:
        remote_url = git_output(["config", "--get", "remote.origin.url"], git_root)
        repo = normalize_github_repo(remote_url or "")
    if not repo:
        return None
    selected_branch = branch or git_output(["branch", "--show-current"], git_root) or "main"
    return f"https://colab.research.google.com/github/{repo}/blob/{selected_branch}/{quote(relative_path, safe='/')}"


def markdown_cell(source: str, role: str, cell_id: str, **metadata: Any) -> Any:
    cell = nbformat.v4.new_markdown_cell(source=source.strip())
    cell.id = cell_id
    cell.metadata.update({"narrative_role": role, **metadata})
    return cell


def code_cell(
    source: str,
    role: str,
    cell_id: str,
    *,
    hidden: bool = False,
    **metadata: Any,
) -> Any:
    cell = nbformat.v4.new_code_cell(source=source.strip())
    cell.id = cell_id
    cell.metadata.update({"narrative_role": role, **metadata})
    if hidden:
        cell.metadata["cellView"] = "form"
    return cell


def validate_spec(spec: dict[str, Any]) -> list[dict[str, Any]]:
    for key in ("title", "central_question", "story_intro", "synthesis", "decision", "rule"):
        require(spec, key)
    require(spec, "story")
    dataset = require(spec, "dataset")
    concepts = require(spec, "concepts")
    if not isinstance(concepts, list) or not 1 <= len(concepts) <= 5:
        raise ValueError("spec.concepts must contain between one and five concepts")

    dataframe_name = str(spec.get("dataframe_name", "df"))
    if not re.fullmatch(r"[A-Za-z_]\w*", dataframe_name):
        raise ValueError("spec.dataframe_name must be a valid Python identifier")
    setup_code = str(require(spec, "setup_code"))
    if not re.search(r"#\s*@param\b", setup_code):
        raise ValueError("spec.setup_code must include at least one Colab # @param control")
    if dataframe_name not in setup_code:
        raise ValueError(f"spec.setup_code must create the shared dataframe {dataframe_name!r}")

    dataset_fields = (
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
    for key in dataset_fields:
        require(dataset, key, "spec.dataset")
    if not SHA256.fullmatch(str(dataset["sha256"])):
        raise ValueError("spec.dataset.sha256 must be 64 lowercase hexadecimal characters")
    if not isinstance(dataset["bytes"], int) or not 0 < dataset["bytes"] <= 25 * 1024 * 1024:
        raise ValueError("spec.dataset.bytes must be a positive integer no greater than 25 MB")
    if not isinstance(dataset["rows"], int) or dataset["rows"] <= 0:
        raise ValueError("spec.dataset.rows must be a positive integer")
    if not isinstance(dataset["columns"], list) or not dataset["columns"]:
        raise ValueError("spec.dataset.columns must be a non-empty list")
    data_format = str(dataset["format"]).casefold()
    if data_format not in {"csv", "json", "jsonl", "ndjson", "zip"}:
        raise ValueError("spec.dataset.format must be csv, json, jsonl, ndjson, or zip")
    if data_format == "zip" and not dataset.get("member"):
        raise ValueError("spec.dataset.member is required for zip data")
    for url_key in ("landing_url", "data_url"):
        if not str(dataset[url_key]).startswith("https://"):
            raise ValueError(f"spec.dataset.{url_key} must use HTTPS")

    names = [str(require(concept, "name", f"spec.concepts[{index}]")) for index, concept in enumerate(concepts)]
    if len({name.casefold() for name in names}) != len(names):
        raise ValueError("concept names must be unique")
    supported = [str(value) for value in dataset["supports_concepts"]]
    if {value.casefold() for value in supported} != {value.casefold() for value in names}:
        raise ValueError("spec.dataset.supports_concepts must match every requested concept")

    dataset_columns = {str(value) for value in dataset["columns"]}
    for index, concept in enumerate(concepts):
        context = f"spec.concepts[{index}]"
        for key in (
            "connection_from_previous",
            "question",
            "scene",
            "learning_code",
            "visualization_code",
            "interpretation",
            "metric_name",
            "metric_expression",
            "required_columns",
        ):
            require(concept, key, context)
        if index and names[index - 1].casefold() not in str(concept["connection_from_previous"]).casefold():
            raise ValueError(
                f"{context}.connection_from_previous must name the previous concept {names[index - 1]!r}"
            )
        if nonblank_lines(str(concept["learning_code"])) > 8:
            raise ValueError(f"{context}.learning_code exceeds eight nonblank lines")
        if dataframe_name not in str(concept["learning_code"]):
            raise ValueError(f"{context}.learning_code must reuse dataframe {dataframe_name!r}")
        visualization_code = str(concept["visualization_code"])
        derived_names = re.findall(r"[A-Za-z_]\w*", str(concept["metric_expression"]))
        if dataframe_name not in visualization_code and not any(
            name in visualization_code for name in derived_names
        ):
            raise ValueError(
                f"{context}.visualization_code must reuse {dataframe_name!r} or its declared metric expression"
            )
        missing = {str(value) for value in concept["required_columns"]} - dataset_columns
        if missing:
            raise ValueError(f"{context}.required_columns are absent from dataset metadata: {sorted(missing)}")

    image = spec.get("image")
    if image:
        for key in ("url", "source_url", "license", "credit", "alt"):
            require(image, key, "spec.image")
        if not str(image["url"]).startswith("https://") or not str(image["source_url"]).startswith("https://"):
            raise ValueError("spec.image URLs must use HTTPS")

    return concepts


def source_markdown(dataset: dict[str, Any]) -> str:
    columns = ", ".join(f"`{column}`" for column in dataset["columns"])
    return (
        "## Fuente real\n\n"
        f"**{dataset['title']}**, {dataset['publisher']}. "
        f"[Página de origen]({dataset['landing_url']}) · "
        f"[datos]({dataset['data_url']}) · licencia: {dataset['license']}.  \n"
        f"Consultado: {dataset['accessed_at']} · {dataset['rows']:,} filas · "
        f"columnas usadas: {columns}."
    )


def render_notebook(
    spec: dict[str, Any],
    template_path: Path = DEFAULT_TEMPLATE,
    output_name: str = "colab-data-story.ipynb",
    output_path: Path | None = None,
    github_repo: str | None = None,
    branch: str | None = None,
) -> Any:
    concepts = validate_spec(spec)
    template = nbformat.read(template_path, as_version=4)
    notebook = nbformat.v4.new_notebook()
    notebook.metadata = copy.deepcopy(template.metadata)
    notebook.metadata.setdefault("colab", {})["name"] = output_name

    story = spec["story"]
    dataset = spec["dataset"]
    dataframe_name = str(spec.get("dataframe_name", "df"))
    story_intro = str(spec["story_intro"]).strip()
    image = spec.get("image")
    if image:
        story_intro += (
            f'\n\n<img src="{html.escape(str(image["url"]), quote=True)}" '
            f'alt="{html.escape(str(image["alt"]), quote=True)}" '
            'style="max-width:100%;height:auto">\n\n'
            f'<small>Imagen: <a href="{html.escape(str(image["source_url"]), quote=True)}">'
            f'{html.escape(str(image["credit"]))}</a>, {html.escape(str(image["license"]))}.</small>'
        )
    colab_url = str(spec.get("colab_url") or "") or build_colab_url(output_path, github_repo, branch)
    colab_badge = ""
    if colab_url:
        colab_badge = (
            "\n\n"
            f"[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"
        )

    cells: list[Any] = [
        markdown_cell(
            f"# {spec['title']}\n\n**Nivel:** {spec.get('level', 'adaptive')}{colab_badge}",
            "title",
            "shared-title",
        ),
        markdown_cell(f"## Pregunta central\n\n{spec['central_question']}", "central-question", "shared-question"),
        markdown_cell(
            "## Recreación narrativa\n\n"
            f"{story_intro}\n\n"
            "*La escena es una recreación; las conclusiones provienen del dataset citado.*",
            "story-intro",
            "shared-story",
        ),
        markdown_cell(source_markdown(dataset), "source", "shared-source"),
        code_cell(
            titled_code(str(spec["setup_code"]), "Preparar los datos"),
            "setup",
            "shared-setup",
            hidden=True,
        ),
    ]

    concept_sequence: list[dict[str, Any]] = []
    metrics: list[dict[str, str]] = []
    for index, concept in enumerate(concepts, start=1):
        slug = f"concept-{index}"
        name = str(concept["name"])
        learner_id = f"{slug}-learner"
        concept_sequence.append(
            {
                "order": index,
                "name": name,
                "question": str(concept["question"]),
                "connection_from_previous": str(concept["connection_from_previous"]),
                "required_columns": [str(value) for value in concept["required_columns"]],
            }
        )
        metrics.append(
            {
                "concept": name,
                "name": str(concept["metric_name"]),
                "expression": str(concept["metric_expression"]),
                "cell_id": learner_id,
            }
        )
        cells.extend(
            [
                markdown_cell(
                    f"## {index}. {name}\n\n{concept['scene']}\n\n"
                    f"**Pregunta:** {concept['question']}\n\n"
                    f"**Conexión:** {concept['connection_from_previous']}",
                    "concept-prompt",
                    f"{slug}-prompt",
                    concept=name,
                    concept_index=index,
                ),
                code_cell(
                    str(concept["learning_code"]),
                    "learner-code",
                    learner_id,
                    concept=name,
                    concept_index=index,
                ),
                code_cell(
                    titled_code(
                        str(concept["visualization_code"])
                        + "\n\ndisplay(Markdown("
                        + json.dumps(f"**Lo que muestra:** {concept['interpretation']}", ensure_ascii=False)
                        + "))",
                        f"Explorar {name}",
                    ),
                    "visualization",
                    f"{slug}-visual",
                    hidden=True,
                    concept=name,
                    concept_index=index,
                ),
            ]
        )
        if concept.get("exercise_prompt"):
            cells.append(
                markdown_cell(
                    f"**Tu turno:** {concept['exercise_prompt']}",
                    "exercise",
                    f"{slug}-exercise",
                    concept=name,
                    concept_index=index,
                )
            )

    cells.extend(
        [
            markdown_cell(f"## Cómo se conecta todo\n\n{spec['synthesis']}", "synthesis", "shared-synthesis"),
            markdown_cell(
                f"## Decisión\n\n{spec['decision']}\n\n**Regla:** {spec['rule']}",
                "conclusion",
                "shared-conclusion",
            ),
        ]
    )
    notebook.cells = cells
    notebook.metadata["narrative_colab"] = {
        "schema_version": "1.0",
        "primary_concept": concept_sequence[0]["name"],
        "concept_sequence": concept_sequence,
        "dataframe_name": dataframe_name,
        "story": copy.deepcopy(story),
        "dataset": copy.deepcopy(dataset),
        "metrics": metrics,
        "image": copy.deepcopy(image),
        "cell_budget": {
            "standard": 7 + 3 * len(concepts),
            "absolute_max": 27,
            "markdown_word_max": 250 + 100 * (len(concepts) - 1),
        },
        "colab_url": colab_url,
    }
    nbformat.validate(notebook)
    return notebook


def load_spec(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle)
    if not isinstance(payload, dict):
        raise ValueError("specification must be a YAML mapping")
    return payload


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--github-repo", help="GitHub owner/repository used to build the Colab badge URL")
    parser.add_argument("--branch", help="Git branch used to build the Colab badge URL")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = make_parser().parse_args(argv)
    spec = load_spec(args.spec)
    notebook = render_notebook(
        spec,
        args.template,
        args.output.name,
        args.output,
        github_repo=args.github_repo,
        branch=args.branch,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(notebook, args.output)
    print(f"Rendered {args.output} ({len(notebook.cells)} cells)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
