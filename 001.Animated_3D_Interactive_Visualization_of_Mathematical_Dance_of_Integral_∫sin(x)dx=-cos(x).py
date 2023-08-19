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

import plotly.graph_objects as go

slider_steps = []

for i in range(len(x_vals)):
    slider_step = {
        "args": [
            [f"frame{i}"],
            {
                "frame": {"duration": 100, "redraw": True},
                "mode": "immediate",
                "transition": {"duration": 0}
            }
        ],
        "label": f"{x_vals[i]:.2f}",
        "method": "animate"
    }
    slider_steps.append(slider_step)

animation_frames = []

for i in range(len(x_vals)):
    animation_frame = {
        "data": [
            {"x": x_vals[:i + 1], "y": y_vals[:i + 1], "mode": "lines", "name": "sin(x)"},
            {"x": x_vals[:i + 1], "y": z_vals[:i + 1], "mode": "lines", "name": "-cos(x)"}
        ],
        "layout": go.Layout(
            title=f"Mathematical Dance: ∫sin(x) dx = -cos(x) for x = {x_vals[i]:.2f}",
            xaxis_title="x", yaxis_title="Value", showlegend=True
        )
    }
    animation_frames.append(animation_frame)

animation_fig = go.Figure(
    data=[
        {"x": x_vals, "y": y_vals, "mode": "lines", "name": "sin(x)"},
        {"x": x_vals, "y": z_vals, "mode": "lines", "name": "-cos(x)"}
    ],
    frames=animation_frames
)

animation_fig.update_layout(
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}],
                    "label": "Play",
                    "method": "animate",
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate",
                },
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top",
        }
    ],
    sliders=[{
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 20},
            "prefix": "x = ",
            "visible": True,
            "xanchor": "right"
        },
        "transition": {"duration": 300, "easing": "cubic-in-out"},
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
    }],
)

animation_fig.show()
