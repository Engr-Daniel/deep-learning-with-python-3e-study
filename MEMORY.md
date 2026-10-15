# MEMORY.md

## Durable study decisions

- Book: **Deep Learning with Python, Third Edition**.
- Scope: complete the **entire book**, not selected chapters.
- Order: Chapter 1 through Chapter 20.
- Daily commitment: **at least 5 pages per study day**.
- Practical commitment: execute and understand the code, not merely read it.
- Learning record: maintain notes, code, outputs, questions, exercises, and progress in this repository.
- Copyright discipline: do not reproduce book text; write original summaries and code notes.

## Assistance preference

Think alongside the learner and proactively suggest useful learning checks, explanations, and workspace improvements. Use judgment rather than applying templates mechanically.

## Chapter workspace decision

Follow the official online chapter structure. Create only artifacts needed by the chapter. Chapter 1 uses NOTES.md as its main output, with section notes, external figure references, reflection, and recap. Use notebooks for the Colab examples. Empty code/ placeholders have been removed from all chapters; create standalone script folders only for a specific task. RUN_LOG.md applies only when there is runnable work.

## Notebook and runtime decision

Use Google Colab for chapter code. Official third-edition notebooks come from fchollet/deep-learning-with-python-notebooks, pinned to fbf7f1bf2041093c4081e72544ec5905ace9dc8f. There are 16 study copies (Chapters 2-5 and 7-18); Chapters 1, 6, 19, and 20 have no published upstream notebooks. Preserve original code, document every environment change in NOTEBOOK_CHANGES.md, and record actual runs in RUN_LOG.md. Prepared copies are not evidence of execution. Chapter 2 now has a learner-saved executed copy and declared practice edits; see its RUN_LOG.md. See study/NOTEBOOKS.md.

## Teaching experiment preference

Create original lesson notebooks within the current chapter scope. Prefer real datasets when useful and tiny synthetic examples when they expose the concept. Use sliders for weights, learning rate, and other visual explanations; require predictions, observations, and teach-back.

## Framework decision

Do not prematurely standardize everything to one backend. The book explicitly covers TensorFlow, PyTorch, JAX, and Keras. Use the backend appropriate to the section and document it. For Keras sections, the backend may be selected explicitly when needed.

## Current resume state

- Chapter: **2 — The mathematical building blocks of neural networks**
- Progress: **Chapter 1 complete; Chapter 2 reading/book notebook reported complete; original teaching lab built and CPU-executed; learner experiment and recap pending**
- Resume point: **Chapter 2 experiment: Lesson 0 of experiments/chapter02_interactive_foundations_lab.ipynb, then teach-back and recap**
- Last updated: **2026-10-15**

## Update policy

Keep this file short. Only store facts needed to resume the project correctly after a long break. Session detail belongs in `study/logs/` and `study/PROGRESS.md`.
