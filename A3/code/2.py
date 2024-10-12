import matplotlib.pyplot as plt
import numpy as np


# Custom Epanechnikov KDE class
class EpanechnikovKDE:
    def __init__(self, bandwidth=1.0):
        self.bandwidth = bandwidth
        self.data = None

    def fit(self, data):
        """Fit the KDE model with the given data."""
        self.data = data

    def epanechnikov_kernel(self, x, xi):
        """Epanechnikov kernel function."""
        a = np.linalg.norm((x - xi) / self.bandwidth, axis=-1)
        return np.where(a <= 1, 3 / 4 * (1 - a**2), 0)[()]

    def evaluate(self, x):
        """Evaluate the KDE at point x."""
        return self.epanechnikov_kernel(x, self.data).mean() / self.bandwidth


# Load the data from the NPZ file
data_file = np.load("transaction_data.npz")
data = data_file["data"]

# TODO: Initialize the EpanechnikovKDE class
epanechnikov_kde = EpanechnikovKDE()

# TODO: Fit the data
epanechnikov_kde.fit(data)

# TODO: Plot the estimated density in a 3D plot
X = np.arange(-10, 10.25, 0.25)
Y = np.arange(-10, 10.25, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.zeros_like(X)
for x in range(X.shape[0]):
    for y in range(X.shape[1]):
        Z[x, y] = epanechnikov_kde.evaluate(np.array([X[x, y], Y[x, y]]))
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, vmin=Z.min() * 2)

# TODO: Save the plot
fig.savefig("transaction_distribution.png", dpi=300)
