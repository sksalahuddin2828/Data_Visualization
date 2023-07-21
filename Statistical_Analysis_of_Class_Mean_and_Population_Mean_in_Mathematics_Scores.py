import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp

# Given data
class_mean_score = 70
population_mean_score = 55
population_deviation = 35
sample_size = 60

# Create random samples from the population with mean and deviation
np.random.seed(42)
population_scores = np.random.normal(population_mean_score, population_deviation, size=100000)

# Perform one-sample t-test
t_stat, p_value = ttest_1samp(population_scores, class_mean_score)

# Check if p-value is less than the significance level (e.g., 0.05) for a two-tailed test
significance_level = 0.05
is_significant = p_value < significance_level

# Print the results
print("T-statistic:", t_stat)
print("P-value:", p_value)
print("Is the class mean significant from the population mean?", is_significant)

# Create a histogram to visualize the distribution of population scores
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(population_scores, bins=50, density=True, alpha=0.7, color='blue', label='Population Scores')

# Add a vertical line for the class mean score
ax.axvline(class_mean_score, color='red', linestyle='dashed', linewidth=2, label='Class Mean (Sample)')

# Add a vertical line for the population mean score
ax.axvline(population_mean_score, color='green', linestyle='dashed', linewidth=2, label='Population Mean')

# Add labels and title
ax.set_xlabel('Mathematics Score')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Population Scores with Class Mean and Population Mean')

# Add a legend
ax.legend()

# Show the plot
plt.grid()
plt.show()
