# Logistic Regression for Binary Classification

The next evolutionary step between regression and neural networks is a simplified logistic regression. This is a simple linear regression where, in order to get classes as predictions, the output is passed through an activation function. In this exercise, you should use your code from the last exercise and add functionality to create a model that can do binary classification on 2D data (2D input, {0,1} output).

The model will look like this:

### Modifications to Implement:

1. **Sigmoid function**:  
   A method `_sigmoid(x)` should be implemented as an internal helper method for the activation function.

2. **Soft predictions**:  
   We want to both train the model and make crisp predictions. The `predict` function from before could do both, but this is no longer the case. We need a “soft” prediction, a function `_soft_predict`, that can tell us how close we are to the desired result. Otherwise, it will be hard to define any meaningful loss function.

3. **Parameter vector**:  
   The parameter vector can be initialized as before, but the number of parameters is different from a regression model.

4. **Prediction**:  
   The prediction function for logistic regression takes the data `X` of shape `(n_samples, n_features)`, where `n_features=2`, and predicts crisp classifications as a flat vector. With a pseudo input, this would look like (the bars symbolize the absolute value in this case). 

5. **Score**:  
   There are many possible metrics to choose from for measuring performance for any model. However, for a classification task, one of the simplest, yet still very informative, is accuracy. The `score` function should output the relative number of correct classifications as a value between 0 and 1.

6. **Loss function**:  
   Square loss is not a great loss function, but we can keep it for now.
