import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# Create figure and axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Set initial degree for the polynomial
initial_degree = 2

# Function to update the plot based on the degree
def update(val):
    degree = int(s_degree.val)
    plot_polynomial(degree)

# Create a slider for the degree of the polynomial
ax_degree = plt.axes([0.2, 0.02, 0.65, 0.03])
s_degree = Slider(ax_degree, 'Degree', 2, 10, valinit=initial_degree, valstep=1)
s_degree.on_changed(update)

# Function to plot the polynomial
def plot_polynomial(degree):
    # Clear previous plot
    ax.clear()

    # Generate random coefficients for the polynomial
    coefficients = np.random.randn(degree + 1)

    # Solve the polynomial roots
    roots = np.roots(coefficients)

    # Plot the roots in 3D space
    ax.scatter(roots.real, roots.imag, np.zeros_like(roots), c='red', s=100)

    # Set plot properties
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_zlabel('Degree')
    ax.set_title(f'Roots of Polynomial (Degree: {degree})')

    # Show the plot
    plt.draw()

# Initial plot
plot_polynomial(initial_degree)

# Show the plot
plt.show()
