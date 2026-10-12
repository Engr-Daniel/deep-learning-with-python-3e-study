"""Print the study environment without requiring every backend to be installed."""
from __future__ import annotations

import importlib
import os
import platform
import sys

PACKAGES = ["numpy", "matplotlib", "pandas", "sklearn", "keras", "tensorflow", "torch", "jax"]

print(f"Python: {sys.version.split()[0]}")
print(f"Platform: {platform.platform()}")
print(f"KERAS_BACKEND: {os.environ.get('KERAS_BACKEND', '<not set>')}")
print()
print("Packages:")
for name in PACKAGES:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "<unknown>")
        print(f"  {name:12s} {version}")
    except Exception as exc:
        print(f"  {name:12s} not available ({type(exc).__name__})")
