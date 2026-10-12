"""Basic structural sanity check for the study repository."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "TASK.md",
    ROOT / "MEMORY.md",
    ROOT / "study" / "PROGRESS.md",
]
missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
chapter_dirs = sorted((ROOT / "chapters").glob("ch*"))
if len(chapter_dirs) != 20:
    missing.append(f"expected 20 chapter directories, found {len(chapter_dirs)}")
for d in chapter_dirs:
    for name in ["README.md", "NOTES.md", "EXERCISES.md", "RUN_LOG.md"]:
        if not (d / name).exists():
            missing.append(str((d / name).relative_to(ROOT)))
if missing:
    raise SystemExit("Structure check failed:\n- " + "\n- ".join(missing))
print("Structure check passed: 20 chapter workspaces and core control files are present.")
