import numpy as np
import plotly.graph_objects as go
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

# Create 3D surface plot with Plotly
fig = go.Figure()

# Plot the confidence interval bounds as a surface
fig.add_trace(go.Surface(
    x=data1_mesh, y=data2_mesh, z=mean_diff_mesh,
    colorscale='Viridis', opacity=0.8,
))

# Add color bar to show confidence levels
color_bar = dict(title='Confidence Level')
fig.update_layout(coloraxis_colorbar=color_bar)

# Add annotations with mathematical expressions
fig.add_trace(go.Scatter3d(
    x=[sample_data_1.mean()], y=[sample_data_2.mean()], z=[lower_bound],
    mode='text', text=['95% CI Lower Bound'], textposition='bottom left'
))
fig.add_trace(go.Scatter3d(
    x=[sample_data_1.mean()], y=[sample_data_2.mean()], z=[upper_bound],
    mode='text', text=['95% CI Upper Bound'], textposition='top left'
))
fig.add_trace(go.Scatter3d(
    x=[sample_data_1.mean()], y=[sample_data_2.mean()], z=[mean_difference],
    mode='text', text=['95% CI'], textposition='bottom left'
))

# Set axis labels and plot title
fig.update_layout(
    scene=dict(
        xaxis_title='Sample Data 1',
        yaxis_title='Sample Data 2',
        zaxis_title='Mean Difference',
    ),
    title='Confidence Interval for Mean Difference',
    width=600,
    height=600,
)

# Show the plot
fig.show()
