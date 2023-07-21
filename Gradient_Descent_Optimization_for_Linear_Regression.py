import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Function to calculate SSR (Sum of Squares due to Regression)
def calculate_ssr(y, yhat):
    return np.sum((yhat - np.mean(y))**2)

# Generate synthetic data for demonstration
np.random.seed(42)
X = np.random.rand(50) * 10
y = 2.5 * X + 5 + np.random.randn(50) * 2

# Create a meshgrid of slope and intercept values for visualization
slope_vals = np.linspace(1, 4, 100)
intercept_vals = np.linspace(0, 10, 100)
S, I = np.meshgrid(slope_vals, intercept_vals)

# Initialize arrays to store SSR values and fitted lines
ssr_vals = np.zeros_like(S)
fit_lines = np.zeros((50, 100))

# Calculate SSR for all combinations of slope and intercept
for i in range(len(slope_vals)):
    for j in range(len(intercept_vals)):
        fit_lines[:, i] = slope_vals[i] * X + intercept_vals[j]
        ssr_vals[j, i] = calculate_ssr(y, fit_lines[:, i])

# Perform gradient descent optimization to find the best fit line
# You can use more advanced optimization methods in real-world scenarios
alpha = 0.001  # Learning rate
epochs = 500
slope = 0
intercept = 0
for _ in range(epochs):
    yhat = slope * X + intercept
    slope -= alpha * np.mean((yhat - y) * X)
    intercept -= alpha * np.mean(yhat - y)

# Final best-fit line
final_fit_line = slope * X + intercept

# Create an animated 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the meshgrid
ax.plot_surface(S, I, ssr_vals, alpha=0.6, cmap='viridis')

# Plot the optimal regression line in red
ax.scatter(slope, intercept, calculate_ssr(y, final_fit_line), color='red', s=100, label='Optimal Regression Line')

# Plot the history of the regression lines during optimization in blue
for i in range(epochs):
    ax.scatter(slope_vals, intercept_vals, ssr_vals[:, i], color='blue', alpha=0.1)

# Set labels and title
ax.set_xlabel('Slope (b)')
ax.set_ylabel('Intercept (a)')
ax.set_zlabel('SSR (Sum of Squares due to Regression)')
ax.set_title('Gradient Descent Optimization for Linear Regression')

# Add a color bar to represent SSR values
cbar = plt.colorbar(ax.plot_surface(S, I, ssr_vals, alpha=0.6, cmap='viridis'))
cbar.set_label('SSR Values', rotation=270, labelpad=20)

# Add annotations for the optimal slope and intercept values
ax.text(slope, intercept, calculate_ssr(y, final_fit_line), "Optimal", color='red', fontsize=12, ha='left')

# Function to update the plot during animation
def update_plot(i):
    ax.view_init(elev=20, azim=i*2)
    return fig,

# Create the animation
ani = FuncAnimation(fig, update_plot, frames=180, interval=50, blit=True)

# Save the animation to a file (you can view it in a video player)
ani.save('linear_regression_optimization.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.legend()
plt.show()
