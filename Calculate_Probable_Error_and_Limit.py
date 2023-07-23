import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the probable error for 'r'
def probable_error(r, N):
    return 0.674 * (1 - r**2) / np.sqrt(N)

# Given correlation coefficient (r) and sample size (N)
r = 0.7
N = 64

# Calculate the probable error
prob_error = probable_error(r, N)
print(f"Probable Error: {prob_error:.3f}")

# Calculate the lower and upper limits for the population correlation coefficient
lower_limit = r - prob_error
upper_limit = r + prob_error
print(f"Probable Limit: ({lower_limit:.3f}, {upper_limit:.3f})")


# Answer: Probable Error: 0.043
#         Probable Limit: (0.657, 0.743)
