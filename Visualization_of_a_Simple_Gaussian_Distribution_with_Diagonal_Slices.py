import numpy as np
import matplotlib.pyplot as plt

def simple_gaussian(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))

# Define parameters for the simple Gaussian distribution
mu_simple, sigma_simple = 10, 2

# Generate data points for visualization
x_vals = np.linspace(0, 20, 500)
y_vals_simple = simple_gaussian(x_vals, mu_simple, sigma_simple)

# Plot the simple Gaussian distribution
plt.figure(figsize=(12, 8))

# Main plot
plt.subplot(2, 2, (1, 3))
plt.plot(x_vals, y_vals_simple, label='Simple Gaussian Distribution')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.title('Simple Gaussian Distribution')
plt.grid(True)

# Diagonal slice f(x)
x_slice = 12
y_vals_slice_x = simple_gaussian(x_slice, mu_simple, sigma_simple) * np.ones_like(x_vals)
plt.subplot(2, 2, 2)
plt.plot(x_vals, y_vals_simple, label='Simple Gaussian Distribution')
plt.plot(x_vals, y_vals_slice_x, '--', label=f'f(x={x_slice})')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.title(f'Diagonal Slice f(x={x_slice})')
plt.grid(True)

# Diagonal slice g(y)
y_slice = 0.08
x_vals_slice_y = np.linspace(mu_simple - 3*sigma_simple, mu_simple + 3*sigma_simple, 500)
x_vals_slice_y_values = simple_gaussian(x_vals_slice_y, mu_simple, sigma_simple)
plt.subplot(2, 2, 4)
plt.plot(x_vals, y_vals_simple, label='Simple Gaussian Distribution')
plt.plot(x_vals_slice_y, x_vals_slice_y_values, '--', label=f'g(y={y_slice})')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.title(f'Diagonal Slice g(y={y_slice})')
plt.grid(True)

plt.tight_layout()
plt.show()
