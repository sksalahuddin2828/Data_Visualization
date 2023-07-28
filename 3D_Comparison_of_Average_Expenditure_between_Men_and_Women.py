import numpy as np
from scipy import stats
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Data for men
mean_men = 20
std_dev_men = 3
sample_size_men = 500

# Data for women
mean_women = 15
std_dev_women = 2
sample_size_women = 1000

# Calculate standard error
se = np.sqrt((std_dev_men ** 2) / sample_size_men + (std_dev_women ** 2) / sample_size_women)

# Calculate critical value (z-score) for a 99% confidence level
confidence_level = 0.99
alpha = 1 - confidence_level
critical_value = stats.norm.ppf(1 - alpha / 2)

# Calculate margin of error
margin_of_error = critical_value * se

# Calculate the difference in means
mean_difference = mean_men - mean_women

# Calculate the confidence interval
lower_bound = mean_difference - margin_of_error
upper_bound = mean_difference + margin_of_error

print(f"99% Confidence Interval for Spending Difference between Men and Women: ${mean_difference:.2f} ± ${margin_of_error:.2f}")
print(f"Range: ${lower_bound:.2f} to ${upper_bound:.2f}")

# Generate additional data points for the 3D plot
x = np.linspace(mean_men - 3 * std_dev_men, mean_men + 3 * std_dev_men, 100)
y = np.linspace(mean_women - 3 * std_dev_women, mean_women + 3 * std_dev_women, 100)
X, Y = np.meshgrid(x, y)

# Calculate the Z values (difference in means) for the 3D plot
Z = X - Y

# Create the 3D plot
fig = go.Figure()
fig.add_trace(go.Surface(z=Z, x=X, y=Y, colorscale='Viridis'))

# Add the means for men and women with error bars
fig.add_trace(go.Scatter3d(x=[mean_men], y=[mean_women], z=[mean_difference],
                           mode='markers', marker=dict(size=5, color='red'), name='Means'))
fig.add_trace(go.Scatter3d(x=[mean_men, mean_men], y=[mean_women, mean_women],
                           z=[lower_bound, upper_bound], mode='lines', line=dict(color='black'),
                           name='Confidence Interval'))

fig.update_layout(title="Spending Difference between Men and Women",
                  scene=dict(xaxis_title="Men Spending", yaxis_title="Women Spending", zaxis_title="Difference"),
                  height=600, width=800)

# Show the bar plot for means and confidence intervals
plt.bar(['Men', 'Women'], [mean_men, mean_women], yerr=[margin_of_error, margin_of_error], capsize=5)
plt.ylabel('Average Expenditure', fontsize=12)
plt.title('Comparison of Average Expenditure between Men and Women', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--')
plt.show()

# Show the 3D plot
fig.show()
