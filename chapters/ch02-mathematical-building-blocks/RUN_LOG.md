# Run Log

| Date | File | Backend/device | Result | Notes |
|---|---|---|---|---|

## Learner book-following run ? reported 2026-10-15

- File: `notebooks/chapter02_mathematical_building_blocks.ipynb` (learner-saved filename).
- Reading and notebook execution: learner reports complete. Saved file inspected: 75 code cells; 73 have execution counts; no saved error outputs. Two cells without counts remain unverified from the file alone.
- Saved environment evidence: Python 3.13.15, TensorFlow 2.21.0, Keras 3.15.1, NumPy 2.1.3; requested Keras backend TensorFlow; Tesla T4. The assistant did not independently run this saved notebook in Colab.
- Learner practice edits expose rank/shape and slicing outputs. No environment fix was reported; no successful metric is inferred from the absence of errors.

## Assistant development run ? 2026-10-15

- File: `experiments/chapter02_interactive_foundations_lab.ipynb`.
- Full sequential execution completed: all 15 teaching code cells. Development assertions and alternate widget callback checks passed.
- Environment: Windows CPU, Python 3.10.0, TensorFlow/Keras 2.11.0, NumPy 1.24.1, Matplotlib 3.7.0, ipywidgets 8.1.5. Seed 2026; cached real MNIST used. No package changes.
- Configuration: 6,000 training images; 1,000 held-out images; 784 ? 32 ReLU ? 10 output scores; SGD learning rate 0.1; batch size 128; three epochs.
- Observed training loss: 2.309777 ? 0.538247. Held-out loss: 0.634320; accuracy: 0.821 (82.1%). These are demonstration results, not promised thresholds for a future Colab run.
- Numerical checks: tiny matrix product/ReLU, reshape invariants, analytic versus finite-difference/autodiff gradients, matching parameter/gradient shapes, probability row sums, toy descent versus divergence, and default training loss decrease.
- Interactivity checks: alternate batch/crop/neuron/geometry/learning-rate/prediction arguments and actual widget trait changes triggered kernel callbacks. Colab browser rendering/dragging was not tested.
- Fix required: local sandbox initially blocked secure Jupyter connection files; reran with execution approval. A Windows event-loop warning required no code change. Colab-specific widget-manager branch was not exercised locally.
- Evidence: executed experiment notebook and `outputs/ch02_lesson_execution.json`.
- Learner completion of the new experiment and teach-back: pending.
