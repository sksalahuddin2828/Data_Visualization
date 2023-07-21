import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data points
x_values = np.array([5, -2])
y_values = np.array([3, 4])

# Create a meshgrid of slope and intercept values for visualization
a_vals = np.linspace(-10, 10, 100)
b_vals = np.linspace(-10, 10, 100)
A, B = np.meshgrid(a_vals, b_vals)

# Calculate the corresponding f(x) values for each combination of a and b
F_X = A[..., None] * x_values + B[..., None]

# Calculate the squared error for each data point
error = np.sum((F_X - y_values)**2, axis=-1)

# Find the minimum error index
min_error_idx = np.unravel_index(np.argmin(error), error.shape)
optimal_a = A[min_error_idx]
optimal_b = B[min_error_idx]

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the error surface
ax.plot_surface(A, B, error, cmap='viridis', alpha=0.8)

# Mark the minimum error point (optimal a and b values)
ax.scatter(optimal_a, optimal_b, error[min_error_idx], color='red', s=100, label='Optimal (a, b)')

# Set labels and title
ax.set_xlabel('Slope (a)')
ax.set_ylabel('Intercept (b)')
ax.set_zlabel('Squared Error')
ax.set_title('Optimization for Linear Equation f(x) = ax + b')

# Add annotations for the optimal (a, b) values
ax.text(optimal_a, optimal_b, error[min_error_idx], "Optimal (a, b)", color='red', fontsize=12, ha='left')

plt.legend()
plt.show()

# Print the optimal values of a and b
print("Optimal value of a:", optimal_a)
print("Optimal value of b:", optimal_b)
