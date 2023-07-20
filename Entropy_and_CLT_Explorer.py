import numpy as np
import matplotlib.pyplot as plt

# Compute the entropy of a given distribution
def entropy(probabilities):
    return -np.sum(probabilities * np.log(probabilities))

# Calculate the probabilities of the sample means distribution
hist, bins = np.histogram(sample_means_large, bins=30, density=True)
probabilities = hist * np.diff(bins)

# Calculate the entropy of the sample means distribution
entropy_sample_means = entropy(probabilities)

# Calculate the entropy of the fitted normal distribution
probabilities_normal = 1/(fit_sigma * np.sqrt(2*np.pi)) * np.exp(-(bins[:-1] - fit_mu)**2 / (2 * fit_sigma**2)) * np.diff(bins)
entropy_normal = entropy(probabilities_normal)

print("Entropy of Sample Means Distribution:", entropy_sample_means)
print("Entropy of Fitted Normal Distribution:", entropy_normal)


# Answer: Entropy of Sample Means Distribution: 2.838312394271712
#         Entropy of Fitted Normal Distribution: 2.8320086397180475
