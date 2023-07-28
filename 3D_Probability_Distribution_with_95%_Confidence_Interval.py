import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Sample data
n1, n2 = 100, 100
P1, P2 = 0.52, 0.47
alpha = 0.05  # Significance level for confidence intervals

# Step 1: Check if the sample size is large enough
assert n1 * P1 >= 10 and n1 * (1 - P1) >= 10, "Sample size for the first state is not large enough."
assert n2 * P2 >= 10 and n2 * (1 - P2) >= 10, "Sample size for the second state is not large enough."

# Step 2: Calculate the mean of the difference in sample proportions
mean_diff = P1 - P2

# Step 3: Calculate the standard deviation of the difference
std_dev_diff = np.sqrt((P1 * (1 - P1) / n1) + (P2 * (1 - P2) / n2))

# Step 4: Calculate the probability using the z-score
z_score = (0 - mean_diff) / std_dev_diff
probability = stats.norm.cdf(z_score)

# Step 5: Calculate the confidence intervals
margin_of_error = stats.norm.ppf(1 - alpha / 2) * std_dev_diff
lower_bound = mean_diff - margin_of_error
upper_bound = mean_diff + margin_of_error

# Display the results
print(f"The probability that the survey will show a greater percentage of Republican voters in the second state than in the first state is: {probability:.2f}")
print(f"Confidence Interval (95%): {lower_bound:.3f} to {upper_bound:.3f}")

# Create a 3D bar plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

x = [mean_diff]
y = [0]
z = [probability]

dx = dy = 0.02
dz = probability

ax.bar3d(x, y, z, dx, dy, dz, shade=True, color='g', alpha=0.7)

ax.set_xlabel('Difference in Proportions (p1 - p2)')
ax.set_ylabel('Probability Density')
ax.set_zlabel('Probability')
ax.set_title('Probability Distribution with 95% Confidence Interval')

# Plot confidence intervals
ax.plot([lower_bound, lower_bound], [0, 0], [0, probability], color='r', linestyle='--', linewidth=2)
ax.plot([upper_bound, upper_bound], [0, 0], [0, probability], color='r', linestyle='--', linewidth=2)

plt.show()
