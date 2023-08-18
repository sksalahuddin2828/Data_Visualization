import numpy as np
import pandas as pd
import dask
import plotly
import bokeh
import holoviews as hv
import sympy as sp
import torch
import sklearn
import keras
import scipy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = sp.symbols('x')
f = x**2
g = 2*x

integral_f = sp.integrate(f, x)
integral_g = sp.integrate(g, x)
sum_integrals = integral_f + integral_g

x_vals = np.linspace(-10, 10, 100)
f_vals = x_vals**2
g_vals = 2 * x_vals

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_vals, f_vals, g_vals)
ax.set_xlabel('X')
ax.set_ylabel('f(x)')
ax.set_zlabel('g(x)')
plt.title('3D Visualization of f(x) and g(x)')
plt.show()

import plotly.express as px

data = pd.DataFrame({'x': x_vals, 'f(x)': f_vals, 'g(x)': g_vals})
fig = px.line(data, x='x', y=['f(x)', 'g(x)'], title='f(x) and g(x) Plot')
fig.show()
