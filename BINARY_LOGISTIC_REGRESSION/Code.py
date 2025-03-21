import numpy as np

class SimplifiedLogisticRegression:
    def __init__(self, n_max_iter = 1000, lr = 0.01):
        self.n_max_iter = n_max_iter
        self.lr = lr
        self._theta = np.random.randn(3)
        self.loss = []

    def _sigmoid(self, X):
        return 1 / (1 + np.exp(-X))
      
    def _soft_predict(self, X):
        X_poly = np.hstack([np.ones(X.shape(0), 1), X])
        return _sigmoid(X_poly.dot(self._theta))

    def predict(self, X):
        return (self._soft_sigmoid(X) > 0.5).astype(int).flatten()        
      
    def _loss(self, X, y):
        predictions = self.predict(X)
        return -np.mean(y * np.log(predictions + 1e-15) + (1 - y) * np.log(1 - predictions + 1e-15))

    def _fit(self, X, y):
       X_poly = np.hstack([np.ones((X.shape[0], 1)), X])
       predictions = self._soft_predict(X)
       difference = predictions - y
       gradient = X_poly.T.dot(difference) / X.shape[0]
       self._theta -= self.lr * gradient

    def fit(self, X, y):
        for i in range(n_max_iter):
            self._fit(X, y)
            self.loss.append(self._loss(X, y))
        return self

    def score(self, X, y):
        predictions = self.predict(X)
        return np.mean(predictions == y)
      
      
