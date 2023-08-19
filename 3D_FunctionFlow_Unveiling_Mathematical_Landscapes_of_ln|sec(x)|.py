import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from IPython.display import display, HTML

# Matplotlib Visualization
x_vals = np.linspace(-2*np.pi, 2*np.pi, 400)
y_vals = np.log(np.abs(1/np.cos(x_vals)))

df = pd.DataFrame({'x': x_vals, 'y': y_vals})
df['curve'] = np.floor(df['x'] / (np.pi / 2))  # Group by quarter periods

# Plotly Express Line Plot
fig = px.line(df, x='x', y='y', color='curve', title="Multiple Curves of ln|sec(x)|")
display(HTML(fig.to_html()))

# Plotly Express Area Plot
fig = px.area(df, x='x', y='y', title="Filled Area Under ln|sec(x)|")
display(HTML(fig.to_html()))

# Plotly Express Line Plot with Annotations
fig = px.line(df, x='x', y='y', title="ln|sec(x)| with Annotations")
fig.update_layout(annotations=[
    dict(x=np.pi/2, y=5, text="π/2", showarrow=True),
    dict(x=np.pi, y=5, text="π", showarrow=True),
    dict(x=-np.pi/2, y=5, text="-π/2", showarrow=True),
    dict(x=-np.pi, y=5, text="-π", showarrow=True)
])
display(HTML(fig.to_html()))

# 3D Scatter Plot
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.log(np.abs(1/np.cos(X)))
df_3d = pd.DataFrame({'x': X.flatten(), 'y': Y.flatten(), 'z': Z.flatten()})

fig = px.scatter_3d(df_3d, x='x', y='y', z='z', title="3D Scatter Plot of ln|sec(x)|")
display(HTML(fig.to_html()))

# Plotly Surface Plot
fig = go.Figure(data=[go.Surface(z=Z, colorscale='Viridis')])
fig.update_layout(scene=dict(zaxis_title='ln|sec(x)|'), title="Surface Plot with Contours of ln|sec(x)|")
display(HTML(fig.to_html()))
