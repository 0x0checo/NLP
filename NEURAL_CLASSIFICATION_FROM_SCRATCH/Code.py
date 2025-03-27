import numpy as np

class FeedForwardNeuralNetwork:
    def __init__(self, n_hidden=3):
        """Initialize neural network with n hidden units"""
        # First layer: 3×n matrix (3 for 2D input + bias)
        self._theta1 = np.random.randn(3, n_hidden) * 0.01
        # Second layer: (n+1)×1 matrix (added +1 for bias)
        self._theta2 = np.random.randn(n_hidden + 1, 1) * 0.01
        self.loss = []
        self.n_max_iterations = 10000
    def _sigmoid(self, x):
        """Compute sigmoid function σ(x) = 1/(1 + e^(-x))"""
        return 1 / (1 + np.exp(-np.clip(x, -100, 100)))
    @property
    def theta_(self):
        """Flatten and concatenate parameters for optimization"""
        return np.concatenate([self._theta1.ravel(), self._theta2.ravel()])
    @theta_.setter
    def theta_(self, values):
        """Reshape flat parameter vector into matrices"""
        n_hidden = self._theta1.shape[1]
        split_idx = 3 * n_hidden
        self._theta1 = values[:split_idx].reshape(3, n_hidden)
        self._theta2 = values[split_idx:].reshape(n_hidden + 1, 1)
    def _soft_predict(self, X):
        """Make soft predictions (probabilities)"""
        if X.ndim == 1:
            X = X.reshape(1, -1)
        # Add bias term
        X_with_bias = np.column_stack([np.ones(len(X)), X])
        # Forward pass
        hidden_layer = self._sigmoid(X_with_bias @ self._theta1)
        hidden_with_bias = np.column_stack([np.ones(len(hidden_layer)),
    hidden_layer])
        output = self._sigmoid(hidden_with_bias @ self._theta2)

        return output.ravel()
    def predict(self, X):
        """Make crisp predictions (0 or 1)"""
        probabilities = self._soft_predict(X)
        predictions = (probabilities > 0.5).astype(int)
        return predictions[0] if len(predictions) == 1 else predictions
    def _loss(self, X, y):
        """Compute squared loss"""
        predictions = self._soft_predict(X)
        return np.mean((predictions - y) ** 2)
    def score(self, X, y):
        """Compute accuracy score"""
        predictions = self.predict(X)
        return np.mean(predictions == y)
    def _fit(self, X, y, learning_rate=0.1):
        """Single iteration of gradient descent"""
        if X.ndim == 1:
            X = X.reshape(1, -1)
        y = y.reshape(-1, 1) # Ensure y is 2D
        # Forward pass
        X_with_bias = np.column_stack([np.ones(len(X)), X])
        hidden = self._sigmoid(X_with_bias @ self._theta1)
        hidden_with_bias = np.column_stack([np.ones(len(hidden)), hidden])
        output = self._sigmoid(hidden_with_bias @ self._theta2)
        # Backward pass with cross-entropy gradient
        delta2 = output - y # Simplified gradient for cross-entropy
        delta1 = hidden * (1 - hidden) * (delta2 @ self._theta2[1:].T)
        # Compute gradients
        grad_theta2 = hidden_with_bias.T @ delta2
        grad_theta1 = X_with_bias.T @ delta1
        # Update parameters
        self._theta2 -= learning_rate * grad_theta2
        self._theta1 -= learning_rate * grad_theta1
        return self._loss(X, y)
    def fit(self, X, y, learning_rate=0.5): # Adjusted learning rate
        """Train the model using gradient descent"""
        # Reset parameters for consistent training
        n_hidden = self._theta1.shape[1]
        self._theta1 = np.random.randn(3, n_hidden) * 0.01
        self._theta2 = np.random.randn(n_hidden + 1, 1) * 0.01
        self.loss = []
        for _ in range(self.n_max_iterations):
            current_loss = self._fit(X, y, learning_rate)
            self.loss.append(current_loss)
            if current_loss < 1e-6:
                break
        return self

        
