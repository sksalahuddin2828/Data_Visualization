# Dynamic Visualization of Moderately Skewed Lognormal Distribution and Central Limit Theorem

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set the random seed for reproducibility
np.random.seed(42)

# Generate the moderately skewed lognormal distribution
population_size = 1000000
population = np.random.lognormal(mean=0.5, sigma=0.8, size=population_size)

# Define function for generating sample means
def generate_sample_means(sample_size, num_samples=500000):
    return np.array([np.mean(np.random.choice(population, size=sample_size)) for _ in range(num_samples)])

# Define sample sizes
sample_sizes = [5, 20, 40]

# Initialize the figure and subplots
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(121, projection='3d')  # For the skewed lognormal distribution
ax2 = fig.add_subplot(122)  # For the CLT demonstration

# Plot the moderately skewed lognormal distribution in 3D
x = np.log(population)
y = np.arange(population_size)
ax1.plot(x, y, zs=0, zdir='y', lw=0.5, color='b')
ax1.set_xlabel('Lognormal Distribution')
ax1.set_ylabel('Data Point Index')
ax1.set_zlabel('Density')
ax1.set_title('Moderately Skewed Lognormal Distribution')

# Plot the CLT demonstration for each sample size
for i, sample_size in enumerate(sample_sizes):
    sample_means = generate_sample_means(sample_size)
    ax2.hist(sample_means, bins=50, density=True, alpha=0.7, label=f'Sample Size = {sample_size}')

# Plot the theoretical normal distribution for comparison
x_normal = np.linspace(np.min(population), np.max(population), 100)
y_normal = np.exp(-0.5 * ((x_normal - np.mean(population)) / np.std(population)) ** 2) / (np.std(population) * np.sqrt(2 * np.pi))
ax2.plot(x_normal, y_normal, color='red', lw=2, label='Theoretical Normal Distribution')
ax2.legend()
ax2.set_xlabel('Sample Mean')
ax2.set_ylabel('Density')
ax2.set_title('Central Limit Theorem Demonstration')

# Display the plot
plt.tight_layout()
plt.show()
