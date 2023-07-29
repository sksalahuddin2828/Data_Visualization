import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.stats as stats

# Simulate paired sample data
np.random.seed(42)
sample_size = 30
sample_data_1 = np.random.normal(loc=10, scale=2, size=sample_size)
sample_data_2 = sample_data_1 + np.random.normal(loc=3, scale=1, size=sample_size)

# Calculate the mean difference and standard deviation of the sample difference
mean_difference = np.mean(sample_data_2 - sample_data_1)
std_dev_difference = np.std(sample_data_2 - sample_data_1, ddof=1)

# Set confidence level
confidence_level = 0.95

# Calculate the standard error of the mean difference
se_mean_difference = std_dev_difference / np.sqrt(sample_size)

# Calculate the critical value based on the confidence level (two-tailed test)
critical_value = stats.t.ppf((1 + confidence_level) / 2, df=sample_size - 1)

# Calculate the margin of error
margin_of_error = critical_value * se_mean_difference

# Calculate the confidence interval
lower_bound = mean_difference - margin_of_error
upper_bound = mean_difference + margin_of_error

# Visualize the results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Sample Data 1')
ax.set_ylabel('Sample Data 2')
ax.set_zlabel('Mean Difference')
ax.scatter(sample_data_1, sample_data_2, sample_data_2 - sample_data_1, c='b', marker='o')
ax.plot(sample_data_1, sample_data_2, lower_bound * np.ones_like(sample_data_1), c='r', linestyle='dashed')
ax.plot(sample_data_1, sample_data_2, upper_bound * np.ones_like(sample_data_1), c='r', linestyle='dashed')
ax.set_title('Confidence Interval for Mean Difference')
plt.show()

# Print the results
print(f"Sample Data 1: {sample_data_1}")
print(f"Sample Data 2: {sample_data_2}")
print(f"Mean Difference: {mean_difference}")
print(f"Standard Error of the Mean Difference: {se_mean_difference}")
print(f"Confidence Interval: ({lower_bound}, {upper_bound})")
