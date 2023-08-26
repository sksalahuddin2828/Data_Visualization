import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
x_vals = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x_vals, np.sin(x_vals))

def update(frame):
    line.set_ydata(np.sin(x_vals + frame * 0.1))
    return line,

ani = FuncAnimation(fig, update, frames=50, blit=True)
plt.show()
