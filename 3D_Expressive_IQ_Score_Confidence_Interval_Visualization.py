import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.stats as stats

# Given data
n_sample = 150
sample_mean = 115
sample_std = 10
confidence_level = 0.99

# Calculate standard error
SE = sample_std / np.sqrt(n_sample)

# Find critical value (t-distribution for small sample size)
alpha = 1 - confidence_level
df = n_sample - 1
critical_value = stats.t.ppf(1 - alpha / 2, df)

# Calculate margin of error
ME = critical_value * SE

# Calculate confidence interval
lower_bound = sample_mean - ME
upper_bound = sample_mean + ME

# Display theoretical explanation for the confidence interval
print("Theoretical Explanation:")
print(f"We are {confidence_level * 100:.0f}% confident that the true population mean IQ score lies within the")
print(f"interval [{lower_bound:.2f}, {upper_bound:.2f}]. This means that if we were to draw multiple")
print(f"random samples of {n_sample} students from the population and compute the confidence interval")
print(f"for each sample, approximately {confidence_level * 100:.0f}% of those intervals would contain the true")
print(f"population mean.")

# Create some creative elements for the interactive Plotly plot
confetti_colors = ['rgba(255, 0, 0, 0.8)', 'rgba(0, 255, 0, 0.8)', 'rgba(0, 0, 255, 0.8)']
confetti_shapes = ['circle', 'star', 'hexagram']

# Create the interactive plot using Plotly
fig = go.Figure()

# Add the confidence interval bar
fig.add_trace(go.Bar(
    x=["IQ Score"],
    y=[sample_mean],
    error_y=dict(
        type='data',
        symmetric=False,
        array=[ME],
        arrayminus=[ME],
        color="rgba(255, 0, 0, 0.7)"  # Red color for the error bar
    ),
    marker=dict(
        color="rgba(0, 128, 255, 0.7)",  # Blue color for the bar
    ),
    name="IQ Score",
))

# Add confetti-like shapes to the plot
for i in range(100):
    fig.add_trace(go.Scatter(
        x=["IQ Score"],
        y=[sample_mean + np.random.uniform(-ME, ME)],
        mode='markers',
        marker=dict(
            size=np.random.randint(5, 15),
            color=np.random.choice(confetti_colors),
            symbol=np.random.choice(confetti_shapes),
        ),
        showlegend=False,
    ))

# Set layout and axis labels for the Plotly plot
fig.update_layout(
    title="IQ Score Confidence Interval",
    yaxis=dict(
        title="IQ Score",
        range=[100, 130]  # Adjust the y-axis range for better visualization
    ),
)

# Show the Plotly plot
fig.show()

# Create the 3D scatter plot using Matplotlib
num_points = 1000
iq_scores = np.random.normal(loc=sample_mean, scale=sample_std, size=num_points)

# Plot the 3D scatter plot
fig_3d = plt.figure(figsize=(10, 8))
ax_3d = fig_3d.add_subplot(111, projection='3d')
ax_3d.scatter(iq_scores, np.zeros(num_points), np.zeros(num_points), c=iq_scores, cmap='viridis', marker='o')

# Set labels and title for the 3D plot
ax_3d.set_xlabel('IQ Score')
ax_3d.set_ylabel(' ')
ax_3d.set_zlabel(' ')
plt.title('3D Scatter Plot of IQ Scores with Confidence Interval')

# Add confidence interval lines to the 3D plot
ax_3d.plot([lower_bound, upper_bound], [0, 0], [0, 0], 'r', marker='o', markersize=8)

# Add mathematical equation for the confidence interval as 2D annotation
math_expression = "Confidence Interval = mean ± t_alpha/2,n-1 * SE"
ax_3d.text(lower_bound + (upper_bound - lower_bound) / 2, -5, 0, math_expression, fontsize=12, color='blue', ha='center')

plt.show()
