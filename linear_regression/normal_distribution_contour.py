"""
Create a contour plot of a two-dimensional normal distribution

Parameters
----------
ax: axis handle to plot
mu: mean vector 2x1
Sigma: covariance matrix 2x2
"""

import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt


def plot_distribution(ax, mu, Sigma):
    x = np.linspace(-1.5, 1.5, 100)
    x1p, x2p = np.meshgrid(x, x)
    pos = np.vstack((x1p.flatten(), x2p.flatten())).T

    pdf = multivariate_normal(mu.flatten(), Sigma)
    Z = pdf.pdf(pos)
    Z = Z.reshape(100, 100)

    ax.contour(x1p, x2p, Z, 5, colors='r', alpha=0.7)
    ax.set_xlabel('w_0')
    ax.set_ylabel('w_1')
    plt.show()

    return


fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)

Sigma = np.eye(2)
mu = np.zeros((2, 1))

plot_distribution(ax, mu, Sigma)
