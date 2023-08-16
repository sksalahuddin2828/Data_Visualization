import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function and its terms
def exponential_series(x, n_terms):
    terms = [x**k / np.math.factorial(k) for k in range(n_terms)]
    return np.sum(terms)

# Generate data for the visualization
x_vals = np.linspace(-2, 2, 100)
n_terms = np.arange(1, 11)
X, N = np.meshgrid(x_vals, n_terms)
Z = np.array([exponential_series(x, n) for x, n in zip(np.ravel(X), np.ravel(N))]).reshape(X.shape)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the function
surface = ax.plot_surface(X, N, Z, cmap='viridis')

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('Number of Terms')
ax.set_zlabel('f(x)')
ax.set_title('3D Visualization of e^x Series')

# Add a colorbar
fig.colorbar(surface, ax=ax)

plt.show()
