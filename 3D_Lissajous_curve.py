import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for Lissajous curve
A = 1.0
B = 2.0
delta = np.pi / 2  # Phase difference

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], lw=2)

# Animation initialization function
def init():
    line.set_data([], [])
    return line,

# Animation update function
def animate(t):
    t_vals = np.linspace(0, 2 * np.pi, 500)
    x_vals = A * np.sin(3 * t_vals + delta * np.cos(2 * t))
    y_vals = B * np.sin(2 * t_vals)
    line.set_data(x_vals, y_vals)
    return line,

# Create animation
ani = FuncAnimation(fig, animate, init_func=init, frames=np.linspace(0, 2 * np.pi, 100), interval=50, blit=True)

# Save animation as a GIF
ani.save('lissajous_animation.gif', writer='pillow', fps=20)

# Show the animation
plt.show()
