import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Given data points
data_points = np.array([[-1, 0], [1, 2], [2, 3]])

# Extract independent (X) and dependent (y) variables
X = data_points[:, 0]
y = data_points[:, 1]

# Function to calculate SSR (Sum of Squares due to Regression)
def calculate_ssr(y, yhat):
    return np.sum((yhat - np.mean(y))**2)

# Create a meshgrid of slope and intercept values for visualization
slope_vals = np.linspace(-1, 4, 100)
intercept_vals = np.linspace(-1, 4, 100)
S, I = np.meshgrid(slope_vals, intercept_vals)

# Initialize arrays to store SSR values and fitted lines
ssr_vals = np.zeros_like(S)
fit_lines = np.zeros((3, 100))

# Calculate SSR for all combinations of slope and intercept
for i in range(len(slope_vals)):
    for j in range(len(intercept_vals)):
        fit_lines[:, i] = slope_vals[i] * X + intercept_vals[j]
        ssr_vals[j, i] = calculate_ssr(y, fit_lines[:, i])

# Perform gradient descent optimization to find the best fit line
alpha = 0.05  # Learning rate
epochs = 50
slope = 0
intercept = 0
optimal_slopes = [slope]
optimal_intercepts = [intercept]
for _ in range(epochs):
    yhat = slope * X + intercept
    slope -= alpha * np.mean((yhat - y) * X)
    intercept -= alpha * np.mean(yhat - y)
    optimal_slopes.append(slope)
    optimal_intercepts.append(intercept)

# Final best-fit line
final_fit_line = slope_vals[-1] * X + intercept_vals[-1]

# Create an animated 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the meshgrid
ax.plot_surface(S, I, ssr_vals, alpha=0.6, cmap='viridis')

# Plot the history of the regression lines during optimization in blue
for i in range(epochs):
    y_vals = optimal_slopes[i] * X + optimal_intercepts[i]
    ax.scatter(optimal_slopes[i], optimal_intercepts[i], calculate_ssr(y, y_vals), color='blue', alpha=0.7)

# Plot the optimal regression line in red
ax.scatter(slope_vals[-1], intercept_vals[-1], calculate_ssr(y, final_fit_line), color='red', s=100, label='Optimal Regression Line')

# Set labels and title
ax.set_xlabel('Slope (b)')
ax.set_ylabel('Intercept (a)')
ax.set_zlabel('SSR (Sum of Squares due to Regression)')
ax.set_title('Gradient Descent Optimization for Linear Regression')

# Add a color bar to represent SSR values
cbar = plt.colorbar(ax.plot_surface(S, I, ssr_vals, alpha=0.6, cmap='viridis'))
cbar.set_label('SSR Values', rotation=270, labelpad=20)

# Add annotations for the optimal slope and intercept values
ax.text(slope_vals[-1], intercept_vals[-1], calculate_ssr(y, final_fit_line), "Optimal", color='red', fontsize=12, ha='left')

# Function to update the plot during animation
def update_plot(i):
    ax.view_init(elev=20, azim=i*5)
    return fig,

# Create the animation
ani = FuncAnimation(fig, update_plot, frames=180, interval=50, blit=True)

# Save the animation to a file (you can view it in a video player)
# ani.save('linear_regression_optimization.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.legend()
plt.show()
