# Chapter 2 notes: the mathematical building blocks of neural networks

These are original study summaries prepared with assistance from the chapter and the executed notebooks. They are not quotations or a claim that the learner wrote every explanation.

[Chapter overview and notebooks](README.md) · [Official chapter](https://deeplearningwithpython.io/chapters/chapter02_mathematical-building-blocks/)

## 1. A first look at a neural network

The task is to recognize handwritten digits in MNIST. Each sample is a 28 × 28 grayscale image, and its label is an integer from 0 to 9. The label is stored separately from the pixels. During training, the model uses examples and their labels to adjust its parameters; during prediction, it receives images and produces class scores.

A dense layer combines input values using weights, adds a bias, and optionally applies an activation. A hidden ReLU layer builds a representation of the image. The output layer has ten positions, one per digit. Softmax converts scores into positive probability scores whose sum is one. The index of the largest score is the predicted class; a high score does not guarantee a correct answer.

Training and testing have different jobs. Training examples influence the parameters. Separate test examples measure performance on data not used for those updates. Accuracy is the fraction of correct top predictions; loss measures how the predicted distribution agrees with the targets.

## 2. Data representations for neural networks

A tensor is an organized collection of numbers. Three attributes matter:

| Attribute | Meaning | MNIST batch example |
|---|---|---|
| Rank (`ndim`) | Number of axes | A batch of images has rank 3 |
| Shape | Length of each axis | `(8, 28, 28)` means samples, rows, columns |
| Dtype | How numbers are stored | Raw pixels are `uint8`; normalized inputs use `float32` |

A scalar has shape `()` and rank 0. A vector has one axis, such as `(784,)`. A matrix has two axes. Rank is not the number of values: a vector containing 784 pixels still has rank 1.

Indexing one sample, `images[0]`, produces shape `(28, 28)`. Taking a one-sample slice, `images[0:1]`, preserves the batch axis and produces `(1, 28, 28)`. Slice stop positions are excluded: rows `4:12` contain eight rows.

Flattening a batch from `(8, 28, 28)` to `(8, 784)` keeps every pixel but combines the spatial axes. Converting to `float32` and dividing by 255 scales values into `[0, 1]`; it does not change the shape. A raw brightness of 128 becomes approximately 0.502.

Reshape and transpose are different. Reshape reorganizes values while preserving their flattened order. Transpose exchanges axes. Reshaping `[[0, 1, 2], [3, 4, 5]]` to `(3, 2)` gives `[[0, 1], [2, 3], [4, 5]]`; transposing gives `[[0, 3], [1, 4], [2, 5]]`.

## 3. The gears: tensor operations

Element-wise operations act on corresponding positions. Multiplying an array by itself squares each value and keeps its shape. Matrix multiplication combines features through sums of products; it is a different operation.

For a dense layer:

```text
output = ReLU(inputs @ weights + bias)
(batch, input_features) @ (input_features, output_features)
    -> (batch, output_features)
```

The inner dimensions must agree. A bias of shape `(output_features,)` is broadcast across the batch: each sample receives the same bias values. Broadcasting follows shape compatibility rules; it does not make arbitrary incompatible arrays fit.

For an invented sample `[1, 2, 3]`, weight column `[1, 0, 1]`, and bias `-3`, the weighted sum is `1*1 + 2*0 + 3*1 - 3 = 1`. ReLU keeps positive values and replaces negative values with zero.

These operations also have a geometric interpretation. Matrix multiplication can rotate or scale point coordinates; adding a bias translates them. ReLU changes negative coordinates to zero, introducing a nonlinear transformation. Successive layers can therefore change how data is represented.

## 4. The engine: gradient-based optimization

A derivative describes the local rate of change of a function. A gradient collects the loss derivatives for the adjustable entries of a parameter tensor. Its shape matches the parameter's shape.

Gradient descent updates parameters using:

```text
parameter = parameter - learning_rate * gradient
```

A positive gradient suggests decreasing the parameter locally; a negative gradient suggests increasing it. The learning rate controls the step size. A useful local direction does not guarantee that a very large step will improve the loss.

For the synthetic loss `L(w) = (w - 2)^2`, the derivative is `2*(w - 2)`. At `w=-1`, loss is 9 and the gradient is -6. With learning rate 0.1, the new weight is `-1 - 0.1*(-6) = -0.4`, and loss falls to 5.76. At learning rate 1.1, the weight instead becomes 5.6 and loss rises to 12.96. These particular rates describe this toy curve, not a universal rule for neural networks.

Backpropagation applies the chain rule through recorded operations to work out each parameter's effect on the loss. Automatic differentiation calculates gradients; it does not update parameters on its own. In the experiment, `GradientTape` computes them and `assign_sub` applies the update.

For `prediction = w*x + b` and squared loss, the weight gradient is `2*(prediction-target)*x`; the bias gradient is `2*(prediction-target)`. If `x=0`, this sample's prediction does not depend on the weight, so its weight gradient is zero even though its bias gradient may be nonzero.

## 5. Looking back: one complete training loop

The experiment makes each stage visible:

1. Select a mini-batch and flatten/scale its images.
2. Run the forward pass to obtain output scores.
3. Compute a scalar mean loss against the integer labels.
4. Differentiate that loss with respect to every parameter.
5. Subtract learning rate × gradient from the parameters.
6. Repeat across batches and epochs, then evaluate on held-out images.

The experiment's network maps `784 -> 32 ReLU -> 10` and has 25,450 parameters. It uses 6,000 training images, batches of 128, and three default epochs. There are 47 updates per epoch: 46 batches of 128 and a final batch of 112. An epoch is one pass through the training subset; an update is one parameter adjustment.

The loss function receives raw scores and computes sparse softmax cross-entropy stably. Explicit softmax is used when displaying predictions. Passing already-softmaxed probabilities to a function expecting raw scores would change the computation.

A loss returned by one training step was calculated before that step's update. To measure the updated network, run another forward pass. Likewise, retraining makes old prediction plots stale: rerun evaluation before interpreting them. The experiment checks this relationship before allowing prediction browsing or a run summary.

Actual environments, results, and deviations are recorded once in the [chapter overview](README.md#execution-and-changes); the executed notebooks retain their outputs.

## Chapter recap

Pixels are numbers organized into tensors. Layers transform those tensors using weights, biases, and activations. A loss turns prediction quality into a scalar feedback signal. Gradients describe how parameters affect that signal, and an update rule changes the parameters. Mini-batches make those updates repeatedly over the training data. Held-out evaluation checks the resulting network on examples that did not drive its updates.

This supplies the mechanics behind Chapter 1's weights–loss–optimization explanation. Chapter 3 develops the framework tools used to express these mechanics.

**Next reading:** Beginning of Chapter 3 — Introduction to TensorFlow, PyTorch, JAX, and Keras.
