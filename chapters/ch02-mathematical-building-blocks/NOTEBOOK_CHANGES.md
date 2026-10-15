# Notebook preparation and environment changes - Chapter 2

## Source and preparation (2026-10-13)

- [Official third-edition source](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/fbf7f1bf2041093c4081e72544ec5905ace9dc8f/chapter02_mathematical-building-blocks.ipynb)
- Revision: `fbf7f1bf2041093c4081e72544ec5905ace9dc8f`
- Original SHA-256: `87927adbfa5dd031d237f54edbc3703e8fbc909ec60ea3dc7e1c0c6e2ce5a16e`
- Local notebook: `notebooks/chapter02_mathematical_building_blocks.ipynb`
- MIT notice preserved in `notebooks/LICENSE.upstream.txt`.
- Added a labeled provenance/Colab guide cell, an environment-evidence code cell after the original backend selection (or before examples if absent), and a run-evidence footer.
- Original code-cell sources preserved exactly, including backend settings, installation commands, and seeds.
- Cleared original outputs and execution counts so upstream results are not mistaken for study execution.
- Environment/API compatibility changes: **none**. No extra package pins or backend substitutions.
- Verification: valid notebook JSON, upstream code sources compared exactly, outputs empty. **Chapter code not executed; Colab behavior not yet verified.**

## Future changes

Record each change before considering an example complete:

| Date | Cell/section | Observed issue and environment | Original code | Change | Why it preserves the lesson | Result after execution |
|---|---|---|---|---|---|---|

Keep credentials out of this log. Explain API/backend differences before applying a fix.

## Learner-saved notebook and original experiment - 2026-10-15

- The learner supplied `notebooks/chapter02_mathematical_building_blocks.ipynb`, replacing the hyphenated local filename. Preserved the file and updated local links/manifest; official source URLs remain unchanged.
- Inspected saved code relative to the prior study copy: a rank-3 array example now displays its rank/shape, and slice examples display their shapes. These are learner practice edits, not compatibility fixes introduced by the assistant.
- The file has 75 code cells, 73 with execution counts, and no saved error outputs. The learner reports completing the notebook. The original header's preparation status is historical; it does not override the saved execution evidence.
- Saved environment output reports Python 3.13.15, TensorFlow 2.21.0, Keras 3.15.1, NumPy 2.1.3, TensorFlow backend, and Tesla T4. These values are from the learner's file, not independently measured in Colab by the assistant.
- Added a separate original experiment under `experiments/`. Deliberate scope choices: direct TensorFlow variables/GradientTape, the tf.keras MNIST loader, a 32-unit hidden layer, 6,000/1,000 sample subsets, and plain mini-batch SGD. They make operations visible and keep CPU runtime short; they do not patch the official notebook.
- Local development used existing TensorFlow/Keras 2.11.0 rather than installing Colab's newer versions. The new experiment avoids Keras-3-specific APIs; no package upgrades, downgrades, or changes to the book-following notebook were made by the assistant.
- Initial local Jupyter startup failed because sandbox permissions prevented secure connection-file ACLs; reran with execution approval. This required no mathematical or package compatibility change.
- The new lab ran completely on local CPU, including alternate-control and widget callback checks. Colab browser interactions remain unverified. See `experiments/README.md`, RUN_LOG.md, and `outputs/ch02_lesson_execution.json`.

## Visitor-focused lesson revision — 2026-10-15

- The learner reported completing the experiment and requested stronger explanations for visitors. Preserved their executed experiment snapshot before revising the working lesson.
- Expanded teaching text with explanations before code, worked calculations, controlled slider activities, output interpretation, misconception checks, hints, and transfer practice. Split the large MNIST code cell into six smaller cells without changing its mathematical operations.
- Behavioral fix: after a retraining cell runs, older evaluation can become stale. Added training/evaluation records; training invalidates evaluation, and prediction browsing/run summaries reject old evaluation. Reason: visitors must connect the displayed predictions to the parameters actually evaluated.
- No environment compatibility patches, backend substitutions, package installations, or official notebook edits were introduced. Colab widget setup is unchanged.
- The revision ran fully on local CPU. Training/evaluation values match the earlier development defaults. See RUN_LOG.md and `outputs/ch02_lesson_revision_execution.json` for actual versions and verification limits.
