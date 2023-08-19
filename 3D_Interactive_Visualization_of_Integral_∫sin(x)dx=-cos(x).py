import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sympy as sp

# Calculate integral
x = sp.symbols('x')
integral_expr = sp.integrate(sp.sin(x), x)

# Generate data
x_vals = np.linspace(0, 2*np.pi, 100)
y_vals = np.sin(x_vals)
z_vals = -np.cos(x_vals)

# Create a DataFrame for pandas
data = {'x': x_vals, 'sin(x)': y_vals, '-cos(x)': z_vals}
df = pd.DataFrame(data)

# Create interactive subplot
fig = make_subplots(rows=2, cols=1, shared_xaxes=True)

# Add line plots to the subplot
fig.add_trace(go.Scatter(x=df['x'], y=df['sin(x)'], mode='lines', name='sin(x)'), row=1, col=1)
fig.add_trace(go.Scatter(x=df['x'], y=df['-cos(x)'], mode='lines', name='-cos(x)'), row=2, col=1)

# Update subplot layout
fig.update_layout(title='Interactive Visualization of Integral ∫sin(x) dx = -cos(x)',
                  xaxis_title='x', yaxis_title='Value',
                  showlegend=True)

# Add annotations
fig.add_annotation(x=3, y=-0.8, text="∫sin(x) dx = -cos(x)", showarrow=True, arrowhead=1)

# Add slider to control x values
slider_steps = [dict(args=['x', [x_vals[i]]],
                     label=f'{x_vals[i]:.2f}',
                     method='animate') for i in range(len(x_vals))]

sliders = [dict(active=0, steps=slider_steps)]

fig.update_layout(sliders=sliders)

# Show the interactive plot
fig.show()
