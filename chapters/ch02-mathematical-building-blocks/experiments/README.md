# Chapter 2 experiment: interactive foundations lab

[Open the lesson notebook](chapter02_interactive_foundations_lab.ipynb)

This is an original, student-facing lesson built within Chapter 2's scope. It uses MNIST where images and labels matter, and small invented arrays where the numbers need to be visible. It is separate from the book-following notebook; it does not replace the reading.

## What makes this a lesson

The revised notebook starts with a concrete digit-recognition problem and explains the vocabulary before using it. It assumes basic Python, but no calculus or prior neural-network training. Learners encounter a hand-worked example before a larger computation, a prediction prompt before a control, and an explanation of what the plot/output means afterward.

The controls have specific experiments: change only weight, then only bias; compare predetermined learning rates; follow point colors during rotation; inspect a wrong prediction. Twelve short checks include optional hints and explanations; a final transfer task checks a fresh example. The large final implementation is split into six small code blocks, with parameter-count calculations, shape traces, and a line-by-line update explanation. A fresh transfer problem tests whether learners can use the ideas without copying the displayed example.

These changes address the gap between running code and understanding it. They do not prove that every visitor will understand: ask a new learner to predict a shape, calculate an update, and explain a prediction. Where they get stuck is evidence for the next teaching revision.

## Teaching sequence

1. Inspect real MNIST images and distinguish samples from labels.
2. Explore rank, shape, dtype, batches, slices, flattening, and transpose versus reshape.
3. Work through a tiny matrix product, broadcast a bias, and apply ReLU.
4. Manipulate weight/bias and geometric transformation controls.
5. Explore a one-weight loss curve, compare derivatives, and change the learning rate to see convergence and overshooting.
6. Trace the chain rule through one invented neuron and compare it with automatic differentiation.
7. Train a small MNIST network with an explicit mini-batch SGD loop, inspect gradient shapes, evaluate held-out images, and browse correct/incorrect predictions.
8. Complete the teach-back and record one controlled variation.

Every interactive figure also has a normal default call, so the executed notebook contains readable examples even when a viewer cannot render live widgets. Run the cells to activate controls. Changing the training sliders does not train automatically: rerun the marked training cell afterward. Changing training settings also requires rerunning evaluation before interpreting predictions.

## Colab use

Upload the `.ipynb` through **File → Upload notebook** in Colab. Use a fresh Python session; CPU is sufficient for this small demonstration. A GPU is optional. Run cells in order. The first dataset load needs network access; the standard Keras loader caches MNIST.

The notebook enables Colab's widget manager when running there. Package installation is not automatic. If widgets are unavailable, the notebook explains the optional installation step; record any installation or API fix in `../NOTEBOOK_CHANGES.md`. Local development checked Python callbacks and widget trait updates, but actual slider dragging and rendering in the Colab browser have not been verified.

## Deliberate choices and boundaries

- TensorFlow is explicit because the experiment teaches `GradientTape`, variables, and the update assignment. `tf.keras.datasets.mnist` loads data. No Keras-3-only API is required, and no dependency downgrade is requested for Colab.
- The one-weight quadratic loss is synthetic and intentionally easy to inspect. Its special learning-rate behavior does not generalize to arbitrary neural networks.
- The digit network uses 6,000 training samples, 1,000 held-out samples, 32 hidden units, and three default epochs to keep the lesson short. These are original experiment settings, not patches to the official examples.
- Raw output scores feed a numerically stable sparse softmax cross-entropy operation. Explicit softmax is used when viewing probabilities. The loop uses plain SGD, not an unexplained optimizer implementation.
- Initial weights use fixed stateless seeds; each training run resets the shuffle generator. Exact metrics may vary by device/version.
- No CNNs, augmentation, dropout, model-search tools, or later-chapter techniques are introduced.

## Executed development evidence — 2026-10-15

The entire notebook ran on local Windows CPU using Python 3.10.0, TensorFlow/Keras 2.11.0, NumPy 1.24.1, Matplotlib 3.7.0, and ipywidgets 8.1.5. No packages were installed or changed for this run. This local environment is older than the learner's saved Colab environment; successful local execution is not a claim of a tested Colab run.

- Initial training loss: **2.309777**.
- Final training loss: **0.538247**, after three epochs at learning rate **0.1**, batch size **128**.
- Held-out loss: **0.634320**; accuracy: **0.821 (82.1%)**, on 1,000 images.
- Default numerical/shape assertions passed, including hand-computed matrix outputs, gradient comparisons, gradient shapes, and probability row sums.
- Alternate controls were exercised, including a batch of one, edge crop, negative weight, geometric transform plus ReLU, zero gradient, diverging toy updates, and a misclassified image. Actual widget trait changes triggered their kernel callbacks.
- The local sandbox initially blocked Jupyter from securing its connection file. The run was retried with execution approval; notebook mathematics and package versions were unchanged. A Windows Jupyter event-loop warning required no lesson-code change.

Saved evidence: the executed notebook and [machine-readable run summary](../outputs/ch02_lesson_execution.json). The development checks do not complete the learner's teach-back. The learner subsequently reported completing the experiment and supplied its executed notebook. The written observations and recap remain to be recorded.

**Learner resume:** Record the Chapter 2 recap using Lesson 8. For a visitor’s first pass, start at the introduction and run lessons in order. To review the revised explanations, begin with Lesson 2’s worked shape example. Next reading after the Chapter 2 review: beginning of Chapter 3.

## Teaching revision and learner evidence — 2026-10-15

- Preserved the learner’s pre-revision executed notebook in `../outputs/ch02_learner_lab_before_teaching_revision.ipynb`, with its saved summary separately recorded. The saved training cell ran after its evaluation/summary cells, so those old metrics are not attributed to the final saved training state.
- Revised the main notebook to 67 cells: 47 explanation/activity cells and 20 code cells. Added worked arithmetic, guided slider settings, plot interpretation, twelve knowledge checks plus a transfer task, a worked teach-back, and an unseen transfer problem.
- Added training/evaluation run records. Retraining invalidates evaluation; the browser and summary require evaluation from the current training run. Existing old plots on the page are still static images from their original runs; rerun evaluation to refresh them.
- Re-executed all 20 code cells locally in sequence. Worked learning-rate tables, softmax values, transfer-task arithmetic, parameter count (25,450), batch count (47 per epoch), callback behavior, and stale-evaluation guards passed targeted checks.
- Default metrics remained training loss 2.309777 → 0.538247 and held-out accuracy 0.821. Same local CPU environment and no package changes. Evidence: `../outputs/ch02_lesson_revision_execution.json`.
- The learner’s previous Colab run is recorded separately from this development run. The revised explanations and browser interactions have not yet been independently evaluated with a new visitor or in Colab.
