# Neural Network Model and Loss Function

## 1. Model Overview

Logistic regression has some great advantages, like mathematical simplicity and statistical interpretability (also, a linear separation is often enough if the data dimensionality is higher). However, sometimes one might want a more complex decision boundary. Therefore, it's time to write a neural network from scratch. The new model is `ŷ = |σ(σ(Xθ₁)θ₂)|`, which will be used for classification in 2D and has a sigmoid activation function. The parameter matrices are defined as `θ₁ ∈ ℝ³⁰ⁿ` and `θ₂ ∈ ℝⁿˣ¹`, where `n` is the number of internal linear decision boundaries that will be combined at the end. You can find these linear decision boundaries in the columns of `θ₁`, each being a logistic regression like in the last exercise. The input dimensionality for the first linear transform is 3 to give room for 2D points and a pseudo input (bias/intercept). The `n` number of decision boundaries will project the data into an `n` dimensional space, where `θ₂` will define one decision boundary for the binary output.

Your old code for optimization is going to work still, but might need more iterations and some tuning of the standard deviation of the noise. The problem is a bit more complex, but we can rely on modern computers for this one and set the max iterations to 10000.

## 2. Parameter Vector

The parameters of a model are often split up into several matrices, scalars, and vectors. However, for easy access and abstraction, the parameters are typically treated as a vector. Your `θ₁` and `θ₂` need to be flattened and concatenated for access, and the reverse will need to be done for setting parameter values. You should look into getters and setters for Python to do this. Code suggestion:

```python
@property
def theta(self):
    return np.concatenate([self._theta1.ravel(), self._theta2.ravel()])

@theta._setter
def theta(self, values):
    self._theta1 = ...
    self._theta2 = ...
