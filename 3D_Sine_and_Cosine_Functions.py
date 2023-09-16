import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import matplotlib.pyplot as plt
import torch
import sklearn
import scipy

def calculate_trig_values(theta_degrees):
    theta_radians = np.deg2rad(theta_degrees)
    sin_theta = np.sin(theta_radians)
    cos_theta = np.cos(theta_radians)
    tan_theta = np.tan(theta_radians)
    cosec_theta = 1 / sin_theta
    sec_theta = 1 / cos_theta
    cot_theta = 1 / tan_theta
    return sin_theta, cos_theta, tan_theta, cosec_theta, sec_theta, cot_theta

# Example usage:
sin_theta, cos_theta, tan_theta, cosec_theta, sec_theta, cot_theta = calculate_trig_values(30)

theta_degrees = np.linspace(0, 360, 360)
sin_values = np.sin(np.deg2rad(theta_degrees))
cos_values = np.cos(np.deg2rad(theta_degrees))

df = pd.DataFrame({'Theta': theta_degrees, 'sin(Theta)': sin_values, 'cos(Theta)': cos_values})

fig = px.line(df, x='Theta', y=['sin(Theta)', 'cos(Theta)'], title='Sine and Cosine Functions')
fig.update_xaxes(title='Angle (Degrees)')
fig.update_yaxes(title='Value')
fig.show()

x = sp.symbols('x')
expr = sp.sin(x)**2 + sp.cos(x)**2
simplified_expr = sp.simplify(expr)
print(simplified_expr)
