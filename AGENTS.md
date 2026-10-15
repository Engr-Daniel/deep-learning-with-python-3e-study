# AGENTS.md

## Purpose

This repository is a guided learning workspace for completing *Deep Learning with Python, Third Edition* from beginning to end, including code execution.

## Non-negotiable rules

1. **Preserve learning integrity.** Explain concepts; do not replace the learner's thinking with unexplained answers.
2. **Do not copy the book.** Store original summaries, paraphrases, code adaptations, references, and learning notes only.
3. **Follow chapter order** unless the learner explicitly changes the plan.
4. **Minimum daily reading target is 5 pages.** Treat this as a floor, not a forced ceiling.
5. **Code must be executed.** Do not mark a practical section complete merely because code has been transcribed.
6. **Record evidence.** For meaningful runs, note environment, backend, result, and any fix required.
7. **Never fabricate execution.** If code was not run, state that it was not run.
8. **Prefer understanding over blind compatibility patches.** When a package/API difference appears, explain why before changing code.
9. **Respect framework context.** The book introduces TensorFlow, PyTorch, JAX, and Keras. Preserve backend-specific distinctions when they matter.
10. **Keep experiments reproducible.** Set seeds where pedagogically appropriate and record version-sensitive behavior.

## File discipline

- Chapter concepts → `chapters/chXX-*/NOTES.md`
- Book-following code → `chapters/chXX-*/notebooks/`
- Independent practice → `chapters/chXX-*/experiments/`
- Execution/environment changes → the chapter `README.md` under Execution and changes
- Optional learner questions/reflections → chapter `NOTES.md`, only when reported
- Session record → `study/logs/YYYY-MM-DD.md`
- Exact resume state / durable project decisions → `MEMORY.md`
- Current work and completion criteria → `TASK.md`

## Completion protocol

A chapter is complete only when all applicable items are satisfied:

- Reading completed.
- Core concepts summarized in original words.
- Relevant listings/examples executed.
- Errors or deviations documented.
- Applicable experiment/project completed or explicitly marked not applicable. Extra written exercises and teach-back answers are optional.
- Chapter recap written.
- Progress table updated.

## Assistance style

When helping with a section:

1. State the concept in simple language.
2. Explain why it matters.
3. Walk through code line by line when useful.
4. Inspect shapes, tensors, metrics, or outputs rather than hand-waving.
5. Connect back to prior chapters.
6. Offer brief understanding checks when useful, without making them extra completion gates. Do not invent learner answers or reflections.
7. End with the exact next page/section to resume from.

## Repository simplicity

Follow read → run → apply. Keep one current artifact per purpose. Create notes, experiment folders, or additional records only when real content exists. Do not recreate removed exercise templates, duplicate run logs, JSON result exports, or snapshot notebooks. Notebook outputs and the chapter overview hold execution evidence; study/manifest.json holds provenance; THIRD_PARTY_NOTICES.md holds the upstream license.
