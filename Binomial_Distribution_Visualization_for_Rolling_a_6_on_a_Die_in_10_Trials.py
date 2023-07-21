import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate the probability of rolling exactly k 6s in n trials
def binomial_probability(n, k, p):
    q = 1 - p
    return np.math.comb(n, k) * (p ** k) * (q ** (n - k))

# Function to calculate cumulative probability of rolling k or more 6s in n trials
def cumulative_probability(n, k, p):
    cumulative_prob = 0
    for i in range(k, n + 1):
        cumulative_prob += binomial_probability(n, i, p)
    return cumulative_prob

# Constants for the die roll
num_trials = 10
p_six = 1 / 6  # Probability of rolling a 6 on a fair die

# Calculate probabilities for rolling k 6s in ten trials
results = []
cumulative_probs = []
for k in range(num_trials + 1):
    prob_k = binomial_probability(num_trials, k, p_six)
    cumulative_prob_k = cumulative_probability(num_trials, k, p_six)
    results.append(prob_k)
    cumulative_probs.append(cumulative_prob_k)

# 3D bar plot to visualize probabilities for each number of 6s rolled
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

x = np.arange(num_trials + 1)
y = results
z = np.zeros(num_trials + 1)

dx = dy = 0.5
dz = y

ax.bar3d(x, y, z, dx, dy, dz, shade=True, color='b', alpha=0.8)

ax.set_xlabel('Number of 6s rolled')
ax.set_ylabel('Probability')
ax.set_zlabel('Frequency')
ax.set_title('Probability of Rolling k 6s in 10 Trials')

# Add frequency values as text labels on top of bars
for xi, yi, zi in zip(x, y, z + dz):
    ax.text(xi + dx / 2, yi, zi, f'{zi:.2f}', ha='center', va='bottom', fontsize=9)

# 2D area plot to visualize cumulative probabilities for rolling four or more 6s
fig2, ax2 = plt.subplots(figsize=(10, 6))

ax2.fill_between(range(num_trials + 1), cumulative_probs, color='orange', alpha=0.6)
ax2.set_xlabel('Number of 6s rolled')
ax2.set_ylabel('Cumulative Probability')
ax2.set_title('Cumulative Probability of Rolling 4 or More 6s in 10 Trials')

plt.tight_layout()
plt.show()
