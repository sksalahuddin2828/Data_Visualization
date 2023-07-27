import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sympy import symbols, sqrt, cbrt, log, tanh, sin, cos, exp, lambdify, solve, Eq

# Define the functions f(x) and g(x) using SymPy
x_sym = symbols('x')
f_sym = 2 + sqrt(x_sym + 1) + cbrt(1 - x_sym)
g_sym = log((log(1 - x_sym) / log(1 + x_sym)) ** 2) / log(1 - x_sym ** 2)

# Additional functions
h_sym = sin(x_sym) + cos(x_sym)
k_sym = exp(x_sym) + x_sym**2
m_sym = tanh(x_sym)

# Convert the SymPy expressions to NumPy functions for evaluation
f = lambdify(x_sym, f_sym, 'numpy')
g = lambdify(x_sym, g_sym, 'numpy')
h = lambdify(x_sym, h_sym, 'numpy')
k = lambdify(x_sym, k_sym, 'numpy')
m = lambdify(x_sym, m_sym, 'numpy')

# Generate x and y values
x_values = np.linspace(0.001, 0.99, 100)
y_values_f = f(x_values)
y_values_g = g(x_values)
y_values_h = h(x_values)
y_values_k = k(x_values)
y_values_m = m(x_values)

# Create a meshgrid for 3D plotting
X, Y = np.meshgrid(x_values, x_values)
Z_f = f(X + Y * 1j).real
Z_g = g(X + Y * 1j).real
Z_h = h(X + Y * 1j).real
Z_k = k(X + Y * 1j).real
Z_m = m(X + Y * 1j).real

# Calculate the intersection point (root) of f(x) and g(x) using numerical methods
def find_intersection(func1, func2, x_values):
    tol = 1e-9
    for x in x_values:
        y1 = func1(x)
        y2 = func2(x)
        if abs(y1 - y2) < tol:
            return x
    return None

root = find_intersection(f, g, x_values)

if root is not None:
    # Create 3D scatter plot for the root
    df_root = pd.DataFrame({'X': [root], 'Y': [root], 'Z': [f(root)]})
else:
    # No valid intersection point found
    df_root = pd.DataFrame({'X': [], 'Y': [], 'Z': []})

# Create DataFrame for 3D plotting
df_f = pd.DataFrame({'X': X.flatten(), 'Y': Y.flatten(), 'Z': Z_f.flatten()})
df_g = pd.DataFrame({'X': X.flatten(), 'Y': Y.flatten(), 'Z': Z_g.flatten()})
df_h = pd.DataFrame({'X': X.flatten(), 'Y': Y.flatten(), 'Z': Z_h.flatten()})
df_k = pd.DataFrame({'X': X.flatten(), 'Y': Y.flatten(), 'Z': Z_k.flatten()})
df_m = pd.DataFrame({'X': X.flatten(), 'Y': Y.flatten(), 'Z': Z_m.flatten()})

# Create 3D plot using Plotly
fig = go.Figure()

fig.add_trace(go.Surface(z=Z_f, x=X, y=Y, colorscale='viridis', name='f(x) = 2 + sqrt(x+1) + cbrt(1 - x)'))
fig.add_trace(go.Surface(z=Z_g, x=X, y=Y, colorscale='plasma', name='g(x) = log((log(1 - x) / log(1 + x))^2) / log(1 - x^2)'))
fig.add_trace(go.Surface(z=Z_h, x=X, y=Y, colorscale='magma', name='h(x) = sin(x) + cos(x)'))
fig.add_trace(go.Surface(z=Z_k, x=X, y=Y, colorscale='inferno', name='k(x) = exp(x) + x^2'))
fig.add_trace(go.Surface(z=Z_m, x=X, y=Y, colorscale='cividis', name='m(x) = tanh(x)'))

if root is not None:
    fig.add_trace(go.Scatter3d(x=df_root['X'], y=df_root['Y'], z=df_root['Z'], mode='markers', marker=dict(size=5, color='red'), name='Root (x={:.3f})'.format(float(root))))

# Update layout for title, axes labels, and colorbar
fig.update_layout(
    title='Visualization of Mathematical Functions in 3D',
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z'
    ),
    scene_camera=dict(eye=dict(x=1.6, y=-1.6, z=0.8)),
    legend=dict(x=0, y=1, traceorder='normal'),
    coloraxis_colorbar=dict(title='Function Value')
)

# Add contour lines for f(x) and g(x)
fig.add_trace(go.Surface(z=Z_h, x=X, y=Y, colorscale='magma', name='h(x) = sin(x) + cos(x)', showscale=False, visible=False))
fig.update_layout(
    updatemenus=[
        dict(
            type='buttons',
            showactive=True,
            buttons=list([
                dict(label='f(x)',
                     method='update',
                     args=[{'visible': [True, False, False, False, False, False]},
                           {'title': 'Visualization of f(x) in 3D', 'scene_coloraxis_cmin': df_f['Z'].min(), 'scene_coloraxis_cmax': df_f['Z'].max()}]),
                dict(label='g(x)',
                     method='update',
                     args=[{'visible': [False, True, False, False, False, False]},
                           {'title': 'Visualization of g(x) in 3D', 'scene_coloraxis_cmin': df_g['Z'].min(), 'scene_coloraxis_cmax': df_g['Z'].max()}]),
                dict(label='h(x)',
                     method='update',
                     args=[{'visible': [False, False, True, False, False, False]},
                           {'title': 'Visualization of h(x) in 3D', 'scene_coloraxis_cmin': df_h['Z'].min(), 'scene_coloraxis_cmax': df_h['Z'].max()}]),
                dict(label='k(x)',
                     method='update',
                     args=[{'visible': [False, False, False, True, False, False]},
                           {'title': 'Visualization of k(x) in 3D', 'scene_coloraxis_cmin': df_k['Z'].min(), 'scene_coloraxis_cmax': df_k['Z'].max()}]),
                dict(label='m(x)',
                     method='update',
                     args=[{'visible': [False, False, False, False, True, True]},
                           {'title': 'Visualization of m(x) in 3D', 'scene_coloraxis_cmin': df_m['Z'].min(), 'scene_coloraxis_cmax': df_m['Z'].max()}])
            ])
        )
    ]
)

# Show the plot
fig.show()
