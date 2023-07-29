import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.stats as stats

# Given data
sample_size = 22
mean_difference = 1
sum_diff_squared = 270

# Calculate the standard error (SE)
sd = np.sqrt(sum_diff_squared / (sample_size - 1))
se = sd / np.sqrt(sample_size)

# Set confidence level
confidence_level = 0.90

# Calculate the critical value (t-score)
alpha = 1 - confidence_level
critical_probability = 1 - alpha / 2
df = sample_size - 1
critical_value = stats.t.ppf(critical_probability, df)

# Calculate the margin of error (ME)
margin_of_error = critical_value * se

# Calculate the confidence interval
lower_bound = mean_difference - margin_of_error
upper_bound = mean_difference + margin_of_error

# Prepare data for Probability Density Function plot
d_values = np.linspace(mean_difference - 2 * sd, mean_difference + 2 * sd, 100)
pdf_values = stats.t.pdf(d_values, df, mean_difference, se)

# Create Confidence Interval plot
fig_ci = go.Figure()
fig_ci.add_trace(go.Scatter(
    x=[mean_difference, mean_difference],
    y=[lower_bound, upper_bound],
    mode='lines+markers',
    line=dict(color='blue', width=3),
    name='Confidence Interval',
))
fig_ci.add_trace(go.Scatter(
    x=[mean_difference],
    y=[mean_difference],
    mode='markers',
    marker=dict(color='red', size=10),
    name='Mean Difference',
))
fig_ci.update_layout(
    title='Confidence Interval for Mean Difference',
    xaxis_title='Mean Difference',
    yaxis_title='Difference',
)

# Create Probability Density Function plot
fig_pdf = go.Figure()
fig_pdf.add_trace(go.Scatter(
    x=d_values,
    y=pdf_values,
    mode='lines',
    line=dict(color='green', width=3),
    name='Probability Density Function',
))
fig_pdf.update_layout(
    title='Probability Density Function',
    xaxis_title='Mean Difference',
    yaxis_title='Probability Density',
)

# Combine plots in a subplot
fig_combined = make_subplots(rows=1, cols=2, subplot_titles=('Confidence Interval', 'Probability Density Function'))
fig_combined.add_trace(fig_ci.data[0], row=1, col=1)
fig_combined.add_trace(fig_ci.data[1], row=1, col=1)
fig_combined.add_trace(fig_pdf.data[0], row=1, col=2)

# Update layout for the combined figure
fig_combined.update_layout(
    title='Confidence Interval for Mean Difference between English and Math Test Scores',
    scene2=dict(
        xaxis_title='Mean Difference',
        yaxis_title='Probability Density',
    ),
    width=1000,
    height=500,
)

# Show the plot
fig_combined.show()
