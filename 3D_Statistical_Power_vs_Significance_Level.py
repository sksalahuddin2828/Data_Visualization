import numpy as np
import matplotlib.pyplot as plt
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

# Create a range of colors for the lines
colors = plt.cm.rainbow(np.linspace(0, 1, len(sample_sizes)))

# Create the static plot
plt.figure(figsize=(10, 6))

for i, sample_size in enumerate(sample_sizes):
    plt.plot(significance_levels, power_values[i], color=colors[i], linewidth=2, label=f'Sample Size = {sample_size}')

plt.legend(loc='lower right')

plt.xlabel('Significance Level')
plt.ylabel('Power')
plt.title('Power vs. Significance Level')
plt.grid(color='gray', linestyle='-', linewidth=0.5)

plt.show()
