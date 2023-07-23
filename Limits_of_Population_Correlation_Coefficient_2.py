import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the probable error (P.E.) for 'r'
def probable_error(r, N):
    return 0.674 * (1 - r**2) / np.sqrt(N)

# Function to calculate the standard error (SE) for 'r'
def standard_error(r, N):
    return np.sqrt((1 - r**2) / N)

# Given correlation coefficient (r) and sample size (N)
r = 0.7
N = 64

# Calculate the probable error and standard error
prob_error = probable_error(r, N)
standard_err = standard_error(r, N)

# Calculate the lower and upper limits for the population correlation coefficient
lower_limit = r - prob_error
upper_limit = r + prob_error

# Visualization
plt.figure(figsize=(8, 6))
plt.plot([r, r], [0, 1], 'r--', label='r')
plt.plot([lower_limit, lower_limit], [0, 1], 'g--', label='Lower Limit')
plt.plot([upper_limit, upper_limit], [0, 1], 'b--', label='Upper Limit')
plt.xlabel('Correlation Coefficient')
plt.ylabel('Probability Density')
plt.title('Limits of Population Correlation Coefficient')
plt.legend()
plt.grid(True)
plt.show()

print(f"Probable Error (P.E.): {prob_error:.3f}")
print(f"Standard Error (SE): {standard_err:.3f}")
print(f"Population Correlation Coefficient Limits: ({lower_limit:.3f}, {upper_limit:.3f})")
