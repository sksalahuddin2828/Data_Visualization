import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the equation and its solutions
def equation(x):
    return 3*x**2 - 5*x + 2

solutions = np.roots([3, -5, 2])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
x_vals = np.linspace(-2, 4, 400)
y_vals = equation(x_vals)

# Plot the parabola
ax.plot(x_vals, y_vals, label='3x^2 - 5x + 2', color='blue')
ax.axhline(0, color='black', linewidth=0.5)

# Annotate the solutions
for solution in solutions:
    ax.annotate(f'x = {solution:.2f}', xy=(solution, 0), xytext=(solution, -5),
                textcoords='offset points', arrowprops=dict(facecolor='black', arrowstyle='->'))

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Visualizing Equation: 3x^2 - 5x + 2 = 0')

# Animation initialization
line, = ax.plot([], [], 'ro', markersize=10)
def init():
    line.set_data([], [])
    return line,

# Animation update
def animate(i):
    x = solutions[i]
    y = equation(x)
    line.set_data(x, y)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(solutions),
                              interval=1500, blit=True)

# Show the animation
plt.show()
