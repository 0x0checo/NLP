import numpy as np

class LinearRegression:
  def __init__(self, n_order = 1, n_max_iter = 5000):
      self.n_order = n_order
      self.n_max_iter = n_max_iter
      self._theta = np.random.randn(n_order + 1)
      self.loss_ = []

  def predict(self, X):
      X_poly = np.hstack([np.ones((X.shape[0], 1))] + [X.reshape(-1, 1)**i for i in range(1, self.n_order+1)])
      return X_poly.dot(self._theta)

  def score(self, X, y):
      predictions = self.predict(X)
      return np.sum((y - predictions) ** 2)

  def _fit(self, X, y):
      old_theta = self._theta.copy()
      old_loss = self.score(X, y)

      noise = np.random.normal(scale = 0.1, size = self._theta.shape)
      self._theta += noise

      new_loss = self.score(X, y)
      if new_loss < old_loss:
          self.loss_.append(new_loss)
      else:
          self._thata = old_theta

  def fit(self, X, y):
      for i in range(n_max_iter):
          self._fit(X, y)
      return self
    
          
