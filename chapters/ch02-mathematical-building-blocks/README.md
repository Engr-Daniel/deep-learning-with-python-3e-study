# Chapter 2: The mathematical building blocks of neural networks

**Complete:** reading, book notebook, and applied experiment reported complete by the learner on 2026-10-15. Original notes and a chapter recap are now recorded. Additional written exercises are optional.

| Step | Material | Run |
|---|---|---|
| Read | [Official chapter](https://deeplearningwithpython.io/chapters/chapter02_mathematical-building-blocks/) | — |
| Review | [Concept notes and recap](NOTES.md) | — |
| Follow the book | [Chapter notebook](notebooks/chapter02_mathematical_building_blocks.ipynb) | [Open in Colab](https://colab.research.google.com/github/Engr-Daniel/deep-learning-with-python-3e-study/blob/main/chapters/ch02-mathematical-building-blocks/notebooks/chapter02_mathematical_building_blocks.ipynb) |
| Apply | [Interactive MNIST foundations lab](experiments/chapter02_interactive_foundations_lab.ipynb) | [Open in Colab](https://colab.research.google.com/github/Engr-Daniel/deep-learning-with-python-3e-study/blob/main/chapters/ch02-mathematical-building-blocks/experiments/chapter02_interactive_foundations_lab.ipynb) |

## The experiment

The lab explains tensors, batches, slicing, matrix multiplication, bias broadcasting, ReLU, gradients, the chain rule, and mini-batch SGD. Real MNIST images support the digit task; small invented arrays make the arithmetic visible.

Worked examples come before larger code blocks. Guided sliders manipulate images, weights, biases, geometry, and learning rate. Twelve optional checks include hints and explanations; a transfer task offers extra practice. The final network is split into six small implementation blocks. Visitors need basic Python, but no prior calculus or neural-network training.

Start at the notebook introduction and run in order. A CPU runtime is sufficient for this small model. Changing the training sliders selects settings; rerun training and then evaluation to update predictions. A runtime check prevents summaries or prediction browsing from using an older evaluation after retraining. Read [Colab guidance](../../environment/README.md) for setup and saving your run.

## Execution and changes

| Evidence | Environment | Observed result |
|---|---|---|
| Learner’s book notebook | Saved environment: Python 3.13.15, TensorFlow 2.21.0, Keras 3.15.1, NumPy 2.1.3; TensorFlow backend, Tesla T4 | Learner reports completion; 73 of 75 code cells have saved execution counts; no saved error outputs. Two TensorFlow-specific cells have no saved execution count, so their execution is unverified from the file alone. |
| Revised teaching lab, development run | Windows CPU; Python 3.10.0, TensorFlow/Keras 2.11.0, NumPy 1.24.1, Matplotlib 3.7.0, ipywidgets 8.1.5 | All 20 code cells executed without saved errors. Training loss 2.309777 → 0.538247; held-out loss 0.634320; accuracy 82.1%. |

The learner also reported completing the experiment in Colab. Their earlier saved training cell had been rerun after evaluation, so its old summary is not evidence for that final model state. The current notebook retains the verified revision’s complete outputs and environment record. Its browser interactions have not been independently tested in Colab after the revision.

The experiment deliberately uses 6,000 training and 1,000 held-out images, a `784 -> 32 ReLU -> 10` network, batch size 128, three epochs, seed 2026, and SGD learning rate 0.1 for a short CPU demonstration. Different versions/devices can give different results. These are experiment choices, not patches to the book notebook.

**Changes:** The learner renamed the book notebook and added rank/shape inspection. The teaching revision added worked examples, smaller code blocks, and a guard against stale evaluation. No package upgrades, downgrades, or backend substitutions were required for the local verification. Windows sandbox restrictions initially blocked Jupyter connection-file permissions; execution approval resolved that host issue without changing the mathematics. Numeric examples, parameter/batch counts, widget callbacks, and stale-evaluation checks passed.

[Official notebook source](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/fbf7f1bf2041093c4081e72544ec5905ace9dc8f/chapter02_mathematical-building-blocks.ipynb) · [Source registry](../../study/manifest.json) · [Upstream license](../../THIRD_PARTY_NOTICES.md)

**Next reading:** Beginning of [Chapter 3](../ch03-ml-frameworks/README.md) — Introduction to TensorFlow, PyTorch, JAX, and Keras.
