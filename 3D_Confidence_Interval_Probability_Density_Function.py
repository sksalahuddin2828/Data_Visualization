import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.stats as stats

# Given data
sample_sizes = np.arange(5, 101, 5)
mean_difference = 1
sum_diff_squared = 270

# Calculate the standard error (SE) for each sample size
sd = np.sqrt(sum_diff_squared / (sample_sizes - 1))
se = sd / np.sqrt(sample_sizes)

# Set confidence level
confidence_level = 0.90

# Calculate the critical value (t-score)
alpha = 1 - confidence_level
critical_probability = 1 - alpha / 2
df = sample_sizes - 1
critical_value = stats.t.ppf(critical_probability, df)

# Calculate the margin of error (ME) for each sample size
margin_of_error = critical_value * se

# Calculate the confidence intervals for each sample size
lower_bound = mean_difference - margin_of_error
upper_bound = mean_difference + margin_of_error

# Prepare data for Probability Density Function plot
d_values = np.linspace(mean_difference - 2 * sd.max(), mean_difference + 2 * sd.max(), 100)
pdf_values = stats.t.pdf(d_values, df[:, np.newaxis], mean_difference, se[:, np.newaxis])

# Create Confidence Interval plot
fig_ci = make_subplots(rows=1, cols=2, subplot_titles=('Confidence Interval', 'Probability Density Function'))

# Add Confidence Interval traces
for i, sample_size in enumerate(sample_sizes):
    fig_ci.add_trace(go.Scatter(
        x=[mean_difference, mean_difference],
        y=[lower_bound[i], upper_bound[i]],
        mode='lines',
        line=dict(color=f'hsl({i / len(sample_sizes) * 360}, 70%, 50%)', width=2, dash='solid'),
        name=f'{sample_size} Samples',
    ), row=1, col=1)

# Add Confidence Interval hover tooltips
for i in range(len(sample_sizes)):
    fig_ci.data[i].update(hovertemplate=(
        f'Sample Size: {sample_sizes[i]}<br>'
        'Confidence Interval: %{y:.2f} to %{customdata[0]:.2f}'
    ))

# Add Sample Mean Difference trace
fig_ci.add_trace(go.Scatter(
    x=[mean_difference] * len(sample_sizes),
    y=mean_difference + np.arange(0, 0.4, 0.4 / len(sample_sizes)),
    customdata=upper_bound,
    mode='markers+text',
    marker=dict(color='red', size=10, symbol='diamond-open'),
    name='Sample Mean Difference',
    text=[f'Sample Mean Difference: {mean_difference}' for _ in range(len(sample_sizes))],
    hoverinfo='text',
    textposition='bottom center',
    showlegend=False,
), row=1, col=1)

# Add Probability Density Function plot
fig_ci.add_trace(go.Scatter(
    x=d_values,
    y=pdf_values.mean(axis=0),
    mode='lines',
    line=dict(color='green', width=2, dash='dot'),
    name='Average PDF',
), row=1, col=2)

# Update layout for the combined figure
fig_ci.update_layout(
    title_text='Confidence Interval for Mean Difference between English and Math Test Scores',
    title_x=0.5,
    width=1000,
    height=500,
    xaxis_title='Mean Difference',
    yaxis_title='Difference',
    xaxis2_title='Mean Difference',
    yaxis2_title='Probability Density',
    showlegend=True,
    legend_title_text='Sample Size',
    hoverlabel=dict(bgcolor='white'),
)

# Add slider to adjust sample size
fig_ci.update_layout(
    sliders=[{
        'active': len(sample_sizes) - 1,
        'currentvalue': {'prefix': 'Sample Size: '},
        'pad': {'t': 50},
        'len': 0.9,
        'x': 0.05,
        'y': 0,
        'xanchor': 'left',
        'yanchor': 'top',
        'steps': [{'args': [[
            f'Sample Size: {sample_size}',
            dict(visible=[True if size == i else False for size in range(len(sample_sizes))])
        ]],
            'label': f'{sample_size}',
            'method': 'update'
        } for i, sample_size in enumerate(sample_sizes)]
    }],
)

# Add annotations with mathematical expressions and theory
fig_ci.update_layout(
    annotations=[
        dict(
            text='Confidence Interval:',
            xref='paper',
            yref='paper',
            x=0.01,
            y=1.08,
            showarrow=False,
        ),
        dict(
            text='Probability Density Function:',
            xref='paper',
            yref='paper',
            x=0.56,
            y=1.08,
            showarrow=False,
        ),
        dict(
            text='Confidence Interval = Sample Mean ± Margin of Error',
            xref='paper',
            yref='paper',
            x=0.01,
            y=1.05,
            showarrow=False,
            font=dict(size=12),
        ),
        dict(
            text='Margin of Error = Critical Value * Standard Error',
            xref='paper',
            yref='paper',
            x=0.01,
            y=1.02,
            showarrow=False,
            font=dict(size=12),
        ),
        dict(
            text='Standard Error = Standard Deviation / √Sample Size',
            xref='paper',
            yref='paper',
            x=0.01,
            y=0.99,
            showarrow=False,
            font=dict(size=12),
        ),
        dict(
            text='95% Confidence Level CI Shown',
            xref='paper',
            yref='paper',
            x=0.55,
            y=1.05,
            showarrow=False,
            font=dict(size=12),
        ),
    ],
)

# Show the plot
fig_ci.show()
