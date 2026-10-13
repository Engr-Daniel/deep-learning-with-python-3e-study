"""Prepare attributed study copies from a downloaded, pinned upstream snapshot.

Usage: python scripts/prepare_colab_notebooks.py SOURCE_DIRECTORY COMMIT_SHA
Upstream code is preserved exactly. This does not execute any chapter examples.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = "https://github.com/fchollet/deep-learning-with-python-notebooks"
STUDY = "https://github.com/Engr-Daniel/deep-learning-with-python-3e-study"
MISSING = {1, 6, 19, 20}
ENVIRONMENT_CELL = '''# Study addition: environment evidence; does not import ML frameworks.
# Run after the upstream backend-selection cell and before expensive training.
import datetime
import importlib.metadata
import json
import os
import platform
import shutil
import subprocess

study_environment = {
    "recorded_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "python": platform.python_version(),
    "platform": platform.platform(),
    "requested_keras_backend": os.environ.get("KERAS_BACKEND", "not explicitly set"),
    "packages": {},
}
for study_package in ("keras", "tensorflow", "torch", "jax", "jaxlib", "numpy", "kagglehub", "keras-hub"):
    try:
        study_environment["packages"][study_package] = importlib.metadata.version(study_package)
    except importlib.metadata.PackageNotFoundError:
        study_environment["packages"][study_package] = "not installed"
if shutil.which("nvidia-smi"):
    study_gpu = subprocess.run(
        ["nvidia-smi", "--query-gpu=name,driver_version,memory.total", "--format=csv,noheader"],
        capture_output=True, text=True, check=False,
    )
    study_environment["gpu"] = study_gpu.stdout.strip() or "GPU query unsuccessful"
else:
    study_environment["gpu"] = "nvidia-smi unavailable; check actual framework devices"
print(json.dumps(study_environment, indent=2))
# After framework imports, also record keras.backend.backend() and the framework device list.
'''


def cell(kind, source, identifier):
    result = {"cell_type": kind, "id": identifier, "metadata": {}, "source": source.splitlines(True)}
    if kind == "code":
        result.update(execution_count=None, outputs=[])
    return result


def write(path, text):
    path.write_text(text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("commit")
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.commit):
        raise SystemExit("Expected a full upstream commit SHA")
    files = sorted(args.source.glob("chapter*.ipynb"))
    numbers = {int(re.match(r"chapter(\d+)", p.name)[1]) for p in files}
    if numbers != set(range(1, 21)) - MISSING:
        raise SystemExit(f"Unexpected upstream chapter coverage: {sorted(numbers)}")
    license_text = (args.source / "LICENSE").read_text(encoding="utf-8")
    manifests = []
    index = ["# Official notebook index\n", f"Source: [third-edition repository]({UPSTREAM}), pinned at `{args.commit}`.\n",
             "Study copies are prepared for Colab but **not executed or runtime-validated**. Code and backend choices remain upstream originals.\n",
             "| Chapter | Study copy | Official source | Colab |\n|---:|---|---|---|"]
    for directory in sorted((ROOT / "chapters").glob("ch*")):
        number = int(directory.name[2:4])
        readme = directory / "README.md"
        original_readme = readme.read_text(encoding="utf-8")
        original_readme = original_readme.split("\n## Companion notebook\n")[0].rstrip()
        if number in MISSING:
            section = f"\n\n## Companion notebook\n\n[Official notebook repository]({UPSTREAM}). No third-edition notebook is published for Chapter {number} at the recorded revision. No placeholder notebook has been created. Follow the chapter text and use notes as appropriate.\n"
            write(readme, original_readme + section)
            index.append(f"| {number:02} | No official notebook | [Repository]({UPSTREAM}) | N/A |")
            continue
        source = next(p for p in files if int(re.match(r"chapter(\d+)", p.name)[1]) == number)
        notebook = json.loads(source.read_text(encoding="utf-8"))
        source_code = [c["source"] for c in notebook["cells"] if c["cell_type"] == "code"]
        title = original_readme.splitlines()[0].lstrip("# ")
        source_url = f"{UPSTREAM}/blob/{args.commit}/{source.name}"
        relative = f"chapters/{directory.name}/notebooks/{source.name}"
        study_colab = f"https://colab.research.google.com/github/Engr-Daniel/deep-learning-with-python-3e-study/blob/main/{relative}"
        official_colab = f"https://colab.research.google.com/github/fchollet/deep-learning-with-python-notebooks/blob/{args.commit}/{source.name}"
        header = f"""# {title} - Colab study notebook

