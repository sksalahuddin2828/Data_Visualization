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

# Create an interactive 3D surface plot with plotly
fig = px.scatter_3d(df, x='x', y='a', z='value', opacity=0.7,
                    title='Complex 3D Function Visualization',
                    labels={'value': 'Function Value'},
                    color='value',
                    color_continuous_scale=px.colors.sequential.Viridis)
fig.update_traces(marker=dict(size=3))
fig.update_layout(scene=dict(zaxis_title='Function Value'))
fig.show()

# Create a more intricate 3D plot using matplotlib
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, A, Z, cmap='viridis', linewidth=0, antialiased=True)
ax.set_xlabel('x')
ax.set_ylabel('a')
ax.set_zlabel('Function Value')
ax.set_title('Intricate 3D Function Visualization')
plt.show()

# Create an interactive animated plot using plotly
fig = go.Figure()

for a_val in a_vals:
    y_vals = complex_function(x_vals, a_val)
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, name=f'a = {a_val:.2f}'))

fig.update_layout(title='Interactive Function Animation',
                  xaxis_title='x', yaxis_title='Function Value')
fig.update_xaxes(range=[0, 5])
fig.update_yaxes(range=[-10, 10])
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                method='animate', args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True, mode='immediate')])])])
frames=[go.Frame(data=[go.Scatter(x=x_vals, y=complex_function(x_vals, a_val))],
                 layout=go.Layout(title=f'a = {a_val:.2f}', xaxis=dict(range=[0, 5]), yaxis=dict(range=[-10, 10])))
        for a_val in a_vals]
fig.frames=frames

fig.show()
