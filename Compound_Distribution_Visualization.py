import numpy as np

def compound_distribution(x):
    # Define a Gaussian distribution
    gaussian_mean, gaussian_std = 10, 2
    gaussian = np.exp(-0.5 * ((x - gaussian_mean) / gaussian_std) ** 2) / (gaussian_std * np.sqrt(2 * np.pi))

    # Define an Exponential distribution
    exponential_lambda = 0.2
    exponential = exponential_lambda * np.exp(-exponential_lambda * x)

    # Define a Uniform distribution
    uniform_low, uniform_high = 5, 15
    uniform = np.where((x >= uniform_low) & (x <= uniform_high), 1 / (uniform_high - uniform_low), 0)

    # Combine the distributions to create a compound distribution
    # You can adjust the weights to change the contribution of each distribution
    compound_dist = 0.6 * gaussian + 0.2 * exponential + 0.2 * uniform

    return compound_dist

# Generate data points for visualization
x_vals = np.linspace(0, 20, 500)
y_vals = compound_distribution(x_vals)

# Plot the compound distribution
import matplotlib.pyplot as plt

plt.plot(x_vals, y_vals, label='Compound Distribution')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.title('Creative Compound Distribution')
plt.grid(True)
plt.show()
