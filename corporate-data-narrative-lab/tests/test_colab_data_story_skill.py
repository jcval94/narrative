from __future__ import annotations

import importlib.util
import hashlib
import io
import sys
import zipfile
from pathlib import Path
from types import ModuleType

import nbformat
import pytest
import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / ".codex" / "skills" / "create-colab-data-story"


def load_module(name: str, relative_path: str) -> ModuleType:
    path = SKILL_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


catalog = load_module("colab_story_catalog", "scripts/catalog_stories.py")
renderer = load_module("colab_story_renderer", "scripts/render_notebook.py")
validator = load_module("colab_story_validator", "scripts/validate_notebook.py")
reviewer = load_module("colab_story_reviewer", "scripts/review_notebook.py")


def make_spec(concept_count: int, *, exercises: bool = False) -> dict:
    names = [f"Concepto {index}" for index in range(1, concept_count + 1)]
    concepts = []
    for index, name in enumerate(names, start=1):
        previous = "Punto de partida" if index == 1 else f"Concepto {index - 1} mostró el primer límite"
        concept = {
            "name": name,
            "connection_from_previous": previous,
            "question": f"¿Qué cambia al aplicar {name}?",
            "scene": (
                '> **La jefa:** "¿Entonces ya podemos decidir?"\n>\n'
                '> **La analista:** "Todavía no; la misma tabla dejó una duda concreta."'
            ),
            "learning_code": (
                f'resumen_{index} = df.groupby("group", as_index=False)["value"].mean()\n'
                f"resumen_{index}"
            ),
            "visualization_code": (
                f'vista_{index} = df.groupby("group", as_index=False)["value"].mean()\n'
                f'fig = px.bar(vista_{index}, x="group", y="value", color_discrete_sequence=["#2F5D62"], title="{name}<br><sup>n=4 observaciones de prueba</sup>")\n'
                'fig.update_traces(marker_line_color="#173F5F", hovertemplate="grupo=%{x}<br>media=%{y:.1f}<extra></extra>")\n'
                'fig.update_layout(xaxis_title="Grupo", yaxis_title="Media (unidades)", updatemenus=[{"buttons": [{"label": "Todos", "method": "update", "args": [{}]}]}])\n'
                "fig.show()"
            ),
            "interpretation": "La comparación usa las mismas observaciones y cambia la decisión sin inventar causalidad.",
            "metric_name": f"media_{index}",
            "metric_expression": f"resumen_{index}",
            "required_columns": ["group", "value"],
        }
        if exercises:
            concept["exercise_prompt"] = "Cambia el grupo y describe qué permanece igual."
        concepts.append(concept)

    return {
        "title": "Una decisión, varias preguntas",
        "level": "adaptive",
        "central_question": "¿Qué evidencia necesitamos antes de cambiar la operación?",
        "story_intro": (
            '> **La jefa:** "El promedio quedó bonito; ya podemos decidir."\n>\n'
            '> **La analista:** "Bonito sí. Primero veamos qué observaciones quedaron detrás."'
        ),
        "synthesis": "Cada concepto responde la limitación encontrada por el anterior usando la misma tabla.",
        "decision": "Comparar los grupos y documentar la incertidumbre antes de escalar.",
        "rule": "Una técnica nueva debe responder una limitación real de la anterior.",
        "dataframe_name": "df",
        "setup_code": (
            'segmento = "Todos" # @param ["Todos"]\n'
            "import pandas as pd\n"
            "import numpy as np\n"
            "import plotly.express as px\n"
            "from IPython.display import Markdown, display\n"
            'df = pd.DataFrame({"group": ["A", "A", "B", "B"], "value": [2, 4, 5, 9]})\n'
            "df.head()"
        ),
        "story": {
            "case_id": "05",
            "title": "Caso de prueba",
            "source_path": "examples/cases/05_case.md",
            "created_by_pipeline": False,
            "adaptations": ["Cifras reemplazadas por resultados ejecutados"],
        },
        "dataset": {
            "title": "Dataset de prueba",
            "publisher": "Publicador",
            "landing_url": "https://example.com/dataset",
            "data_url": "https://example.com/data.csv",
            "license": "CC-BY-4.0",
            "accessed_at": "2026-07-18",
            "format": "csv",
            "bytes": 100,
            "rows": 4,
            "columns": ["group", "value"],
            "sha256": "0" * 64,
            "supports_concepts": names,
        },
        "concepts": concepts,
        "image": None,
    }


