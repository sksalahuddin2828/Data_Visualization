import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Define functions
x = np.linspace(-5, 5, 100)
f = lambda x: x**2
g = lambda x: 2*x

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(0, 25)
line_f, = ax.plot([], [], label='f(x)')
line_g, = ax.plot([], [], label='g(x)')
ax.legend()

def init():
    line_f.set_data([], [])
    line_g.set_data([], [])
    return line_f, line_g

def animate(i):
    y_f = f(x[:i])
    y_g = g(x[:i])
    line_f.set_data(x[:i], y_f)
    line_g.set_data(x[:i], y_g)
    return line_f, line_g

anim = FuncAnimation(fig, animate, init_func=init, frames=len(x), interval=100, blit=True)
plt.close()

HTML(anim.to_jshtml())
