import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import root

# Define the functions f(x) and g(x)
def f(x):
    return 2 + np.sqrt(x + 1) + np.cbrt(1 - x)

def g(x):
    return np.log((np.log(1 - x) / np.log(1 + x)) ** 2) / np.log(1 - x ** 2)

# Generate x and y values
x_values = np.linspace(-0.99, 0.99, 100)
y_values_f = f(x_values)
y_values_g = g(x_values)

# Create a meshgrid for 3D plotting
X, Y = np.meshgrid(x_values, x_values)
Z_f = np.array([[f(x) for x in row] for row in X])
Z_g = np.array([[g(x) for x in row] for row in X])

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot f(x) as a surface
ax.plot_surface(X, Y, Z_f, cmap='viridis', alpha=0.7, label='f(x) = 2 + sqrt(x+1) + cbrt(1 - x)')

# Plot g(x) as a surface
ax.plot_surface(X, Y, Z_g, cmap='plasma', alpha=0.7, label='g(x) = log((log(1 - x) / log(1 + x))^2) / log(1 - x^2)')

# Function to solve the equation f(x) - g(y) = 0
def equation_to_solve(xy):
    x, y = xy
    return [f(x) - g(y), 0]  # The second element of the array is a dummy value (0).

# Find the intersection point (root) using scipy.optimize.root
result = root(equation_to_solve, [0, 0])
if result.success:
    root_x, root_y = result.x
    ax.scatter(root_x, root_y, f(root_x), color='red', s=100, label='Root (x={:.3f}, y={:.3f})'.format(root_x, root_y))
else:
    print("Intersection point not found.")

# Set labels and title for the 3D plot
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Visualization of f(x) and g(x) in 3D')

# Create a 2D plot to show the legend
dummy_plot = plt.figure().add_subplot(111)
dummy_plot.legend()

# Show the plot
plt.show()