@pytest.mark.parametrize("concept_count", [1, 3, 5])
def test_renders_and_validates_supported_concept_counts(concept_count: int) -> None:
    notebook = renderer.render_notebook(make_spec(concept_count))

    assert len(notebook.cells) == 7 + 3 * concept_count
    assert validator.notebook_errors(notebook) == []
    assert len(notebook.metadata.narrative_colab.concept_sequence) == concept_count


def test_allows_one_optional_exercise_per_concept_without_exceeding_cap() -> None:
    notebook = renderer.render_notebook(make_spec(5, exercises=True))

    assert len(notebook.cells) == 27
    assert validator.notebook_errors(notebook) == []


def test_rejects_more_than_five_concepts() -> None:
    with pytest.raises(ValueError, match="one and five"):
        renderer.render_notebook(make_spec(6))


def test_rejects_disconnected_concepts() -> None:
    spec = make_spec(3)
    spec["concepts"][1]["connection_from_previous"] = "Una pregunta completamente distinta"

    with pytest.raises(ValueError, match="must name the previous concept"):
        renderer.render_notebook(spec)


def test_rejects_untraceable_metric() -> None:
    notebook = renderer.render_notebook(make_spec(1))
    notebook.metadata.narrative_colab.metrics[0]["cell_id"] = "missing-cell"

    assert any("does not reference a learner cell" in error for error in validator.notebook_errors(notebook))


def test_normalizes_github_remotes_for_colab_links() -> None:
    assert renderer.normalize_github_repo("https://github.com/acme/course.git") == "acme/course"
    assert renderer.normalize_github_repo("git@github.com:acme/course.git") == "acme/course"


def test_rendered_notebook_includes_colab_badge_when_github_context_is_available() -> None:
    output_path = REPO_ROOT / "outputs" / "notebooks" / "story.ipynb"

    notebook = renderer.render_notebook(
        make_spec(1),
        output_path=output_path,
        github_repo="acme/course",
        branch="main",
    )

    colab_url = (
        "https://colab.research.google.com/github/acme/course/blob/main/"
        "corporate-data-narrative-lab/outputs/notebooks/story.ipynb"
    )
    assert notebook.metadata.narrative_colab.colab_url == colab_url
    assert "colab-badge.svg" in notebook.cells[0].source
    assert colab_url in notebook.cells[0].source
    assert validator.notebook_errors(notebook) == []


def test_validator_rejects_colab_metadata_without_title_badge() -> None:
    notebook = renderer.render_notebook(make_spec(1), output_path=REPO_ROOT / "outputs" / "notebooks" / "story.ipynb")
    notebook.metadata.narrative_colab.colab_url = (
        "https://colab.research.google.com/github/acme/course/blob/main/story.ipynb"
    )

    assert any("title cell must include" in error for error in validator.notebook_errors(notebook))


def test_network_validation_parses_real_payload_and_checks_schema(monkeypatch: pytest.MonkeyPatch) -> None:
    payload = b"group,value\nA,2\nA,4\nB,5\nB,9\n"
    spec = make_spec(1)
    spec["dataset"]["bytes"] = len(payload)
    spec["dataset"]["sha256"] = hashlib.sha256(payload).hexdigest()
    notebook = renderer.render_notebook(spec)

    def fake_fetch(url: str, **_: object) -> tuple[bytes, str]:
        if url.endswith("data.csv"):
            return payload, "text/csv"
        return b"<html>source</html>", "text/html"

    monkeypatch.setattr(validator, "fetch_bytes", fake_fetch)

    assert validator.network_errors(notebook) == []


