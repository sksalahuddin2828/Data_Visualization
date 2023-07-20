import numpy as np

def complex_distribution(x):
    # Define a mixture of three Gaussian distributions
    mu1, sigma1 = 5, 1
    mu2, sigma2 = 12, 2
    mu3, sigma3 = 20, 3

    # Calculate the PDF of each Gaussian distribution
    pdf1 = np.exp(-0.5 * ((x - mu1) / sigma1) ** 2) / (sigma1 * np.sqrt(2 * np.pi))
    pdf2 = np.exp(-0.5 * ((x - mu2) / sigma2) ** 2) / (sigma2 * np.sqrt(2 * np.pi))
    pdf3 = np.exp(-0.5 * ((x - mu3) / sigma3) ** 2) / (sigma3 * np.sqrt(2 * np.pi))

    # Combine the three PDFs to create a complex distribution
    # You can adjust the weights to change the contribution of each Gaussian
    complex_dist = 0.4 * pdf1 + 0.3 * pdf2 + 0.3 * pdf3
    return complex_dist

# Generate data points for visualization
x_vals = np.linspace(-5, 30, 500)
y_vals = complex_distribution(x_vals)

# Plot the complex distribution
import matplotlib.pyplot as plt

plt.plot(x_vals, y_vals, label='Complex Distribution')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.title('Complex Distribution')
plt.grid(True)
plt.show()
