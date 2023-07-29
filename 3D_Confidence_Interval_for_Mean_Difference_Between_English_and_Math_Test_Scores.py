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
    showlegend=False,
))

fig_ci.add_trace(go.Scatter(
    x=[mean_difference],
    y=[mean_difference],
    mode='markers',
    marker=dict(color='red', size=10, symbol='diamond-open'),
    name='Sample Mean Difference',
    text=f'Sample Mean Difference: {mean_difference}',
    hoverinfo='text',
))

fig_ci.add_shape(
    type='line',
    x0=mean_difference,
    y0=lower_bound,
    x1=mean_difference,
    y1=upper_bound,
    line=dict(color='blue', width=2, dash='dash'),
)

fig_ci.add_annotation(
    x=mean_difference,
    y=(lower_bound + upper_bound) / 2,
    xref='x',
    yref='y',
    text=f'Confidence Interval\n({lower_bound:.2f}, {upper_bound:.2f})',
    showarrow=True,
    arrowhead=3,
    ax=40,
    ay=0,
    bgcolor='rgba(255, 255, 255, 0.8)',
)

fig_ci.update_layout(
    title='Confidence Interval for Mean Difference',
    xaxis_title='Mean Difference',
    yaxis_title='Difference',
    hoverlabel=dict(bgcolor='white'),
)

# Create Probability Density Function plot
fig_pdf = go.Figure()

fig_pdf.add_trace(go.Scatter(
    x=d_values,
    y=pdf_values,
    mode='lines',
    line=dict(color='green', width=3),
    name='Probability Density Function',
    showlegend=False,
))

fig_pdf.add_trace(go.Scatter(
    x=[mean_difference],
    y=[0],
    mode='markers',
    marker=dict(color='red', size=10, symbol='diamond-open'),
    name='Sample Mean Difference',
    text=f'Sample Mean Difference: {mean_difference}',
    hoverinfo='text',
))

fig_pdf.add_shape(
    type='line',
    x0=lower_bound,
    y0=0,
    x1=upper_bound,
    y1=0,
    line=dict(color='blue', width=2, dash='dash'),
)

fig_pdf.update_layout(
    title='Probability Density Function',
    xaxis_title='Mean Difference',
    yaxis_title='Probability Density',
    hoverlabel=dict(bgcolor='white'),
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

# Add animated transition between Confidence Interval and Probability Density Function plots
animation_steps = []
for i in range(10, 100, 10):
    step = dict(
        method='animate',
        args=[
            [f'Confidence Interval: {i}%'],
            dict(frame=dict(duration=200, redraw=True), fromcurrent=True, mode='immediate')
        ],
        label=f'{i}%',
    )
    animation_steps.append(step)

fig_combined.update_layout(
    updatemenus=[
        dict(
            buttons=list(animation_steps),
            x=0.15,
            y=1.0,
            xanchor='left',
            yanchor='top',
        ),
    ],
    annotations=[
        dict(
            text='Animate Confidence Level:',
            x=0,
            y=1.08,
            xref='paper',
            yref='paper',
            showarrow=False,
        ),
    ]
)

# Show the plot
fig_combined.show()
