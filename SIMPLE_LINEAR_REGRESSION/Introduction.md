As the first exercise in the course, this is intended as a warm-up exercise. You will implement a python class for a first order simple linear regression model. The model is defined as:

$$
\hat{y}_i = \theta_1 \cdot x_i + \theta_0
$$

predicting a value (\hat{y}_i\) for each input data point (x_i\), given the parameters (\theta_0\) as intercept and (\theta_1\) as the slope. This is the same model as in the maths course from last semester. Since we will be using NumPy and scikit-learn a lot throughout the course, you are expected to follow some conventions from the scikit-learn API. This will be enforced using test-driven development, where you are given a set of unit tests that must run without error for you to pass the exercise.

The code for training the model is given, but the predictions and finding the residual must be implemented. A base to start from can be found in the course repo. You will have to implement the following functionality (this is also a suggestion for implementation order):

- **Parameter vector**: In the maths course, a 2D regression model was defined as:

$$
y = \beta_1 \cdot x + \beta_0
$$

i.e., one input and one output. It's the same number of parameters here, but the parameters are treated as a vector, which is usually called theta (\(\theta\)).

- **Prediction**: This should give a prediction for each line in \(X\). Even for one-dimensional input data, the shape of the input \(X\) should be (n, 1), while the shape of the output \(y\) should be (n,). This is implemented in the `predict` method. You can start plotting after this step.

- **Loss / Residual**: The residual should be used as the metric of "badness", often called loss, of your model. The residual is the sum of the squared errors as:

$$
\sum \left( y_i - (\theta_1 \cdot x_i + \theta_0) \right)^2
$$

This is implemented in the `score` method.

To develop and test your code, you should generate a toy data set for simple linear regression using NumPy (this can be copied from the test code). Don't do everything at the same time. Instead, focus on one test at a time, running tests frequently as you move through the exercise.
