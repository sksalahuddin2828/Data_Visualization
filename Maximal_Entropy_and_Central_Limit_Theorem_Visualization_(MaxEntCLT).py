import numpy as np
import matplotlib.pyplot as plt

# Define the true distribution parameters
mu = 10
sigma = 2

# Function to generate samples from an arbitrary distribution
def generate_samples(size):
    return np.random.normal(mu, sigma, size)

# Compute sample means for different sample sizes
sample_sizes = [1, 2, 5, 10, 50, 100, 500]
sample_means = [np.mean(generate_samples(size)) for size in sample_sizes]

# Plot the sample means as a function of sample size
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, sample_means, marker='o', linestyle='-', color='b', label='Sample Means')
plt.axhline(y=mu, color='r', linestyle='--', label='True Mean')
plt.xlabel('Sample Size')
plt.ylabel('Sample Mean')
plt.title('Convergence to the True Mean')
plt.legend()
plt.grid(True)
plt.show()
