"""
Model a regression task - a model that relates two continuous variables to each other.
Hypothesis space limited to only look at linear relationships.
Note that the concepts are exactly the same as with the binary case (bernoulli distribution).
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_line(ax, w):
    """Method to produce a linear plot given input data."""
    X = np.zeros(2, 2)
    X[0, 0] = -5
    X[1, 0] = 5
    X[:, 1] = 1

    # due to the concatenation we have to flip the transpose
    y = w.dot(X.T)
    ax.plot(X[:, 0], y)

# Create prior distribution
tau = np.eye(2)
w_0 = np.zeros((2, 1))

# Sample from prior
n_samples = 100

w_sample = np.random.multivariate_normal(w_0.flatten(), tau, size=n_samples)

# Create plot
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

for i in w_sample[0]:
    plot_line(ax, w_sample[i, :])

plt.show()
