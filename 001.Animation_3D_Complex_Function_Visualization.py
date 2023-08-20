import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from mpl_toolkits.mplot3d import Axes3D

# Define the function to be visualized
def complex_function(x_val, a_val):
    return np.exp(-a_val) * np.sin(x_val) * np.sqrt(a_val**2 + x_val**2)

# Create x and a values
x_vals = np.linspace(0, 5, 100)
a_vals = np.linspace(0.1, 5, 50)

# Create meshgrid
X, A = np.meshgrid(x_vals, a_vals)
Z = complex_function(X, A)

# Create a DataFrame
df = pd.DataFrame({'x': X.flatten(), 'a': A.flatten(), 'value': Z.flatten()})

# Create an interactive 3D surface plot with dynamic color transitions
fig = px.scatter_3d(df, x='x', y='a', z='value', opacity=0.7,
                    title='Complex 3D Function Visualization with Animation',
                    labels={'value': 'Function Value'},
                    color='value',
                    color_continuous_scale=px.colors.sequential.Viridis,
                    animation_frame='a')
fig.update_layout(scene=dict(zaxis_title='Function Value'))

# Create an interactive animated plot with dynamic color and marker size
fig_animation = go.Figure()

for a_val in a_vals:
    y_vals = complex_function(x_vals, a_val)
    color_scale = np.log10(np.abs(y_vals) + 1)
    marker_size = 20 * np.abs(y_vals) / np.max(np.abs(y_vals))
    fig_animation.add_trace(go.Scatter(x=x_vals, y=y_vals, name=f'a = {a_val:.2f}', 
                             mode='markers', marker=dict(size=marker_size, color=color_scale),
                             text=[f'x = {x:.2f}<br>a = {a_val:.2f}<br>Value = {y:.2f}' for x, y in zip(x_vals, y_vals)],
                             hoverinfo='text'))

fig_animation.update_layout(title='Interactive Function Animation with Color and Marker Size',
                  xaxis_title='x', yaxis_title='Function Value')
fig_animation.update_xaxes(range=[0, 5])
fig_animation.update_yaxes(range=[-10, 10])
frames=[go.Frame(data=[go.Scatter(x=x_vals, y=complex_function(x_vals, a_val),
                                  mode='markers', marker=dict(size=20 * np.abs(complex_function(x_vals, a_val)) / np.max(np.abs(complex_function(x_vals, a_val))),
                                                              color=np.log10(np.abs(complex_function(x_vals, a_val)) + 1),
                                                              colorscale='Viridis'),
                                  text=[f'x = {x:.2f}<br>a = {a_val:.2f}<br>Value = {y:.2f}' for x, y in zip(x_vals, complex_function(x_vals, a_val))],
                                  hoverinfo='text')]
                 , layout=go.Layout(title=f'a = {a_val:.2f}', xaxis=dict(range=[0, 5]), yaxis=dict(range=[-10, 10])))
        for a_val in a_vals]
fig_animation.frames=frames

# Add slider for animation speed control
fig_animation.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                method='animate', args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True, mode='immediate')])])],
                            sliders=[dict(currentvalue=dict(prefix='Speed: ', visible=True), steps=[dict(args=['frame.duration', 100],
                                                                                                      label='Slow',
                                                                                                      method='animate'),
                                                                                                     dict(args=['frame.duration', 50],
                                                                                                      label='Moderate',
                                                                                                      method='animate'),
                                                                                                     dict(args=['frame.duration', 10],
                                                                                                      label='Fast',
                                                                                                      method='animate')])])
fig_animation.show()
