import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import norm

# Flu count and group size for placebo and vaccine groups
placebo_flu_count = 35
placebo_group_size = 325
vaccine_flu_count = 28
vaccine_group_size = 813

# Calculate proportions of flu cases in each group
placebo_proportion = placebo_flu_count / placebo_group_size
vaccine_proportion = vaccine_flu_count / vaccine_group_size

# Calculate the difference in proportions (effect size)
effect_size = placebo_proportion - vaccine_proportion

# Perform the 2-sample proportions test
n1 = placebo_group_size
n2 = vaccine_group_size
p1 = placebo_proportion
p2 = vaccine_proportion
z_score = (p1 - p2) / np.sqrt((p1*(1-p1)/n1) + (p2*(1-p2)/n2))
p_value = 2 * (1 - norm.cdf(abs(z_score)))

# Calculate the confidence interval for the effect size
standard_error = np.sqrt((p1*(1-p1)/n1) + (p2*(1-p2)/n2))
confidence_interval = (effect_size - 1.96 * standard_error, effect_size + 1.96 * standard_error)

# Create a 3D visualization
x = np.linspace(0.01, 0.2, 100)
y = np.linspace(0.01, 0.1, 100)
X, Y = np.meshgrid(x, y)
Z = Y - X

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('Vaccine Proportion')
ax.set_ylabel('Placebo Proportion')
ax.set_zlabel('Effect Size')
ax.set_title('Effect Size in 3D')
plt.show()

# Print the results
print(f"Effect Size: {effect_size * 100:.2f}%")
print(f"P-value: {p_value:.6f}")
print(f"Confidence Interval: {confidence_interval[0] * 100:.2f}% to {confidence_interval[1] * 100:.2f}%")
