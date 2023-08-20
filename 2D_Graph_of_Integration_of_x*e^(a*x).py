import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sympy import symbols, exp

# Define symbolic variables
x, a = symbols('x a')

# Define the expression and integrate
expression = x * exp(a * x)
integral_result = (1 / a**2) * (a * x - 1) * exp(a * x)

# Define the x values for plotting
x_values = np.linspace(0, 2, 400)

# Create the figure and axis
fig, ax = plt.subplots()

# Create a line plot for the original function
line_original, = ax.plot(x_values, x_values * np.exp(1 * x_values), label='Original Function')

# Create a line plot for the integrated result (initially empty)
line_integrated, = ax.plot([], [], label='Integrated Result')

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Integration of x * e^(a * x)')
ax.legend()

# Define initialization function for animation
def init():
    line_integrated.set_data([], [])
    return line_integrated,

# Define update function for animation
def update(frame):
    a_val = (frame + 1) / 20  # Incremental 'a' values for animation
    integrated_y = (np.exp(a_val * x_values) / (a_val**2)) * (a_val * x_values - 1)
    line_integrated.set_data(x_values, integrated_y)
    return line_integrated,

# Create the animation
ani = FuncAnimation(fig, update, frames=20, init_func=init, blit=True)

# Display the animation
plt.show()
