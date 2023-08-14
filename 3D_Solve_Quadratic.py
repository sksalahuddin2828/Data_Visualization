# If ax2+bx+c=0, then x=−b±b2−4ac√2a

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
from sympy.plotting import plot3d

a_list = [1, 2, 3]
b_list = [2, -1, 4]
c_list = [1, 5, -2]

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        return root1, root2

data = {'a': [], 'b': [], 'c': [], 'roots': []}

for a_val, b_val, c_val in zip(a_list, b_list, c_list):
    roots = solve_quadratic(a_val, b_val, c_val)
    if isinstance(roots, tuple):
        data['a'].append(a_val)
        data['b'].append(b_val)
        data['c'].append(c_val)
        data['roots'].append(roots)

df = pd.DataFrame(data)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['a'], df['b'], df['roots'][0], c='r', marker='o')  # Plotting only the first root for visualization
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('Roots')
plt.show()

x = sp.Symbol('x')
equation = x**2 + sp.Symbol('b')*x + sp.Symbol('c')
sp.plot(equation.subs({sp.Symbol('b'): b_list[0], sp.Symbol('c'): c_list[0]}), (x, -10, 10), xlabel='x', ylabel='Equation Value')

a_vals = np.linspace(-10, 10, 100)
b_vals = np.linspace(-10, 10, 100)
a_grid, b_grid = np.meshgrid(a_vals, b_vals)
c_grid = -a_grid - b_grid

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(a_grid, b_grid, c_grid, cmap='viridis')
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')
plt.show()
