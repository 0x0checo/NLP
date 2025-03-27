# Exercise: Implementing Polynomial Linear Regression with Iterative Optimization

Lecture 2 used linear regression as a pedagogical tool for showing the fundamentals of mathematical optimization. Most, but not all, models in machine learning have parameters that we need to tune. For this exercise, you will continue to develop your class for 2D linear regression. The model will be updated to an n-order polynomial as the model. For example, a third-order model would be defined as (see the illustration to the right). Furthermore, you will also do the tuning of the parameters yourself. Though one can find the best parameters easily using analytical methods, this is not the solution you should use here. 

### Objectives

1. **Parameter vector**: The size of the parameter vector should depend on an argument `n_order` given when instantiating your class.
   
2. **Improvement step**: Implement a method `_fit(X, y)` that performs one iteration of the optimization. The data is constant, so the residual only changes with changes in the parameter vector. Change the parameter vector slightly by adding random noise, and see if the residual improves. If the residual is lower than before, keep the new parameter values. If not, discard them and use the old ones. Note that this does not guarantee improvement with every call of the `_fit` method.

3. **Optimization loop**: Implement a method `fit(X, y)` that runs the improvement step multiple times. This should stop after `n_max_iter` number of iterations. You should also store the loss values for each iteration in a list called `loss_`.

4. **Prediction**: Your model should be extended to implement n-th order polynomials. The model then becomes a polynomial of the form:


This can be implemented, for example, using a for loop.

### Instructions

To develop and test your code, you should generate a toy data set for simple linear regression using NumPy (or copy this part from the test code). You then write a class with linear regression following scikit-learn's API as:

- The `fit` method adapts your parameters `self._theta` to the data set using iterative optimization.
- The method of optimization is up to you, but using a loop where you add some random noise is probably the easiest to implement.

Note that this is primarily an exercise in iterative optimization, not in linear regression. You should **not use an external library for the optimization** in the code you hand in, but feel free to use such tools when testing your implementation.

