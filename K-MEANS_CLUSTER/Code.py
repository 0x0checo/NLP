import numpy as np

class NaiveKMeans:
    def __init__(self, n_clusters=3, n_max_iterations=100):
        self.n_clusters = n_clusters
        self.n_max_iterations = n_max_iterations
        self.centers = None
        self.attributions_ = None

    def _E（self, X):
        n_samples = X.shape[0]
        self.attributions_ = np.zeros(n_samples, dtype=int)

        for i in range(n_samples):
            distances = np.sqrt(np.sum((X[i[ - self.centers_) ** 2, axis=1))
            self.attributions_[i] = np.argmin(distances)
    def _M(self, X):
        n_features = X.shape[1]

        new_centers = np.zeros((self.n_clusters, n_features))

        for j in range(self.n_clusters):
            cluster_points = X[self.attributions_ == j]

            if len(cluster_points) == 0:
                idx = np.random.randint(0, X.shape[0])
                new_centers[j] = X[idx]
            else:
                new_centers[j] = np.mean(cluster_points, axis=0)

        self.centers_ = new_centers

    def fit(self, X):
        n_samples, n_features = X.shape

        random_indices = np.random.choice(n_samples, slef.n_clusters, replace=False)
        self.centers_ = X[random_indices].copy()

        self.attributions_ = np.zeros(n_samples, dtype=int)

        for i in range(self.n_max_iterations):
            prev_centers = self.centers_.copy()

            self._E(X)
            self._M(X)

            if np.allclose(prev_centers, self.centers_):
                break
        return self

    def predict(self, X):
        n_samples = X.shape[0]
        labels = np.zeros(n_samples, dtype=int)

        for i in range(n_samples):
            distances = np.sqrt(np.sum((X[i] - self.centers_) **2, axis=1))
            labels[i] = np.argmin(distaces)
        return labels
