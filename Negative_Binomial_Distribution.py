import numpy as np
import matplotlib.pyplot as plt

def negative_binomial_probability(p, k, r):
    q = 1 - p
    return np.math.comb(k - 1, r - 1) * (p ** r) * (q ** (k - r))

# Probability of rolling a 6 in a single roll
probability_of_six = 1 / 6

# Number of 6s desired
desired_successes = 5

# Calculate probabilities for different numbers of rolls (let's say up to 100 rolls)
total_rolls = np.arange(1, 101)
probabilities = [negative_binomial_probability(probability_of_six, k, desired_successes) for k in total_rolls]

cumulative_probabilities = np.cumsum(probabilities)

required_rolls_index = np.argmax(cumulative_probabilities >= 0.5)
required_rolls = total_rolls[required_rolls_index]

fig, ax1 = plt.subplots()

# Bar plot for probabilities of rolling five 6s
ax1.bar(total_rolls, probabilities, color='b', alpha=0.5)
ax1.set_xlabel('Number of Rolls')
ax1.set_ylabel('Probability', color='b')
ax1.set_ylim(0, max(probabilities) + 0.01)
ax1.tick_params(axis='y', labelcolor='b')

# Line plot for cumulative probabilities
ax2 = ax1.twinx()
ax2.plot(total_rolls, cumulative_probabilities, color='r', marker='o', linestyle='--')
ax2.set_ylabel('Cumulative Probability', color='r')
ax2.set_ylim(0, 1.05)
ax2.tick_params(axis='y', labelcolor='r')

# Highlight the point with 50% cumulative probability
ax2.axhline(y=0.5, color='gray', linestyle='--', alpha=0.7)
ax2.axvline(x=required_rolls, color='gray', linestyle='--', alpha=0.7)

# Add a title
plt.title('Negative Binomial Distribution for Rolling Five 6s')

plt.show()
