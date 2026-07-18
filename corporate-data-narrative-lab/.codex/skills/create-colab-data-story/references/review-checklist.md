# Colab Data Story Review Checklist

Apply this only after the notebook has executed successfully once. Review the
rendered outputs, not only source code. Revise before stamping when any answer
is no.

## Evidence pass

- Does every stated number appear in an executed learner result or figure?
- Do independent spot calculations reproduce the mean, quantiles, counts, or
  other metrics that change the decision?
- Are population, units, filters, missing-value treatment, and sample size
  visible near the evidence?
- Does the conclusion avoid causality, representativeness, or precision the
  data cannot support?

## Visual pass

- Does each figure answer the concept question in one glance before hover?
- Are the family, scale, bins, axes, units, ordering, and reference marks honest?
- Does the title say what is plotted and does the subtitle state filter, scope,
  or sample size?
- Are colors explicit, restrained, accessible, and paired with shape, label, or
  line style when meaning would otherwise depend on color?
- Does hover expose useful values? Does every concept add a native control or
  clearly reuse the shared Colab parameter?
- Are labels, legends, annotations, and long values unclipped in the executed
  notebook at a normal laptop width?

## Narrative pass

- Does the opening contain a concrete decision, pressure, and at least two
  people who sound like people?
- Does each line respond to the previous line, and does the bad logic become
  absurd through a consequence rather than a decorative joke?
- Does the next concept answer a limitation exposed by the previous one using
  the same dataframe and decision?
- Does the data create the turn? If the original story disagreed, were its
  numbers, conflict, and ending adapted?
- Is each interpretation specific to its figure? Can a reader explain the
  decision and rule without rereading the prose?

## Final gate

Run `review_notebook.py NOTEBOOK.ipynb --execute --stamp`. Then rerun structural
validation. Any later source edit invalidates the stamp and requires both gates
again.
