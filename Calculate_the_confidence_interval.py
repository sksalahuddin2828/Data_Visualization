import numpy as np
import pandas as pd
import scipy.stats as stats

# Given data
n_boys = 400
n_girls = 300
p_boys = 0.40
p_girls = 0.30
confidence_level = 0.90

# Calculate the standard error
SE = np.sqrt((p_boys * (1 - p_boys) / n_boys) + (p_girls * (1 - p_girls) / n_girls))

# Calculate the critical value
alpha = 1 - confidence_level
z_critical = stats.norm.ppf(1 - alpha / 2)

# Calculate the margin of error
ME = z_critical * SE

# Calculate the confidence interval
lower_bound = p_boys - p_girls - ME
upper_bound = p_boys - p_girls + ME

# Print the results
print(f"Standard Error: {SE:.3f}")
print(f"Critical Value: {z_critical:.3f}")
print(f"Margin of Error: {ME:.3f}")
print(f"Confidence Interval: {lower_bound:.3f} to {upper_bound:.3f}")


# Answer: Standard Error: 0.036
#         Critical Value: 1.645
#         Margin of Error: 0.059
#         Confidence Interval: 0.041 to 0.159
