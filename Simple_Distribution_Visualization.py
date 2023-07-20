import numpy as np

def simple_gaussian(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))

# Define parameters for the simple Gaussian distribution
mu_simple, sigma_simple = 10, 2

# Generate data points for visualization
x_vals = np.linspace(0, 20, 500)
y_vals_simple = simple_gaussian(x_vals, mu_simple, sigma_simple)

# Plot the simple Gaussian distribution
import matplotlib.pyplot as plt

plt.plot(x_vals, y_vals_simple, label='Simple Gaussian Distribution')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.title('Simple Gaussian Distribution')
plt.grid(True)
plt.show()
