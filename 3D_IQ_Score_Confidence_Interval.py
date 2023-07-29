import numpy as np
import pandas as pd
import plotly.graph_objects as go

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

# Print the results
print(f"Standard Error: {SE:.2f}")
print(f"Critical Value: {critical_value:.2f}")
print(f"Margin of Error: {ME:.2f}")
print(f"99% Confidence Interval: {lower_bound:.2f} to {upper_bound:.2f}")

# Create the interactive plot
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

# Set layout and axis labels
fig.update_layout(
    title="IQ Score Confidence Interval",
    yaxis=dict(
        title="IQ Score",
        range=[100, 130]  # Adjust the y-axis range for better visualization
    )
)

# Show the plot
fig.show()
