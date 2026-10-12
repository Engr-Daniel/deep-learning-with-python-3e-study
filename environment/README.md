# Environment

The third edition introduces **TensorFlow, PyTorch, JAX, and Keras**. Keras can run with TensorFlow, JAX, or PyTorch backends, so this repo keeps backend installation modular.

## Recommended workflow

1. Create a fresh Python virtual environment.
2. Install `requirements-core.txt`.
3. Install the backend required for the current section from one of the backend requirement files.
4. Run `python scripts/check_environment.py`.
5. Record actual package versions in the chapter `RUN_LOG.md` when version differences matter.

## Keras backend

Keras backend choice should be explicit when a lesson depends on it. The environment variable `KERAS_BACKEND` must be set before importing Keras.

Examples:

```bash
# Linux/macOS
export KERAS_BACKEND=tensorflow
# or jax / torch
```

On Windows PowerShell:

```powershell
$env:KERAS_BACKEND="tensorflow"
```

Do not assume all accelerator combinations install identically on every OS or GPU. Use the official framework installation instructions when GPU-specific packages are required.
