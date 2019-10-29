"""Input matrix data used in this example case."""

import numpy as np


# Input value for X
X = np.zeros((2, 2))
X[0, 0] = -5
X[1, 0] = 5
X[:, 1] = 1


# Prior distribution
tau = np.eye(2)
w_0 = np.zeros((2, 1))