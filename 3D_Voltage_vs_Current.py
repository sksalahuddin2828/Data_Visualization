import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import torch
import sklearn
import scipy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df_current = pd.DataFrame({'Time': t, 'Current': I})

fig_current = px.line(df_current, x='Time', y='Current', title='AC Current vs Time')
fig_current.update_xaxes(title_text='Time')
fig_current.update_yaxes(title_text='Current')

fig_current.show()

voltage_values = np.linspace(0, V0, 1000)
resistance_values = np.linspace(1, 100, 1000)  # Varying resistance

current_values = voltage_values / resistance_values

df_voltage_current = pd.DataFrame({'Voltage': voltage_values, 'Current': current_values})

fig_voltage_current = px.scatter(df_voltage_current, x='Voltage', y='Current', title='Voltage vs Current')
fig_voltage_current.update_xaxes(title_text='Voltage')
fig_voltage_current.update_yaxes(title_text='Current')

fig_voltage_current.show()

x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.sin(np.sqrt(X**2 + Y**2))

df_surface = pd.DataFrame({'X': X.ravel(), 'Y': Y.ravel(), 'Z': Z.ravel()})

fig_surface = px.scatter_3d(df_surface, x='X', y='Y', z='Z', title='3D Surface Plot')
fig_surface.update_layout(scene=dict(zaxis_title='Z'))

fig_surface.show()


