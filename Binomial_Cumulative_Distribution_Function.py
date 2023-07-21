import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def binomial_cumulative(n, p, k):
    q = 1 - p
    return 1 - np.sum([binomial_probability(n, p, i) for i in range(k)])

def binomial_probability(n, p, k):
    return np.math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

n_trials = 10
probability_of_six = 1 / 6  # Probability of rolling a six in a single roll
desired_successes = np.arange(3, n_trials + 1)
cumulative_probabilities = [binomial_cumulative(n_trials, probability_of_six, k) for k in desired_successes]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x_pos = np.arange(len(desired_successes))
y_pos = cumulative_probabilities
z_pos = np.zeros_like(y_pos)
dx = dy = 0.5
dz = y_pos

ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, shade=True)

# Customize the plot
ax.set_xlabel('Number of Sixes')
ax.set_ylabel('Cumulative Probability')
ax.set_zlabel('Probability')
ax.set_title('Binomial Cumulative Distribution Function')

# Show the plot
plt.show()
