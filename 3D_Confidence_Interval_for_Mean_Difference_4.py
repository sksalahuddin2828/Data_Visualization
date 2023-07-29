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

# Set confidence levels for animation
confidence_levels = np.arange(0.80, 1.01, 0.01)

# Prepare data for Probability Density Function plot
d_values = np.linspace(mean_difference - 2 * sd, mean_difference + 2 * sd, 100)
pdf_values = stats.t.pdf(d_values, df, mean_difference, se)

# Create Confidence Interval plot
fig_ci = go.Figure()

for confidence_level in confidence_levels:
    alpha = 1 - confidence_level
    critical_probability = 1 - alpha / 2
    critical_value = stats.t.ppf(critical_probability, df)

    margin_of_error = critical_value * se
    lower_bound = mean_difference - margin_of_error
    upper_bound = mean_difference + margin_of_error

    fig_ci.add_trace(go.Scatter(
        x=[mean_difference, mean_difference],
        y=[lower_bound, upper_bound],
        mode='lines',
        line=dict(color='blue', width=2, dash='solid'),
        name=f'{confidence_level * 100:.1f}% CI',
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
    line=dict(color='green', width=2, dash='dot'),
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

fig_pdf.update_layout(
    title='Probability Density Function',
    xaxis_title='Mean Difference',
    yaxis_title='Probability Density',
    hoverlabel=dict(bgcolor='white'),
)

# Combine plots in a subplot
fig_combined = make_subplots(rows=1, cols=2, subplot_titles=('Confidence Interval', 'Probability Density Function'))
for confidence_level, ci_trace in zip(confidence_levels, fig_ci.data):
    fig_combined.add_trace(ci_trace, row=1, col=1)

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
    updatemenus=[{
        'buttons': [
            {
                'args': [
                    {'visible': [True if i == j else False for j in range(len(confidence_levels))]},
                    {'title': f'Confidence Interval for Mean Difference ({confidence_level * 100:.1f}%)'}
                ],
                'label': f'{confidence_level * 100:.1f}%',
                'method': 'update'
            } for i, confidence_level in enumerate(confidence_levels)
        ],
        'direction': 'down',
        'showactive': True,
        'x': 0.05,
        'y': 1.0,
        'xanchor': 'left',
        'yanchor': 'top',
    }],
)

# Add tooltip with sample mean difference values
fig_combined.update_traces(hoverinfo='text+name', hovertemplate='%{text}<extra></extra>')

# Add slider to adjust sample size
fig_combined.update_layout(
    sliders=[{
        'active': 0,
        'currentvalue': {'prefix': 'Sample Size: '},
        'pad': {'t': 50},
        'len': 0.9,
        'x': 0.05,
        'y': 0,
        'xanchor': 'left',
        'yanchor': 'top',
        'steps': [{'args': [[
            f'Sample Size: {size}',
            dict(visible=[True if size == sample_size else False for size in range(5, 101, 5)])
        ]],
            'label': f'{size}',
            'method': 'update'
        } for size in range(5, 101, 5)]
    }],
)

# Add annotations with mathematical expressions and theory
fig_combined.update_layout(
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
fig_combined.show()
