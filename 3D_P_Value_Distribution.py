import numpy as np
from scipy import stats

def calculate_mean(data):
    return np.mean(data)

def calculate_proportion(data, value):
    return np.mean(data == value)

def calculate_t_statistic(data, null_value):
    t_stat = (calculate_mean(data) - null_value) / (np.std(data, ddof=1) / np.sqrt(len(data)))
    return t_stat

def calculate_z_score(data, null_value, pop_std_dev):
    z_score = (calculate_mean(data) - null_value) / (pop_std_dev / np.sqrt(len(data)))
    return z_score

def calculate_p_value(t_stat, degrees_of_freedom, two_tailed=True):
    if two_tailed:
        if degrees_of_freedom is not None:
            p_value = 2 * (1 - stats.t.cdf(np.abs(t_stat), degrees_of_freedom))
        else:
            p_value = 2 * (1 - stats.norm.cdf(np.abs(t_stat)))
    else:
        if degrees_of_freedom is not None:
            p_value = 1 - stats.t.cdf(np.abs(t_stat), degrees_of_freedom)
        else:
            p_value = 1 - stats.norm.cdf(np.abs(t_stat))
    return p_value

def hypothesis_test(data, null_value, alpha=0.05, two_tailed=True):
    if isinstance(data, list):
        data = np.array(data)

    if len(data) < 30:
        t_stat = calculate_t_statistic(data, null_value)
        degrees_of_freedom = len(data) - 1
        p_value = calculate_p_value(t_stat, degrees_of_freedom, two_tailed)
        hypothesis_result = "Reject" if p_value < alpha else "Fail to reject"
    else:
        z_score = calculate_z_score(data, null_value, pop_std_dev=1.0)  # Assuming known population standard deviation
        p_value = calculate_p_value(z_score, degrees_of_freedom=None, two_tailed=two_tailed)
        hypothesis_result = "Reject" if p_value < alpha else "Fail to reject"

    return hypothesis_result, p_value

import matplotlib.pyplot as plt

def plot_bar_chart(data, labels, title, xlabel, ylabel):
    plt.figure(figsize=(8, 6))
    plt.bar(labels, data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def plot_p_value_distribution(p_values, alpha, title):
    plt.figure(figsize=(8, 6))
    plt.hist(p_values, bins=20, edgecolor='black', alpha=0.7)
    plt.axvline(alpha, color='red', linestyle='dashed', label=f"Alpha ({alpha})")
    plt.xlabel('P-value')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.legend()
    plt.show()

# Example usage with coin flip data
np.random.seed(42)
coin_flips = np.random.randint(0, 2, 50)  # Simulating coin flips (0 = Tails, 1 = Heads)

null_hypothesis_value = 0.5
hypothesis_result, p_value = hypothesis_test(coin_flips, null_hypothesis_value)

print(f"Null Hypothesis: P = {null_hypothesis_value}")
print(f"Hypothesis Result: {hypothesis_result}")
print(f"P-value: {p_value}")

# Example of bar chart visualization
plot_bar_chart([np.sum(coin_flips == 0), np.sum(coin_flips == 1)], 
               labels=['Tails', 'Heads'], 
               title='Coin Flip Results', 
               xlabel='Outcome', 
               ylabel='Frequency')

# Example of P-value distribution visualization
p_values = np.random.rand(1000)  # Simulating random p-values
plot_p_value_distribution(p_values, alpha=0.05, title='P-value Distribution')
