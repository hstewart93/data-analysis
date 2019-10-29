import numpy as np
import matplotlib.pyplot as plt

from input_data import X, tau, w_0


def generate_y(X, w):
    """A function to generate value y given X as a linear distribution."""
    return w.dot(X.T)


def plot_line(X, ax):
    """A function to plot a linear distribution of y against X."""
    y = generate_y(X, w_samp[i, :])
    return ax.plot(X[:, 0], y)


# samples from prior
n_samples = 100

w_samp = np.random.multivariate_normal(w_0.flatten(), tau, size=n_samples)

# create plot
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

for i in range(0, w_samp.shape[0]):
    plot_line(X, ax)

plt.show()

# Iterative procedure to compute and visualise posterior for random data points
index = np.random.permutation(X.shape[0])

for i in range(0, index.shape[0]):
    y = generate_y(X, w_samp[i, :])
    X_i = X[index, :]
    y_i = y[index]
    import ipdb; ipdb.set_trace()