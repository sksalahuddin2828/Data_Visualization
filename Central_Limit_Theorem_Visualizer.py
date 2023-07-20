import numpy as np
import matplotlib.pyplot as plt

# Number of experiments
num_experiments = 10000

# Compute sample means for a large number of experiments
sample_means_large = [np.mean(generate_samples(100)) for _ in range(num_experiments)]

# Plot the histogram of sample means
plt.figure(figsize=(10, 6))
plt.hist(sample_means_large, bins=30, density=True, color='lightblue', alpha=0.7, label='Sample Means')
plt.axvline(x=mu, color='r', linestyle='--', label='True Mean')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.title('Distribution of Sample Means')
plt.legend()
plt.grid(True)

# Fit a normal distribution to the sample means
fit_mu = np.mean(sample_means_large)
fit_sigma = np.std(sample_means_large)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
pdf_normal = 1/(fit_sigma * np.sqrt(2*np.pi)) * np.exp(-(x - fit_mu)**2 / (2 * fit_sigma**2))

# Plot the fitted normal distribution
plt.plot(x, pdf_normal, color='r', linestyle='-', label='Fitted Normal')
plt.legend()
plt.show()
