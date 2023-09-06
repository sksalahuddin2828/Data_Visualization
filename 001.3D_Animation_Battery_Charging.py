import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Given data
emf = 12.0  # V
charging_current = 10.0  # A
time_interval = 10  # seconds
total_time = 120  # seconds

# Calculate internal resistance (R) using Ohm's law
terminal_voltage = []
time_points = []
for t in range(0, total_time + 1, time_interval):
    V = emf - charging_current * t / 3600  # Convert seconds to hours
    terminal_voltage.append(V)
    time_points.append(t)

# Calculate power dissipated inside the battery for each time point
R = (emf - terminal_voltage[-1]) / charging_current  # Recalculate R using the final voltage
power_dissipated = [(I ** 2) * R for I in (charging_current * np.ones(len(time_points)))]

# Create an animated plot
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    subplot_titles=("Battery Terminal Voltage vs. Time",
                                    "Power Dissipated Inside Battery vs. Time"))

# Add voltage vs. time trace
trace1 = go.Scatter(x=time_points, y=terminal_voltage, mode='lines+markers', name='Voltage (V)')
fig.add_trace(trace1, row=1, col=1)

# Add power vs. time trace
trace2 = go.Scatter(x=time_points, y=power_dissipated, mode='lines+markers', name='Power (W)')
fig.add_trace(trace2, row=2, col=1)

# Update axis labels and titles
fig.update_xaxes(title_text="Time (s)", row=2, col=1)
fig.update_xaxes(title_text="Time (s)", row=1, col=1)
fig.update_yaxes(title_text="Voltage (V)", row=1, col=1)
fig.update_yaxes(title_text="Power (W)", row=2, col=1)
fig.update_layout(title="Battery Charging Animation",
                  xaxis=dict(range=[0, total_time]),
                  showlegend=True,
                  sliders=[{
                      "steps": [{"args": [[str(t)], {"frame": {"duration": 500, "redraw": True}, "mode": "immediate", "transition": {"duration": 300}}], "label": str(t), "method": "animate"} for t in time_points],
                      "transition": {"duration": 0},
                      "x": 0,
                      "xanchor": "left",
                      "y": -0.2,
                      "yanchor": "bottom"
                  }])

# Add frames for animation
frames = [go.Frame(data=[go.Scatter(x=time_points[:i], y=terminal_voltage[:i], mode='lines+markers', name='Voltage (V)'),
                         go.Scatter(x=time_points[:i], y=power_dissipated[:i], mode='lines+markers', name='Power (W)')],
                   traces=[0, 1],
                   name=str(t)) for i, t in enumerate(time_points)]

fig.update(frames=frames)

# Show the animation
fig.show()
