# Notes - Chapter 1: What is deep learning?

Source: [Official Chapter 1](https://deeplearningwithpython.io/chapters/chapter01_what-is-deep-learning/), by Francois Chollet and Matthew Watson.

Reading and understanding confirmed by the learner on 2026-10-13. NOTES.md is the main artifact for this conceptual chapter. Code execution, experiments, and equation practice are not applicable.

## Section notes and figures

The headings follow the online chapter. Summaries are original study notes. Figures 1.1-1.9 are displayed from the official website; no image copies are stored in this repository. Viewing them requires internet access. Figure descriptions below are study labels.

### Artificial intelligence, machine learning, and deep learning

AI contains machine learning, which contains deep learning.

![Figure 1.1 - Relationship between the three fields](https://deeplearningwithpython.io/images/ch01/ai-ml-dl.07201556.png)

### Artificial intelligence

AI also includes approaches with manually written rules.

### Machine learning

Training finds rules from examples rather than requiring a programmer to supply every rule.

![Figure 1.2 - Programming compared with learning](https://deeplearningwithpython.io/images/ch01/a-new-programming-paradigm.e8d1a1c2.png)

### Learning rules and representations from data

Changing how data is represented can simplify classification.

![Figure 1.3 - Points before transformation](https://deeplearningwithpython.io/images/ch01/example_data_points.28a84f5a.png)

![Figure 1.4 - Points after a coordinate change](https://deeplearningwithpython.io/images/ch01/learning_representations.97fa3c4b.png)

### The deep in deep learning

Depth refers to successive representation layers. Neural networks are mathematical models, not faithful brain simulations.

![Figure 1.5 - Layers processing a digit](https://deeplearningwithpython.io/images/ch01/a_deep_network.32f0eedf.png)

![Figure 1.6 - Representations along the network](https://deeplearningwithpython.io/images/ch01/mnist_representations.fdb30a2d.png)

### Understanding how deep learning works, in three figures

Parameters determine predictions; loss measures error; feedback guides parameter updates.

![Figure 1.7 - Parameters govern transformations](https://deeplearningwithpython.io/images/ch01/deep-learning-in-3-figures-1.55e5a910.png)

![Figure 1.8 - Predictions compared with targets](https://deeplearningwithpython.io/images/ch01/deep-learning-in-3-figures-2.bb3cebc2.png)

![Figure 1.9 - Feedback changes parameters](https://deeplearningwithpython.io/images/ch01/deep-learning-in-3-figures-3.de178fa4.png)

### What makes deep learning different

Learned features, scalable computation, and reusable models explain its usefulness.

### The age of generative AI

Self-supervised training derives targets from the data itself.

### What deep learning has achieved so far

Applications include recognition, translation, and content generation.

### Beware of the short-term hype

Judge demonstrated abilities separately from predictions.

### Summer can turn to winter

Overpromising can undermine investment when expectations fail.

### The promise of AI

Useful long-term applications warrant continued study.

## What stood out to me

I had encountered this idea before, so it was not a major surprise: neural networks are not faithful adaptations of how the human brain works. Some historical inspiration came from biology, but that does not establish equivalent learning mechanisms.

## Questions and practice

The learner reports that everything in Chapter 1 is clear. No unresolved questions remain. The three-question recall check below was completed accurately. Book-following runnable code, notebooks, experiments, and equation exercises are not applicable; no code execution is claimed.

## Chapter recap

Learner recap recorded on 2026-10-13:

1. **AI, machine learning, and deep learning:** AI is the broad field of making machines perform tasks that require intelligence. Machine learning is a part of AI that learns patterns from data. Deep learning is a part of machine learning that uses neural networks with many layers.
2. **What a neural network learns:** It learns values for its **weights and biases** so that it can map inputs to useful outputs - for example, images to predicted categories.
3. **Weights, loss, and optimization:** Weights influence the network predictions. The **loss** measures how far those predictions are from the desired answers. An **optimizer** adjusts the weights and biases to reduce the loss.

Understanding check: all three explanations are accurate. Layered representations are produced by the learned weights and biases. Training aims to reduce loss; performance on unseen data must still be checked.
