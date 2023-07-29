import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.stats as stats

# Function to calculate the power of the hypothesis test
def calculate_power(sample_size, significance_level, effect_size=0.5):
    null_hypothesis_value = 0.5
    alt_hypothesis_value = null_hypothesis_value + effect_size
    z_critical = stats.norm.ppf(1 - significance_level / 2)

    standard_error = np.sqrt((null_hypothesis_value * (1 - null_hypothesis_value)) / sample_size)
    difference = np.abs(null_hypothesis_value - alt_hypothesis_value)
    z_effect = difference / standard_error

    power = 1 - stats.norm.cdf(z_effect - z_critical) + stats.norm.cdf(-z_effect - z_critical)
    return power

# Generate a range of sample sizes and significance levels
sample_sizes = np.arange(10, 201, 10)
significance_levels = np.linspace(0.001, 0.05, 20)

# Calculate the power for each combination of sample size and significance level
power_values = np.zeros((len(sample_sizes), len(significance_levels)))
for i, sample_size in enumerate(sample_sizes):
    for j, significance_level in enumerate(significance_levels):
        power_values[i, j] = calculate_power(sample_size, significance_level)

# Create a Plotly figure
fig = make_subplots(rows=1, cols=1)

# Add traces for each sample size
for i, sample_size in enumerate(sample_sizes):
    fig.add_trace(
        go.Scatter(
            x=significance_levels,
            y=power_values[i],
            mode='lines',
            line=dict(color=f'hsl({i / len(sample_sizes) * 360}, 70%, 50%)'),
            name=f'Sample Size = {sample_size}'
        )
    )

# Layout customization
fig.update_layout(
    title={
        'text': 'Statistical Power vs. Significance Level for Different Sample Sizes',
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=18)
    },
    xaxis_title='Significance Level',
    yaxis_title='Power',
    xaxis=dict(tickformat='.3f'),
    yaxis=dict(tickformat='.2f'),
    xaxis_ticksuffix='',
    yaxis_ticksuffix='',
    plot_bgcolor='#f0f0f0',  # Background color
    paper_bgcolor='#f0f0f0',  # Plot area color
    font=dict(family='Arial', size=12, color='black'),
    margin=dict(l=70, r=40, t=80, b=70),  # Margins to adjust the plot position
)

# Show the interactive plot
fig.show()
