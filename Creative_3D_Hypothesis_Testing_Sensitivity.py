import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import ipywidgets as widgets
from IPython.display import display

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

# Create interactive plots to show the effect of sample size and significance level on power
def plot_power(sample_size_idx, significance_level_idx):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(significance_levels, power_values[sample_size_idx], marker='o')
    ax.set_xlabel('Significance Level')
    ax.set_ylabel('Power')
    ax.set_title(f'Power vs. Significance Level (Sample Size = {sample_sizes[sample_size_idx]})')
    plt.show()

sample_size_slider = widgets.IntSlider(min=0, max=len(sample_sizes)-1, step=1, value=0, description='Sample Size Index:')
significance_level_slider = widgets.IntSlider(min=0, max=len(significance_levels)-1, step=1, value=0, description='Significance Level Index:')
widgets.interactive(plot_power, sample_size_idx=sample_size_slider, significance_level_idx=significance_level_slider)
