import numpy as np
import plotly.graph_objects as go
import scipy.stats as stats

# Function to calculate the power of the hypothesis test
def calculate_power(sample_size, significance_level, effect_size):
    null_hypothesis_value = 0.5
    alt_hypothesis_value = null_hypothesis_value + effect_size
    z_critical = stats.norm.ppf(1 - significance_level / 2)

    standard_error = np.sqrt((null_hypothesis_value * (1 - null_hypothesis_value)) / sample_size)
    difference = np.abs(null_hypothesis_value - alt_hypothesis_value)
    z_effect = difference / standard_error

    power = 1 - stats.norm.cdf(z_effect - z_critical) + stats.norm.cdf(-z_effect - z_critical)
    return power

# Generate a range of sample sizes, significance levels, and effect sizes
sample_sizes = np.arange(10, 201, 10)
significance_levels = np.linspace(0.001, 0.05, 20)
effect_sizes = np.linspace(0.1, 1.0, 20)

# Calculate the power for each combination of sample size, significance level, and effect size
power_values = np.zeros((len(sample_sizes), len(significance_levels), len(effect_sizes)))
for i, sample_size in enumerate(sample_sizes):
    for j, significance_level in enumerate(significance_levels):
        for k, effect_size in enumerate(effect_sizes):
            power_values[i, j, k] = calculate_power(sample_size, significance_level, effect_size)

# Create meshgrid for heatmap plotting
significance_grid, sample_size_grid, effect_size_grid = np.meshgrid(significance_levels, sample_sizes, effect_sizes, indexing='ij')

# Calculate the total power for each point
total_power = power_values.sum(axis=-1)

# Create the heatmap plot for total power
fig = go.Figure(data=go.Heatmap(
    x=significance_levels,
    y=sample_sizes,
    z=total_power,
    colorscale='Viridis',
    colorbar=dict(title='Total Power'),
))

# Add a creative background shape to highlight a specific region
fig.add_shape(
    type='rect',
    x0=0,
    x1=0.05,
    y0=10,
    y1=200,
    fillcolor='rgba(200, 200, 200, 0.2)',
    line=dict(color='rgba(0, 0, 0, 0)'),
)

# Update layout
fig.update_layout(
    xaxis_title='Significance Level',
    yaxis_title='Sample Size',
    title='Total Statistical Power vs. Significance Level and Sample Size',
    font=dict(family='Arial', size=12, color='black'),
    margin=dict(l=70, r=40, t=80, b=70),
)

# Show the interactive heatmap plot
fig.show()
