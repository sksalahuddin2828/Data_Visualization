import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a, x = np.linspace(0.1, 2*np.pi, 100), np.linspace(0, 2*np.pi, 400)
X, A = np.meshgrid(x, a)
Y = np.sin(2*A*X)**2

fig, ax = plt.subplots()
line = ax.plot(x, Y[0, :])[0]

def animate(frame):
    line.set_ydata(Y[frame, :])
    ax.set_title(f'Mathematical Dance: a = {a[frame]:.2f}')
    return line,

ani = FuncAnimation(fig, animate, frames=len(a), interval=100)
plt.show()


import ipywidgets as widgets
from IPython.display import display

def update_plot(a):
    plt.figure(figsize=(8, 4))
    plt.plot(x, np.sin(2*a*x)**2)
    plt.title(f'Integral Expression: a = {a:.2f}')
    plt.xlabel('x')
    plt.ylabel('Expression Value')
    plt.grid()
    plt.show()

a_slider = widgets.FloatSlider(value=0.1, min=0.1, max=2*np.pi, step=0.1, description='a:')
widgets.interactive(update_plot, a=a_slider)
