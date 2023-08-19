import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from scipy.special import gamma

# Matplotlib Visualization
x_vals = np.linspace(-2*np.pi, 2*np.pi, 400)
y_vals = np.log(np.abs(1/np.cos(x_vals)))

df = pd.DataFrame({'x': x_vals, 'y': y_vals})
df['curve'] = np.floor(df['x'] / (np.pi / 2))  # Group by quarter periods

# Plotly Express Line Plot
fig1 = px.line(df, x='x', y='y', color='curve', title="Multiple Curves of ln|sec(x)|")
display(HTML(fig1.to_html()))

# Plotly Express Area Plot
fig2 = px.area(df, x='x', y='y', title="Filled Area Under ln|sec(x)|")
display(HTML(fig2.to_html()))

# Plotly Express Line Plot with Annotations
fig3 = px.line(df, x='x', y='y', title="ln|sec(x)| with Annotations")
fig3.update_layout(annotations=[
    dict(x=np.pi/2, y=5, text="π/2", showarrow=True),
    dict(x=np.pi, y=5, text="π", showarrow=True),
    dict(x=-np.pi/2, y=5, text="-π/2", showarrow=True),
    dict(x=-np.pi, y=5, text="-π", showarrow=True)
])
display(HTML(fig3.to_html()))

# Custom Mathematical Function and Plot
def custom_function(x):
    return x**2 * np.sin(x) + gamma(x)

y_vals_custom = custom_function(x_vals)
df_custom = pd.DataFrame({'x': x_vals, 'y': y_vals_custom})
fig4 = px.line(df_custom, x='x', y='y', title="Custom Function: x^2 * sin(x) + Γ(x)")
display(HTML(fig4.to_html()))

# 3D Surface Plot with Contours
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.log(np.abs(1/np.cos(X)))
fig5 = make_subplots(rows=1, cols=2, specs=[[{'type': 'surface'}, {'type': 'contour'}]])

fig5.add_trace(go.Surface(z=Z, colorscale='Viridis'), row=1, col=1)
fig5.add_trace(go.Contour(z=Z, colorscale='Viridis'), row=1, col=2)

fig5.update_layout(title_text="3D Surface Plot with Contours of ln|sec(x)|")
display(HTML(fig5.to_html()))

# Animation of a Parametric Function
t_vals = np.linspace(0, 10, 200)
x_anim = np.sin(t_vals)
y_anim = np.cos(t_vals)
fig6 = px.scatter(x=x_anim, y=y_anim, animation_frame=t_vals, title="Parametric Animation: x=sin(t), y=cos(t)")
display(HTML(fig6.to_html()))

# 3D Scatter Plot with Color Dimension
z_vals = np.exp(-x_vals**2/10) * np.sin(y_vals)
df_3d_custom = pd.DataFrame({'x': x_vals, 'y': y_vals, 'z': z_vals})

fig7 = px.scatter_3d(df_3d_custom, x='x', y='y', z='z', color='z', title="3D Scatter Plot with Color Dimension")
display(HTML(fig7.to_html()))
