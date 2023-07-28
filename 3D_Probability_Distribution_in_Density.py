import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Sample data
n1, n2 = 100, 100
P1, P2 = 0.52, 0.47

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

# Display the probability
print(f"The probability that the survey will show a greater percentage of Republican voters in the second state than in the first state is: {probability:.2f}")

# Visualization
x = np.linspace(-0.2, 0.2, 1000)
y = stats.norm.pdf(x, loc=mean_diff, scale=std_dev_diff)

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='b')
plt.fill_between(x, y, where=(x >= 0), color='g', alpha=0.5, label='P(Republican 2nd State > 1st State)')
plt.xlabel('Difference in Proportions (p1 - p2)')
plt.ylabel('Probability Density')
plt.title('Probability Distribution')
plt.legend()
plt.grid(True)
plt.show()
