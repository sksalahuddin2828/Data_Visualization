import numpy as np
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

# Create a meshgrid for 3D surface plot
data1_range = np.linspace(min(sample_data_1), max(sample_data_1), 100)
data2_range = np.linspace(min(sample_data_2), max(sample_data_2), 100)
data1_mesh, data2_mesh = np.meshgrid(data1_range, data2_range)
mean_diff_mesh = data2_mesh - data1_mesh

# Visualize the results with 3D surface plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Sample Data 1')
ax.set_ylabel('Sample Data 2')
ax.set_zlabel('Mean Difference')
ax.set_title('Confidence Interval for Mean Difference', fontsize=16, pad=20)

# Plot the confidence interval bounds as a surface
confidence_interval_surface = ax.plot_surface(
    data1_mesh, data2_mesh, mean_diff_mesh,
    cmap='viridis', alpha=0.8, rstride=100, cstride=100
)

# Add colorbar to show confidence levels
cbar = fig.colorbar(confidence_interval_surface, shrink=0.6, aspect=10)
cbar.ax.set_ylabel('Confidence Level', fontsize=14)

# Add annotations with mathematical expressions
annotation = r'$\bar{d} \pm t_{\alpha/2, n-1} \times SE(\bar{d})$'
annotation_lower = r'$\bar{d} - t_{\alpha/2, n-1} \times SE(\bar{d})$'
annotation_upper = r'$\bar{d} + t_{\alpha/2, n-1} \times SE(\bar{d})$'
ax.text(sample_data_1.mean(), sample_data_2.mean(), lower_bound,
        annotation_lower, color='red', ha='left', va='bottom', fontsize=14)
ax.text(sample_data_1.mean(), sample_data_2.mean(), upper_bound,
        annotation_upper, color='red', ha='left', va='top', fontsize=14)
ax.text(sample_data_1.mean(), sample_data_2.mean(), mean_difference,
        annotation, color='red', ha='left', va='bottom', fontsize=14)

# Show the plot
plt.show()
