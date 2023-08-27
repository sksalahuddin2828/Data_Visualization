import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import sympy as sp
from scipy.special import jn

# Create time and power ranges
time_range = np.linspace(0, 24, 100)
power_range = np.linspace(0, 100, 100)

# Create a 3D meshgrid
time_mesh, power_mesh = np.meshgrid(time_range, power_range)

# Calculate the cost matrix with a complex mathematical pattern
def cost_function(t, p):
    return p * (1 + np.real(jn(0, t))) * np.exp(-0.1 * p * t)

cost_matrix = cost_function(time_mesh, power_mesh)

# Create a 3D surface plot animation
surface = go.Surface(
    x=time_mesh,
    y=power_mesh,
    z=cost_matrix,
    colorscale="Viridis",
    colorbar={"title": "Cost (USD)"},
)

# Create the figure
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])
fig.add_trace(surface)

# Add animation frames
frames = [go.Frame(data=[go.Surface(z=cost_matrix[:, :col], colorscale="Viridis")]) for col in range(1, len(power_range) + 1)]
fig.frames = frames

# Configure layout
fig.update_layout(
    scene=dict(
        xaxis_title="Time (hours)",
        yaxis_title="Power (kW)",
        zaxis_title="Cost (USD)",
        xaxis_range=[0, 24],
        yaxis_range=[0, 100],
        zaxis_range=[0, np.max(cost_matrix)],
        xaxis=dict(showline=False),
        yaxis=dict(showline=False),
        zaxis=dict(showline=False),
        camera_eye=dict(x=1.2, y=1.2, z=0.6),
    ),
    title_text="Artistic 3D Animation: Dynamic Mathematical Cost",
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}],
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
)

# Display the figure
fig.show()
