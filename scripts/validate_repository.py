"""Check repository navigation, text, notebook integrity, and lean structure.

Uses only the Python standard library. Does not execute notebook code.
"""
from pathlib import Path
from urllib.parse import unquote, urlparse
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked_links = 0
checked_notebooks = 0
checked_text = 0
own_github = "https://github.com/Engr-Daniel/deep-learning-with-python-3e-study/blob/main/"
own_colab = "https://colab.research.google.com/github/Engr-Daniel/deep-learning-with-python-3e-study/blob/main/"


def source(cell):
    value = cell["source"]
    return "".join(value) if isinstance(value, list) else value


def code_digest(notebook):
    payload = json.dumps([source(c) for c in notebook["cells"] if c["cell_type"] == "code"], ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def inspect_text(text, location):
    global checked_text
    checked_text += 1
    if "\ufffd" in text or "\x00" in text:
        errors.append(f"{location}: replacement/null character")
    if re.search(r"[\u00c3\u00c2][\u0080-\u00bf]|\u00e2\u20ac|\u00f0\u0178", text):
        errors.append(f"{location}: possible mojibake")
    if re.search(r"(?m)^#{1,6} .* \? ", text):
        errors.append(f"{location}: suspicious question mark in heading")
    if re.search(r"(?m)^#{1,6} .*(?:[A-Za-z]\?[A-Za-z])", text):
        errors.append(f"{location}: possible lost letter in heading")


def inspect_links(text, origin):
    global checked_links
    # Handles ordinary Markdown links/images; strips code blocks so examples of
    # Markdown syntax do not become spurious links.
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for match in re.finditer(r"!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", text):
        raw = match.group(1).strip("<>")
        if raw.startswith(own_github) or raw.startswith(own_colab):
            prefix = own_github if raw.startswith(own_github) else own_colab
            relative = raw[len(prefix):]
            base = ROOT
        elif urlparse(raw).scheme or raw.startswith("//"):
            continue
        else:
            relative = raw
            base = origin.parent
        relative = unquote(relative.split("#", 1)[0].split("?", 1)[0])
        if not relative:
            continue
        target = (base / relative).resolve()
        checked_links += 1
        if not target.is_relative_to(ROOT):
            errors.append(f"{origin.relative_to(ROOT)}: link leaves repository: {raw}")
        elif not target.exists():
            errors.append(f"{origin.relative_to(ROOT)}: broken link: {raw}")
        elif "#" in raw and target.suffix == ".md":
            anchor = unquote(raw.split("#", 1)[1])
            headings = re.findall(r"(?m)^#{1,6}\s+(.+)$", target.read_text(encoding="utf-8"))
            anchors = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings}
            if anchor not in anchors:
                errors.append(f"{origin.relative_to(ROOT)}: missing heading anchor: {raw}")


manifest = json.loads((ROOT / "study/manifest.json").read_text(encoding="utf-8"))
chapters = manifest["chapters"]
if len(chapters) != 20 or {c["number"] for c in chapters} != set(range(1, 21)):
    errors.append("Manifest must describe all 20 chapters exactly once")
expected = set()
for chapter in chapters:
    directory = ROOT / chapter["directory"]
    if not (directory / "README.md").is_file():
        errors.append(f"Missing chapter overview: {directory}")
    if chapter["number"] <= 2 and not (directory / "NOTES.md").is_file():
        errors.append(f"Missing studied chapter notes: {directory}")
    for key in ("notebook", "experiment"):
        item = chapter.get(key)
        if not item:
            continue
        path = ROOT / item["path"]
        expected.add(path)
        if not path.is_file():
            errors.append(f"Missing notebook: {item['path']}")
            continue
        checked_notebooks += 1
        notebook = json.loads(path.read_text(encoding="utf-8"))
        if notebook.get("nbformat") != 4:
            errors.append(f"{path}: expected notebook format 4")
        if code_digest(notebook) != item["study_code_sha256"]:
            errors.append(f"{path.relative_to(ROOT)}: code differs from the recorded verified/prepared version")
        ids = [c["id"] for c in notebook["cells"] if "id" in c]
        if len(ids) != len(set(ids)):
            errors.append(f"{path}: duplicate cell IDs")
        if notebook.get("nbformat_minor", 0) < 5 or len(ids) != len(notebook["cells"]):
            errors.append(f"{path}: use notebook 4.5+ metadata with an ID on every cell")
        if any(not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", ident) for ident in ids):
            errors.append(f"{path}: invalid cell ID")
        for cell in notebook["cells"]:
            inspect_text(source(cell), path.relative_to(ROOT))
            if cell["cell_type"] == "markdown":
                inspect_links(source(cell), path)
            if cell["cell_type"] == "code":
                if any(o.get("output_type") == "error" for o in cell.get("outputs", [])):
                    errors.append(f"{path}: saved cell error")
                if item["execution_status"] == "not run" and (cell.get("execution_count") is not None or cell.get("outputs")):
                    errors.append(f"{path}: unrun status conflicts with saved execution")
        if key == "experiment" and not all(c.get("execution_count") is not None for c in notebook["cells"] if c["cell_type"] == "code"):
            errors.append(f"{path}: verified experiment has an unexecuted code cell")
        if key == "notebook" and len(item["upstream_sha256"]) != 64:
            errors.append(f"{path}: missing upstream hash")

actual = set((ROOT / "chapters").rglob("*.ipynb"))
if actual != expected:
    errors.append("Unexpected or duplicate notebook files: " + ", ".join(str(p.relative_to(ROOT)) for p in actual ^ expected))
if len([c for c in chapters if c.get("notebook")]) != 16:
    errors.append("Expected 16 official third-edition chapter notebooks")

for p in ROOT.rglob("*.md"):
    if any(part in {".git", ".tmp", ".notebook-source"} for part in p.parts):
        continue
    text = p.read_text(encoding="utf-8")
    inspect_text(text, p.relative_to(ROOT))
    inspect_links(text, p)
    if "Write concise explanations in your own words." in text or "Complete after Chapter 20." in text:
        errors.append(f"{p.relative_to(ROOT)}: unused template")

for p in (ROOT / "chapters").rglob(".gitkeep"):
    errors.append(f"Unused placeholder: {p.relative_to(ROOT)}")
for name in ("EXERCISES.md", "RUN_LOG.md", "NOTEBOOK_CHANGES.md", "LICENSE.upstream.txt"):
    if list((ROOT / "chapters").rglob(name)):
        errors.append(f"Duplicate/separate chapter record should be consolidated: {name}")
if not (ROOT / manifest["notebook_license"]).is_file():
    errors.append("Missing shared upstream license")

if errors:
    raise SystemExit("Repository checks failed:\n- " + "\n- ".join(errors))
print(f"Passed: 20 chapter overviews, {checked_notebooks} notebooks, code hashes, {checked_links} local links, and {checked_text} text blocks.")
print("No duplicate notebooks, empty chapter scaffolding, detected encoding damage, or saved cell errors.")
print("Static checks do not prove prose is typo-free or execute notebook code; run evidence is recorded in chapter overviews.")
