# Deep Learning with Python, Third Edition — Study and Experiments

Read the textbook, run its chapter notebook, and apply the concepts in a small experiment. This repository collects original notes, attributed companion code, and practical lessons for learners following the third edition in order.

**Start here:** [Chapter 1 notes](chapters/ch01-what-is-deep-learning/NOTES.md) or the [Chapter 2 interactive MNIST lab](chapters/ch02-mathematical-building-blocks/README.md). See [progress](study/PROGRESS.md) for completed work and the current resume point.

## How to use this repository

1. Read the official chapter. The study target is at least five pages on study days.
2. Open its book notebook in Colab using the chapter overview. Run sections alongside the text and inspect their outputs.
3. Use the original experiment to apply that chapter’s ideas. Experiments stay within the chapter’s scope and explain the steps for visitors.

Each chapter overview links its material and records actual execution results or environment changes. Notes contain the original concept summary and recap. Chapters without runnable code do not need notebook or experiment placeholders. Additional written exercises are optional; questions and personal reflections are recorded when the learner raises them.

**Using a fork:** In Colab, open the notebook from your fork through **File → Open notebook → GitHub**, then save your executed copy back to your fork. Links in this repository open this repository’s notebooks. Running in Colab does not automatically update files on GitHub. See [environment guidance](environment/README.md).

## Chapters

| Chapter | Study workspace | Textbook |
|---:|---|---|
| 01 | [What is deep learning?](chapters/ch01-what-is-deep-learning/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter01_what-is-deep-learning/) |
| 02 | [The mathematical building blocks of neural networks](chapters/ch02-mathematical-building-blocks/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter02_mathematical-building-blocks/) |
| 03 | [Introduction to TensorFlow, PyTorch, JAX, and Keras](chapters/ch03-ml-frameworks/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter03_introduction-to-ml-frameworks/) |
| 04 | [Classification and regression](chapters/ch04-classification-and-regression/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter04_classification-and-regression/) |
| 05 | [Fundamentals of machine learning](chapters/ch05-fundamentals-of-ml/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter05_fundamentals-of-ml/) |
| 06 | [The universal workflow of machine learning](chapters/ch06-universal-ml-workflow/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter06_universal-workflow-of-ml/) |
| 07 | [A deep dive on Keras](chapters/ch07-deep-dive-keras/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter07_deep-dive-keras/) |
| 08 | [Image classification](chapters/ch08-image-classification/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter08_image-classification/) |
| 09 | [ConvNet architecture patterns](chapters/ch09-convnet-architecture-patterns/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter09_convnet-architecture-patterns/) |
| 10 | [Interpreting what ConvNets learn](chapters/ch10-interpreting-convnets/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter10_interpreting-what-convnets-learn/) |
| 11 | [Image segmentation](chapters/ch11-image-segmentation/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter11_image-segmentation/) |
| 12 | [Object detection](chapters/ch12-object-detection/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter12_object-detection/) |
| 13 | [Timeseries forecasting](chapters/ch13-timeseries-forecasting/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter13_timeseries-forecasting/) |
| 14 | [Text classification](chapters/ch14-text-classification/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter14_text-classification/) |
| 15 | [Language models and the Transformer](chapters/ch15-language-models-transformer/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter15_language-models-and-the-transformer/) |
| 16 | [Text generation](chapters/ch16-text-generation/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter16_text-generation/) |
| 17 | [Image generation](chapters/ch17-image-generation/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter17_image-generation/) |
| 18 | [Best practices for the real world](chapters/ch18-real-world-best-practices/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter18_best-practices-for-the-real-world/) |
| 19 | [The future of AI](chapters/ch19-future-of-ai/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter19_future_of_ai/) |
| 20 | [Conclusions](chapters/ch20-conclusions/README.md) | [Read](https://deeplearningwithpython.io/chapters/chapter20_conclusion/) |

## Repository guide

- `chapters/`: one overview per chapter, studied notes, book notebooks, and applicable experiments.
- [Progress](study/PROGRESS.md): the single chapter-status table and next reading point.
- [Source manifest](study/manifest.json): chapter locations, notebook provenance, and integrity hashes.
- `study/logs/`: short session records linking to the actual artifacts.
- [Environment](environment/README.md): Colab workflow and optional local requirements.
- [Contributing](CONTRIBUTING.md): standards for corrections and forks.
- `AGENTS.md`, `MEMORY.md`, `TASK.md`: assistant rules, durable preferences, and the current task.

Run `python scripts/validate_repository.py` to check structure, local links, notebook integrity, and common text corruption. The check does not execute machine-learning code.

## Attribution

Read the book through its [official website](https://deeplearningwithpython.io/chapters/). Book prose is not redistributed here. Companion notebooks retain their [upstream MIT notice](THIRD_PARTY_NOTICES.md); original study work uses this repository’s [license](LICENSE).
