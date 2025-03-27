# K-means Clustering Algorithm

The k-means clustering algorithm identifies groups of data points iteratively, representing the clusters by their respective centres. The training is performed in two steps. 

## Algorithm Overview

1. **Choose the number of clusters to find (k)**. This should be a parameter to your constructor.
2. **Create k number of initial cluster centres**, either random positions or from the training data X. Note that the centres should be different positions.
3. **E step**: Attribute a class label to each data point in X. This is done by attributing the cluster label of the closest cluster centre to each point (for simplicity, assume Euclidean distance).
4. **M step**: Using the attributions from the last step, calculate new cluster centres by finding the mean of the points attributed to each cluster.
5. **Run the E and M steps** until convergence, i.e. when the centres don't move any more.

## Testing

This exercise will be marked by TA-Bot running unit tests on a minimalist system (miniconda with NumPy). You can find these tests in the course code repository. Please let me know if you think TA-Bot is misbehaving.