**Edition:** Third edition. **Execution status:** Not run in this study workspace.

[Official source]({source_url}) | [Official Colab copy]({official_colab})

Upstream revision: `{args.commit}`. Notebook code by the official companion-notebook contributors; Copyright (c) 2017-present Francois Chollet, MIT license (see LICENSE.upstream.txt beside this notebook).

Read beside the chapter and run cells in order. Preserve the upstream backend selection: KERAS_BACKEND must be chosen before importing Keras. Restart the Colab session before changing backends. Chapter 3 demonstrates multiple frameworks; use its section-specific imports and setup.

Choose the Colab runtime for the section. Check accelerator availability before long runs. Use the upstream installation cells; no extra version pins or compatibility patches have been introduced. Use interactive login or Colab secrets when authentication is requested; do not save credentials in notebook cells.

The upstream code cells are unchanged. Saved outputs and execution counts were cleared. This study header, environment-recording cell, and run-evidence footer are the only new cells. See ../NOTEBOOK_CHANGES.md for the complete preparation record.

Preparation is not execution: only mark examples complete after running and inspecting their results.
"""
        for existing in notebook["cells"]:
            if existing["cell_type"] == "code":
                existing["execution_count"] = None
                existing["outputs"] = []
        # Locate the original backend-selection cell without changing its source.
        position = next((i + 1 for i, c in enumerate(notebook["cells"])
                         if c["cell_type"] == "code" and "KERAS_BACKEND" in "".join(c["source"])), 0)
        notebook["cells"].insert(position, cell("code", ENVIRONMENT_CELL, "study-environment"))
        notebook["cells"].insert(0, cell("markdown", header, "study-provenance"))
        notebook["cells"].append(cell("markdown", """## Study run evidence - fill after execution

- Date and sections actually run:
- Colab runtime, accelerator, package versions (copy environment-cell output):
- Actual backend and framework devices:
- Seeds used by the original example; any seed changes and reasons:
- Input/output shapes and observed metrics:
- Errors and fixes (cell/section, original behavior, change, reason, observed result):
- Result versus the intended lesson:
- Exact resume cell/section:

Record meaningful runs in ../RUN_LOG.md and conceptual notes in ../NOTES.md. Record every environment-driven edit in ../NOTEBOOK_CHANGES.md as well. Do not claim unrun cells succeeded.
""", "study-run-evidence"))
        assert [c["source"] for c in notebook["cells"] if c["cell_type"] == "code"
                and c.get("id") != "study-environment"] == source_code
        destination = directory / "notebooks"
        destination.mkdir(exist_ok=True)
        target = destination / source.name
        if target.exists():
            raise SystemExit(f"Refusing to overwrite an existing study notebook: {target}")
        write(target, json.dumps(notebook, ensure_ascii=False, indent=1) + "\n")
        write(destination / "LICENSE.upstream.txt", license_text)
        changes = f"""# Notebook preparation and environment changes - Chapter {number}

## Source and preparation (2026-10-13)

- [Official third-edition source]({source_url})
- Revision: `{args.commit}`
- Original SHA-256: `{hashlib.sha256(source.read_bytes()).hexdigest()}`
- Local notebook: `notebooks/{source.name}`
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
"""
        write(directory / "NOTEBOOK_CHANGES.md", changes)
        section = f"\n\n## Companion notebook\n\n- [Study notebook](notebooks/{source.name})\n- [Open study copy in Colab]({study_colab}) (available after these files are pushed to GitHub)\n- [Official source]({source_url})\n- [Open official copy in Colab]({official_colab})\n- [Preparation and environment change record](NOTEBOOK_CHANGES.md)\n\nExecution status: **Not run**. Run sections in chapter order, inspect outputs, and record actual Colab environment and results in RUN_LOG.md.\n"
        write(readme, original_readme + section)
        manifests.append({"chapter": number, "path": relative, "source_url": source_url,
                          "upstream_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                          "execution_status": "not run", "upstream_code_unchanged": True})
        index.append(f"| {number:02} | [{source.name}](../{relative}) | [Source]({source_url}) | [Study]({study_colab}) / [Official]({official_colab}) |")
    write(ROOT / "study/NOTEBOOKS.md", "\n".join(index) + "\n")
    write(ROOT / "study/notebook_sources.json", json.dumps({"repository": UPSTREAM, "revision": args.commit,
          "notebooks": manifests, "chapters_without_official_notebooks": sorted(MISSING)}, indent=2) + "\n")
    print(f"Prepared {len(manifests)} attributed study notebooks; chapter code not executed.")


if __name__ == "__main__":
    main()
