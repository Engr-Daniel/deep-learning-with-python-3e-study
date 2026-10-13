"""Validate notebook preparation and source preservation without running examples."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "study/notebook_sources.json").read_text(encoding="utf-8"))
seen = set()
for item in manifest["notebooks"]:
    path = ROOT / item["path"]
    notebook = json.loads(path.read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4, path
    assert item["chapter"] not in seen, path
    seen.add(item["chapter"])
    ids = [c["id"] for c in notebook["cells"] if "id" in c]
    assert len(ids) == len(set(ids)), f"Duplicate cell IDs: {path}"
    for c in notebook["cells"]:
        assert c["cell_type"] in {"code", "markdown", "raw"}, path
        if c["cell_type"] == "code":
            assert c["execution_count"] is None and c["outputs"] == [], path
    environment = next(c for c in notebook["cells"] if c.get("id") == "study-environment")
    ast.parse("".join(environment["source"]))
    source = ROOT / ".notebook-source" / path.name
    if source.exists():
        assert hashlib.sha256(source.read_bytes()).hexdigest() == item["upstream_sha256"], path
        original = json.loads(source.read_text(encoding="utf-8"))
        original_code = [c["source"] for c in original["cells"] if c["cell_type"] == "code"]
        current_code = [c["source"] for c in notebook["cells"]
                        if c["cell_type"] == "code" and c.get("id") != "study-environment"]
        assert original_code == current_code, f"Upstream code changed: {path}"
        # Existing narrative cells are preserved as well.
        current_original = [c for c in notebook["cells"] if c.get("id") not in
                            {"study-environment", "study-provenance", "study-run-evidence"}]
        assert [(c["cell_type"], c["source"]) for c in current_original] == [
            (c["cell_type"], c["source"]) for c in original["cells"]], path
    assert (path.parent / "LICENSE.upstream.txt").is_file(), path
    assert (path.parent.parent / "NOTEBOOK_CHANGES.md").is_file(), path
    assert "Not run" in "".join(notebook["cells"][0]["source"]), path

assert seen == set(range(1, 21)) - {1, 6, 19, 20}, seen
assert not any((ROOT / "chapters").glob("ch01-*/notebooks/*.ipynb"))
print(f"Validated {len(seen)} notebooks: structure, attribution, empty outputs, evidence-cell syntax.")
print("Compared all original cells against downloaded upstream files where available.")
print("No chapter examples executed; Colab runtime behavior remains unverified.")
