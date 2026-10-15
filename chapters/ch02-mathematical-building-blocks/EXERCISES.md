# Exercises - Chapter 2: The mathematical building blocks of neural networks

## Book-following practice

Reading and notebook execution reported complete on 2026-10-15. Saved execution evidence is described in RUN_LOG.md. Learner modifications expose rank/shape and slice shapes.

## Independent teaching experiment

[Open the interactive foundations lab](experiments/chapter02_interactive_foundations_lab.ipynb). Status: experiment completed (learner reported on 2026-10-15); saved executed notebook inspected. Written observations and Chapter 2 recap have not yet been recorded. The lesson has since been revised to explain concepts more explicitly for visitors.

1. Run the notebook in order and use the image, batch, crop, weight, bias, geometry, and learning-rate controls.
2. Predict one array shape, then verify it. Calculate one output of the tiny dense layer by hand.
3. Record the toy loss trajectories for learning rates 0.05, 0.5, and 1.1. Explain the direction and size of updates.
4. Explain the chain-rule gradients for the invented neuron and inspect gradient shapes in the MNIST model.
5. Run the small MNIST loop, inspect one correct and one incorrect prediction if available, and save the actual Colab environment/metrics.
6. Complete the teach-back in Lesson 8 and write a short Chapter 2 recap in NOTES.md.

## Learner observations (fill after running)

- My predicted and observed tensor shapes:
- My hand-calculated layer output:
- Learning-rate observations:
- How one batch changes the parameters:
- One prediction I can explain:
- What remains unclear:

Resume: record your Chapter 2 recap using Lesson 8’s teach-back prompts. To review the new visitor explanations, start at Lesson 2’s worked rank/shape example; your previously completed experiment remains recorded. Next reading after the Chapter 2 review: beginning of Chapter 3.

## Teaching-quality review — 2026-10-15

The learner completed the lab but found that a visitor could run the demonstrations without understanding them. The revision adds a problem-first introduction, terms explained before use, hand calculations, controlled slider activities, interpretation after each plot, common misconceptions, and twelve short checks with hints/explanations plus a transfer task. The final MNIST implementation is split into six smaller blocks.

An appropriate learning check is explanation on a fresh example, not merely a successful run: complete the new one-neuron transfer task in Lesson 8 and explain the same stages in the real MNIST batch update. Answers in the notebook are teaching material, not the learner’s recorded responses.
