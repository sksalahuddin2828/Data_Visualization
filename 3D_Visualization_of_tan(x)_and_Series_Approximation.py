import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x_vals = np.linspace(-10, 10, 300)

# Calculate tan(x) and the series approximation
tan_x = np.tan(x_vals)
series_approx = x_vals + (x_vals ** 3) / 3 + (2 * x_vals ** 5) / 15

# Create a figure with subplots
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, projection='3d')

# Plot the tan(x) function and the series approximation
ax1.plot(x_vals, tan_x, label='tan(x)')
ax1.plot(x_vals, series_approx, label='Series Approximation')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('tan(x) vs. Series Approximation')
ax1.legend()

# Create a meshgrid for the 3D visualization
X, Y = np.meshgrid(x_vals, x_vals)
Z_tan_x = np.tan(X)
Z_series_approx = X + (X ** 3) / 3 + (2 * X ** 5) / 15

# Plot the 3D surface for tan(x)
ax2.plot_surface(X, Y, Z_tan_x, cmap='viridis', alpha=0.7, label='tan(x)')

# Plot the 3D surface for the series approximation
ax2.plot_surface(X, Y, Z_series_approx, cmap='plasma', alpha=0.7, label='Series Approximation')

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_title('3D Visualization of tan(x) and Series Approximation')

plt.tight_layout()
plt.show()
