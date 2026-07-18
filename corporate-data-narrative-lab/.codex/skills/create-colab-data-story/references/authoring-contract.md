# Colab Data Story Authoring Contract

## Contents

1. Repository and story contract
2. Concept-chain contract
3. Real-data contract
4. Canonical story creation
5. Notebook specification
6. Visual, code, and image rules
7. Double-check and handoff

## 1. Repository and story contract

Discover cases from `examples/cases/*.md` every time. Parse the `<!-- story
... -->` block and require the paired data spec, visual spec, and HTML. Do not
keep a hard-coded story list: a newly valid case must become selectable without
changing this skill.

Analyze all cases before creating one. Rank up to three candidates using:

- coverage of every requested concept;
- similarity of the decision and bad logic;
- availability of one real dataset for the complete chain;
- ability to preserve the case rule without overstating the evidence.

The data is authoritative. A source case supplies structure, characters, humor,
and pressure; it does not supply facts for the notebook. Mark the notebook
story as a narrative recreation. Never attribute invented dialogue to a real
person or organization.

## 2. Concept-chain contract

Accept one to five concepts. If the user gives an unordered set, use
`00_curriculum_mapper` and `DATA_SCIENCE_CURRICULUM.md` to order concepts from
the minimum sufficient technique toward the more conditional technique.

Use one story, one central decision, one real dataset, and one dataframe. Each
concept after the first must:

1. name the immediately previous concept in `connection_from_previous`;
2. consume a result or limitation revealed by it;
3. ask a new question about the same decision;
4. be supported by declared dataset columns.

Reject a chain that needs unrelated datasets or independent mini-stories.
Recommend splitting six or more concepts across notebooks.

## 3. Real-data contract

Prefer sources in this order:

1. direct download from the original public agency, university, or publisher;
2. an open repository maintained by that publisher;
3. a Kaggle dataset with original provenance and anonymous access.

Before writing the story:

- verify the HTTPS landing page and data URL;
- require an explicit redistribution or use license;
- perform a real GET and parse the data;
- record access date, format, byte size, row count, columns, and SHA-256;
- inspect missingness, types, distributions, segments, and temporal coverage;
- cap the download at 25 MB unless a documented server-side subset is used;
- declare which concepts the dataset supports.

Prefer direct CSV, JSON, JSON Lines, or NDJSON. For a ZIP download, declare the
single tabular `member` to read and keep the complete archive below 25 MB.

Reject authentication, rule acceptance, ambiguous licenses, unexplained
mirrors, sensitive personal data, and data that only supports the desired
conclusion after cherry-picking. If availability changes, show an actionable
error with the source link. Do not substitute synthetic data.

## 4. Canonical story creation

When no existing case survives the data check, use the observed pattern as the
input and execute this repository workflow. Before each step, read that skill's
`.codex/skills/<skill-name>/skill.md` plus its checklist, anti-patterns, and
examples when present; do not imitate the style from memory:

1. `00_curriculum_mapper`: choose the primary concept and minimum technique.
2. `01_case_thesis_builder`: complete the ten-field spine.
3. `02_corporate_conflict_builder`: create competent, incompatible positions.
4. `09_business_decision_simulator`: make the wrong decision comfortable,
   defensible, and dangerous.
5. `03_data_signal_designer`: define the one signal that changes the decision.
6. `04_synthetic_evidence_generator`: create only the canonical synthetic
   evidence specification; do not copy the real dataset.
7. `10_pilot_designer`: apply only when the decision is a pilot or intervention.
8. `11_ethics_and_risk_reviewer`: block sensitive data or harmful automation.
9. `05_simple_visual_builder`: create exactly one canonical SVG.
10. `06_narrative_case_writer`: write 450-700 words and three to five scenes.
11. `07_tragicomic_editor`: make incentives and bureaucracy produce the humor.
12. `08_learning_designer`: add one natural pause and short explanation.
13. `12_senior_data_reviewer`: fail unsupported causality or weak evidence.
14. `13_html_story_renderer`: render the canonical HTML.
15. `14_quality_gatekeeper`: validate the case and collection.

Assign the next available numeric ID from `catalog_stories.py --next-id`. Save
the Markdown, data spec, visual spec, and HTML using one shared stem. Preserve
`synthetic_data: true`. The canonical case has one primary concept; place
supporting concepts only in notebook metadata.

## 5. Notebook specification

Pass YAML with this shape to `render_notebook.py`:

