# Contributing

Corrections should improve understanding, reproducibility, or navigation. Use original explanations; do not copy book prose. Preserve the upstream notebook notice and record source/API changes accurately.

- Follow **read → run → apply**. Keep a single current notebook for each purpose.
- Add files when they contain real work. Use the chapter README for run/change evidence, NOTES.md for summaries, and experiments/ for an applicable project.
- Record the environment, backend, result, and reason for any compatibility change. A saved code cell is not proof it was executed.
- Keep visitor checks optional. Personal questions or reflections belong in notes only when actually reported.
- Run `python scripts/validate_repository.py` before publishing. Update the matching manifest hash when intentionally changing notebook code, after checking and executing the change. Narrative-only edits should preserve code hashes.

When using a fork, open that fork’s notebooks from Colab and save your work back to it. Avoid committing datasets, model binaries, or credentials.
