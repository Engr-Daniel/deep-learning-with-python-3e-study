# Running notebooks in Colab

Open a notebook through its chapter overview. Start in a fresh session and run cells in order. CPU is sufficient for the small Chapter 2 experiment; choose an accelerator when the chapter requires or benefits from it.

- Use the notebook’s setup cells. Preserve TensorFlow, PyTorch, JAX, and Keras distinctions. Set `KERAS_BACKEND` before importing Keras; restart before switching backends.
- Keep the environment-cell output with the notebook. Record a concise result and any environment-driven edit once under **Execution and changes** in the chapter README: original behavior, reason for the fix, change, and observed result.
- Preserve seeds where present; record versions and devices because exact metrics can vary. Do not guess new package pins before seeing an actual problem.
- Use interactive authentication or Colab secrets when required. Do not commit credentials or private outputs. Runtime storage is temporary; save the executed notebook to your repository if you want to keep it.
- Live sliders require notebook execution. Chapter 2 enables Colab’s widget manager; its static figures also remain readable without live controls.

## Notebook provenance

The 16 official third-edition copies cover Chapters 2–5 and 7–18. They are pinned to the source revision in [the manifest](../study/manifest.json), with one [upstream license notice](../THIRD_PARTY_NOTICES.md).

Study additions comprise a source header, environment recorder, and optional run-summary footer. Upstream outputs were cleared before study runs. Preparation did not change original code, backend settings, or seeds. Chapter 2’s later learner edits are declared in its overview and manifest; execution results remain in the notebooks. No placeholder notebooks are created for chapters without official code.

[Official runtime guidance](https://github.com/fchollet/deep-learning-with-python-notebooks#running-the-code).

## Optional local execution

Use a virtual environment with `requirements-core.txt` and the appropriate backend requirement file from this folder. `python scripts/check_environment.py` reports the local packages. Colab users do not need to install these files locally. Keep large datasets and model files outside version control.
