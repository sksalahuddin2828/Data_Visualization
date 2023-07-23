import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the probable error for 'r'
def probable_error(r, N):
    return 0.674 * (1 - r**2) / np.sqrt(N)

# Given correlation coefficient (r) and sample size (N)
r = 0.8
N = 25

# Calculate the probable error
prob_error = probable_error(r, N)
print(f"Probable Error: {prob_error:.4f}")


# Answer: Probable Error: 0.0485
