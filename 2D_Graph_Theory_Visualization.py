import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/10))  # Animation parameter i controls phase shift
    return line,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=100)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sympy as sp

fig, ax = plt.subplots()
t_values = np.linspace(0, 2 * np.pi, 100)
t = sp.symbols('t')
expr = sp.sin(t) + sp.cos(2 * t)
expr_lambdified = sp.lambdify(t, expr, modules=["numpy"])

line, = ax.plot(t_values, expr_lambdified(t_values))

def animate(i):
    line.set_ydata(expr_lambdified(t_values + i/10))  # Animation parameter i controls phase shift
    return line,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=100)
plt.show()