```yaml
title: "Short notebook title"
level: "beginner|intermediate|adaptive"
central_question: "Decision question"
story_intro: "Brief recreated opening"
synthesis: "How the concepts change the reading together"
decision: "Concrete decision after seeing the data"
rule: "Transferable rule"
dataframe_name: "df"
setup_code: |
  segment = "All" # @param ["All"]
  DATA_URL = "https://...csv"
  import pandas as pd
  import numpy as np
  import plotly.express as px
  from IPython.display import Markdown, display
  df = pd.read_csv(DATA_URL)
  df.head()
story:
  case_id: "05"
  title: "Canonical title"
  source_path: "examples/cases/05_case.md"
  created_by_pipeline: false
  adaptations: ["Numbers replaced with executed metrics"]
dataset:
  title: "Dataset title"
  publisher: "Publisher"
  landing_url: "https://..."
  data_url: "https://...csv"
  license: "License identifier"
  accessed_at: "YYYY-MM-DD"
  format: "csv"
  # member: "table.csv" # required only when format is zip
  bytes: 12345
  rows: 1000
  columns: [group, value]
  sha256: "64 lowercase hexadecimal characters"
  supports_concepts: ["Aggregation"]
concepts:
  - name: "Aggregation"
    connection_from_previous: "Starting point"
    question: "What does the average hide?"
    scene: "One short scene beat"
    learning_code: |
      summary = df.groupby("group")["value"].mean()
      summary
    visualization_code: |
      fig = px.bar(summary.reset_index(), x="group", y="value")
      fig.update_layout(updatemenus=[{"buttons": [{"label": "All", "method": "update", "args": [{}]}]}])
      fig.show()
    interpretation: "Executed reading, without invented causality."
    metric_name: "group_mean"
    metric_expression: "summary"
    required_columns: [group, value]
    exercise_prompt: "Optional single-cell learner prompt"
image: null
```

`render_notebook.py` assigns cell IDs and binds each metric to its learning
cell. When the output path is inside a GitHub worktree, it also writes an
"Abrir en Colab" badge into the title cell and stores the same URL in
`metadata.narrative_colab.colab_url`. Pass `--github-repo` and `--branch` when
the notebook should point to a specific published repository or branch. Keep
temporary specifications outside the final output unless the user requests them.

## 6. Visual, code, and image rules

Build five shared cells, three cells per concept, and two closing cells. This is
`7 + 3n` cells. Add at most one Markdown exercise cell per concept and never
exceed 27 cells. Excluding the source cell, allow at most
`250 + 100 * (n - 1)` Markdown words.

Use pandas and NumPy for analysis. Use Plotly for hover, zoom, selection,
legends, and at least one figure-native dropdown, slider, or animation. Reuse a
figure when it makes the progression clearer; otherwise allow one primary
visualization per concept. Import Plotly in the hidden setup cell and install it
quietly there only after an `ImportError`; never expose installation code to the
learner.

Put setup, loading, cleaning, helpers, and plots in cells with
`cellView: form`. Start hidden cells with `# @title`. Include a `# @param`
control in setup and make global filters affect every concept. Keep exactly one
visible learner code cell per concept, no longer than eight nonblank lines.
Shared notebooks must expose the Colab badge from the first Markdown cell, not
only in external documentation.

Allow zero or one contextual online image. Require an HTTPS image URL, HTTPS
source page, license, credit, and alt text. Verify that the URL returns an image
content type. Omit an image that is merely decorative or cannot be licensed.

## 7. Double-check and handoff

Run structural validation, live-source validation, and the first execution:

```powershell
python .codex/skills/create-colab-data-story/scripts/validate_notebook.py NOTEBOOK.ipynb --check-network --execute
```

Then read the executed artifact and apply `review-checklist.md`. Run a second,
fresh execution plus rendered-output review:

```powershell
python .codex/skills/create-colab-data-story/scripts/review_notebook.py NOTEBOOK.ipynb --execute --stamp
```

The second gate must find one executed learner result and one labeled Plotly
figure per concept. Every figure needs hover or direct labels, its own native
control, an explicit non-default palette, honest axes, units or meaning, and a
title with a contextual subtitle. The story needs at least two speaking
characters, a contradiction that the data resolves, distinct interpretations,
and a decision no stronger than the executed evidence. The PASS stamp is bound
to notebook sources; any later source or narrative-metadata edit makes it stale.

Also validate every newly persisted canonical case with the repository case,
HTML, and collection validators. Hand off the notebook path, source status, and
any execution gap. Never write a takeaway before inspecting executed outputs.
Do not hand off without two passing gates and a current quality-review stamp.
