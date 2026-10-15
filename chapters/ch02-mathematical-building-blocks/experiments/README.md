# Chapter 2 experiment: interactive foundations lab

[Open the lesson notebook](chapter02_interactive_foundations_lab.ipynb)

This is an original, student-facing lesson built within Chapter 2's scope. It uses MNIST where images and labels matter, and small invented arrays where the numbers need to be visible. It is separate from the book-following notebook; it does not replace the reading.

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

Saved evidence: the executed notebook and [machine-readable run summary](../outputs/ch02_lesson_execution.json). The development checks do not complete the learner's teach-back. The learner still needs to run this new experiment in Colab, manipulate controls, and explain the observations.

**Resume:** Lesson 0, then run the notebook in order. Complete Lesson 8 before the Chapter 2 recap/completion review. Next reading afterward: beginning of Chapter 3.
