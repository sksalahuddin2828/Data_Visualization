import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import torch
import sklearn
import scipy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 1, 1000)  # Time values
f = 50  # Frequency (Hz)
I0 = 1  # Peak current

I = I0 * np.sin(2 * np.pi * f * t)

V0 = 230  # Peak voltage
R = 50   # Resistance

P_ave = 0.5 * I0 * V0

df = pd.DataFrame({'Time': t, 'Current': I})
fig = px.line(df, x='Time', y='Current', title='AC Current vs Time')
fig.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z)
plt.show()

sp.init_printing()  # Initialize pretty printing for SymPy
I_eq = sp.Eq(sp.Symbol('I'), I0 * sp.sin(2 * sp.pi * f * sp.Symbol('t')))
P_eq = sp.Eq(sp.Symbol('P_{ave}'), 0.5 * I0 * V0)

display(I_eq)
display(P_eq)
