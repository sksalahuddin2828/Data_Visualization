import matplotlib.pyplot as plt
import numpy as np

alpha_vals = np.linspace(0, 2 * np.pi, 100)
beta_vals = np.linspace(0, 2 * np.pi, 100)

# Calculate left and right sides of the identity
left_side_vals = np.cos(alpha_vals) + np.cos(beta_vals)
right_side_vals = 2 * np.cos(0.5 * (alpha_vals + beta_vals)) * np.cos(0.5 * (alpha_vals - beta_vals))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(alpha_vals, left_side_vals, label='cos(α) + cos(β)')
plt.plot(alpha_vals, right_side_vals, label='2cos(1/2(α+β))cos(1/2(α-β))')
plt.xlabel('α')
plt.ylabel('Value')
plt.title('Trigonometric Identity Visualization')
plt.legend()
plt.grid(True)
plt.show()
