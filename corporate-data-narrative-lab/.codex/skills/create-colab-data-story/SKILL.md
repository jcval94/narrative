---
name: create-colab-data-story
description: Create and validate compact, interactive Google Colab notebooks that teach one to five connected data-science concepts through one narrative, one public real-world dataset, and Plotly interactions. Use when Codex must select or create a story from this repository, adapt narrative claims to executed data, persist a new canonical case through the local story skills when needed, or produce an executable .ipynb with hidden implementation code and simple learner-facing Python.
---

# Create Colab Data Story

Produce a Colab tutorial in which one real dataset governs the narrative. Treat
the repository story as a teaching frame, never as evidence.

## Required context

1. Read `references/authoring-contract.md` completely.
2. Read `DATA_SCIENCE_CURRICULUM.md`, `ABSURD_OFFICE_COMEDY_DATA_STANDARD.md`,
   and `CODEX_WORKFLOW.md` from the repository root.
3. Run `scripts/catalog_stories.py --strict --json` instead of assuming how
   many cases exist.

## Workflow

1. Lock the theme, audience, central decision, and an ordered sequence of one
   to five connected concepts. Stop and recommend multiple notebooks for six
   or more concepts.
2. Rank every discovered case by coverage of the entire concept sequence.
   Inspect the best three candidates before selecting one.
3. Find one public dataset that supports every concept without credentials.
   Prefer the original publisher; use Kaggle only when provenance, license,
   and anonymous download are verified.
4. Download and inspect the real data before finalizing any story claim.
   Confirm schema, rows, missingness, distributions, segments, dates, license,
   byte size, and SHA-256.
5. Let evidence veto the story. Adapt numbers, context, conflict, turn, and
   conclusion whenever executed results disagree with the source case.
6. If no case fits, create and persist a canonical case by following the local
   skills in the exact order defined by the authoring contract. Preserve
   `synthetic_data: true` for that canonical artifact; never copy personal or
   raw real-world records into it.
7. Write a temporary YAML notebook specification following the contract.
   Use one story, one dataframe, one decision, and one ordered concept chain.
8. Render with `scripts/render_notebook.py` and validate with
   `scripts/validate_notebook.py`. Execute top-to-bottom before handoff.
9. When the notebook will be shared from GitHub, include a direct Colab badge.
   Let the renderer infer `remote.origin.url`, branch, and notebook path, or pass
   `--github-repo owner/repo --branch branch-name` explicitly.

## Notebook rules

- Build `7 + 3 * concept_count` cells; allow at most one optional exercise cell
  per concept and never exceed 27 cells.
- Keep narrative Markdown within `250 + 100 * (concept_count - 1)` words,
  excluding the source cell.
- Use pandas and NumPy for analysis and Plotly for interactive evidence.
- Match the user's language; default to Latin American Spanish when unspecified.
- Hide setup, loading, cleaning, helper calculations, and plotting code with
  `cellView: form`.
- Leave at most one learner code cell per concept, each no longer than eight
  nonblank lines.
- Include at least one Colab `# @param` control. Reuse global filters across
  concepts and reuse a figure when that makes the progression clearer.
- Include an "Abrir en Colab" badge in the title cell whenever the output path
  can be resolved to a GitHub URL. Keep the same URL in
  `metadata.narrative_colab.colab_url`.
- Attach every stated metric to the learner cell that calculates it through
  `metadata.narrative_colab.metrics`.
- Use at most one online image and only with a verified HTTPS URL, source page,
  license, credit, and alt text.

## Commands

Run from `corporate-data-narrative-lab`:

```powershell
python .codex/skills/create-colab-data-story/scripts/catalog_stories.py --strict --json
python .codex/skills/create-colab-data-story/scripts/render_notebook.py spec.yml outputs/notebooks/case.ipynb --github-repo owner/repo --branch main
python .codex/skills/create-colab-data-story/scripts/validate_notebook.py outputs/notebooks/case.ipynb --execute --check-network
```

Do not hand off a notebook that fails validation. If a live source cannot be
verified, select another source; never fall back silently to synthetic data.
