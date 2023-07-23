import numpy as np

# Function to calculate the probable error for ρ (rho) using the Spearman method
def probable_error_spearman(rho, N):
    rho_squared = rho**2
    pe = 0.6745 * (1 - rho_squared) / (np.sqrt(N) * (1 + 1.086*rho_squared + 0.13*rho_squared**2 + 0.002*rho_squared**3))
    return pe

# Example usage:
rho = 0.8   # Replace this with your desired correlation coefficient (rho) value
N = 100     # Replace this with your desired sample size (N)

# Calculate the probable error for ρ
prob_error_rho = probable_error_spearman(rho, N)
print(f"Probable Error for ρ = {prob_error_rho:.4f}")


# Answer: Probable Error for ρ = 0.0139