def test_network_validation_supports_a_declared_csv_inside_zip(monkeypatch: pytest.MonkeyPatch) -> None:
    csv_payload = b"group,value\nA,2\nA,4\nB,5\nB,9\n"
    archive_buffer = io.BytesIO()
    with zipfile.ZipFile(archive_buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("table.csv", csv_payload)
    payload = archive_buffer.getvalue()
    spec = make_spec(1)
    spec["dataset"].update(
        {
            "data_url": "https://example.com/data.zip",
            "format": "zip",
            "member": "table.csv",
            "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
        }
    )
    notebook = renderer.render_notebook(spec)

    def fake_fetch(url: str, **_: object) -> tuple[bytes, str]:
        if url.endswith("data.zip"):
            return payload, "application/zip"
        return b"<html>source</html>", "text/html"

    monkeypatch.setattr(validator, "fetch_bytes", fake_fetch)

    assert validator.network_errors(notebook) == []


def test_catalog_discovers_current_collection() -> None:
    result = catalog.build_catalog(REPO_ROOT)

    assert result["case_count"] >= 18
    assert result["valid_count"] == result["case_count"]
    assert int(result["next_case_id"]) > max(int(case["case_id"]) for case in result["cases"])


def test_catalog_discovers_a_future_story_without_code_changes(tmp_path: Path) -> None:
    for directory in ("cases", "data_specs", "visual_specs", "html"):
        (tmp_path / "examples" / directory).mkdir(parents=True)
    stem = "42_historia_futura"
    (tmp_path / "examples" / "cases" / f"{stem}.md").write_text(
        """# Historia futura

<!-- story
concept: distribución
situation: un promedio cómodo
bad_logic: el promedio representa a todos
data_turn: el equipo abre percentiles
decision: revisar la cola
punchline: El promedio llegó a tiempo; los clientes no.
rule: revisar la distribución
synthetic_data: true
-->
""",
        encoding="utf-8",
    )
    for directory, suffix in (("data_specs", ".yml"), ("visual_specs", ".yml"), ("html", ".html")):
        (tmp_path / "examples" / directory / f"{stem}{suffix}").write_text("fixture", encoding="utf-8")

    result = catalog.build_catalog(tmp_path)

    assert result["case_count"] == 1
    assert result["cases"][0]["case_id"] == "42"
    assert result["next_case_id"] == "43"


def test_rendered_notebook_executes_top_to_bottom() -> None:
    pytest.importorskip("nbclient")
    notebook = renderer.render_notebook(make_spec(1))

    executed = validator.execute_notebook(notebook, timeout=120)

    code_cells = [cell for cell in executed.cells if cell.cell_type == "code"]
    assert all(cell.execution_count is not None for cell in code_cells)
    assert all("df" in cell.source for cell in code_cells if cell.metadata.narrative_role == "learner-code")


def test_independent_quality_review_stamps_and_invalidates_changed_sources() -> None:
    pytest.importorskip("nbclient")
    notebook = renderer.render_notebook(make_spec(1))
    executed = validator.execute_notebook(notebook, timeout=120)

    errors, figures = reviewer.quality_errors(executed)
    assert errors == []
    assert len(figures) == 1

    reviewer.stamp_review(executed, figures)
    assert validator.notebook_errors(executed) == []
    assert executed.metadata.narrative_colab.quality_review.status == "passed"

    executed.cells[1].source += "\n\nCambio posterior."
    assert any("quality review is stale" in error for error in validator.notebook_errors(executed))


def test_template_is_valid_nbformat() -> None:
    template = nbformat.read(renderer.DEFAULT_TEMPLATE, as_version=4)
    nbformat.validate(template)


def test_command_line_round_trip_renders_valid_executable_notebook(tmp_path: Path) -> None:
    spec_path = tmp_path / "spec.yml"
    notebook_path = tmp_path / "story.ipynb"
    spec_path.write_text(yaml.safe_dump(make_spec(1), allow_unicode=True, sort_keys=False), encoding="utf-8")

    assert renderer.main([str(spec_path), str(notebook_path)]) == 0
    assert validator.main([str(notebook_path), "--execute", "--timeout", "120"]) == 0

    notebook = nbformat.read(notebook_path, as_version=4)
    assert validator.notebook_errors(notebook) == []
