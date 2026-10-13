# Environment and Colab workflow

## Primary runtime: Google Colab

The learner will run all chapter notebooks in Colab. Open the relevant study copy through [the notebook index](../study/NOTEBOOKS.md). If a study copy has not been pushed yet, upload the local .ipynb to Colab or use the indexed official copy.

1. Read alongside the chapter and execute sections in chapter order.
2. Select the runtime/accelerator appropriate to the section. The authors recommend Colab GPU runtimes; confirm what is available in your session before long training runs.
3. Run the original installation and backend-selection cells. The upstream notebooks use Keras 3 and preserve TensorFlow, JAX, and PyTorch distinctions. Backend requirements can differ by section.
4. Run the added environment-evidence cell after backend selection. It records Python/package versions, requested backend, and available NVIDIA GPU information without importing the frameworks. After framework imports, also record the actual backend and devices.
5. Inspect inputs, tensor shapes, predictions, and metrics. Save meaningful evidence in the chapter RUN_LOG.md; notebook preparation alone does not count as execution.
6. When an error occurs, record the exact cell, traceback, versions, proposed change, reason, and observed result. Explain the API/backend difference before changing it. Put every compatibility edit in NOTEBOOK_CHANGES.md.
7. Use the notebook run-evidence footer to capture the exact resume cell/section, seed behavior, and lesson learned. Save the notebook back to this repository after the session if you want its executed state preserved here; running in Colab does not automatically update this checkout.

Set KERAS_BACKEND before importing Keras. Restart the Colab session before switching backends; changing the environment variable after imports is insufficient.

Preserve the authors' package installation commands for the first run rather than guessing new pins. They may upgrade packages, so record the versions actually installed. No Colab compatibility fixes or extra version pins have been introduced during preparation.

For authenticated datasets/models, follow the original login cells and use interactive authentication or Colab secrets. Do not put credentials in cells, saved output, or Git. Colab sessions and locally downloaded files are temporary; rerun setup after a reset.

Official guidance: [companion repository README](https://github.com/fchollet/deep-learning-with-python-notebooks#running-the-code).

## Optional local environment

Local framework installation is optional. The existing requirements files remain available for local practice: install requirements-core.txt and the appropriate backend requirements in a virtual environment, then run python scripts/check_environment.py. Record actual environment details for any meaningful local run as well.
