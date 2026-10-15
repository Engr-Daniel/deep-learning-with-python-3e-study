# Run Log

| Date | File | Backend/device | Result | Notes |
|---|---|---|---|---|

## Learner book-following run ? reported 2026-10-15

- File: `notebooks/chapter02_mathematical_building_blocks.ipynb` (learner-saved filename).
- Reading and notebook execution: learner reports complete. Saved file inspected: 75 code cells; 73 have execution counts; no saved error outputs. Two cells without counts remain unverified from the file alone.
- Saved environment evidence: Python 3.13.15, TensorFlow 2.21.0, Keras 3.15.1, NumPy 2.1.3; requested Keras backend TensorFlow; Tesla T4. The assistant did not independently run this saved notebook in Colab.
- Learner practice edits expose rank/shape and slicing outputs. No environment fix was reported; no successful metric is inferred from the absence of errors.

## Assistant development run - 2026-10-15

- File: `experiments/chapter02_interactive_foundations_lab.ipynb`.
- Full sequential execution completed: all 15 teaching code cells. Development assertions and alternate widget callback checks passed.
- Environment: Windows CPU, Python 3.10.0, TensorFlow/Keras 2.11.0, NumPy 1.24.1, Matplotlib 3.7.0, ipywidgets 8.1.5. Seed 2026; cached real MNIST used. No package changes.
- Configuration: 6,000 training images; 1,000 held-out images; 784 -> 32 ReLU -> 10 output scores; SGD learning rate 0.1; batch size 128; three epochs.
- Observed training loss: 2.309777 -> 0.538247. Held-out loss: 0.634320; accuracy: 0.821 (82.1%). These are demonstration results, not promised thresholds for a future Colab run.
- Numerical checks: tiny matrix product/ReLU, reshape invariants, analytic versus finite-difference/autodiff gradients, matching parameter/gradient shapes, probability row sums, toy descent versus divergence, and default training loss decrease.
- Interactivity checks: alternate batch/crop/neuron/geometry/learning-rate/prediction arguments and actual widget trait changes triggered kernel callbacks. Colab browser rendering/dragging was not tested.
- Fix required: local sandbox initially blocked secure Jupyter connection files; reran with execution approval. A Windows event-loop warning required no code change. Colab-specific widget-manager branch was not exercised locally.
- Evidence: executed experiment notebook and `outputs/ch02_lesson_execution.json`.
- Learner completion of the new experiment and teach-back: pending.

## Learner experiment completion and teaching revision — 2026-10-15

- Learner reports the interactive experiment is done. Preserved their executed notebook in `outputs/ch02_learner_lab_before_teaching_revision.ipynb`; the code was identical to the prior teaching copy, with 15 executed code cells and no saved error outputs.
- The saved summary describes a CPU Colab environment: Python 3.13.16, TensorFlow 2.21.0, Keras 3.13.2, NumPy 2.1.3, Matplotlib 3.10.0, ipywidgets 7.7.1. These are values saved in the learner’s file, not independently inspected live by the assistant.
- The training cell’s execution count is 18; evaluation is 14 and summary 15. The saved summary therefore predates the final saved training run. Preserved it with that limitation in `outputs/ch02_learner_saved_summary_2026-10-15.json`; no metrics are claimed for that final training state.
- Revised the visitor-facing lesson: clearer prerequisites and vocabulary, worked examples, guided controls, shape/parameter calculations, twelve knowledge checks plus a transfer task, smaller training code blocks, and a fresh transfer task. Added a guard against stale evaluation/prediction summaries after retraining.
- Executed all 20 revised code cells in sequence on local Windows CPU, Python 3.10.0, TensorFlow/Keras 2.11.0, NumPy 1.24.1, Matplotlib 3.7.0, ipywidgets 8.1.5. Seed/configuration unchanged; no package changes.
- Result: initial/final training loss 2.309777/0.538247; held-out loss 0.634320, accuracy 0.821. Targeted assertions checked all worked learning-rate numbers, the transfer problem, softmax values, parameter/batch counts, callbacks, and rejection of stale browser/summary use.
- Evidence: executed main experiment and `outputs/ch02_lesson_revision_execution.json`. Local Jupyter shutdown logged an interrupt, but all teaching cells and assertions completed, with no notebook error outputs.
- Execution checks establish computational correctness, not visitor comprehension. Revised Colab browser behavior and independent visitor teach-back remain unverified. Learner experiment completion is recorded; their Chapter 2 recap remains pending.
