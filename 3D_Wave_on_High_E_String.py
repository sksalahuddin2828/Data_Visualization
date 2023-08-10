import numpy as np
import plotly.graph_objects as go

# Given values
tension_high_E = 56.40  # N
linear_density_high_E = 3.09e-4  # kg/m

# Calculate wave speed using the formula: v = sqrt(FT / μ)
wave_speed_high_E = np.sqrt(tension_high_E / linear_density_high_E)

print(f"Wave speed on high E string: {wave_speed_high_E:.2f} m/s")

# Visualization
x = np.linspace(0, 1, 100)  # Points along the string
y = np.sin(2 * np.pi * x)  # Example wave shape

# Create a Plotly figure
fig = go.Figure()

# Add a scatter trace for the wave
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Wave on High E String'))

# Update layout for title, labels, and grid
fig.update_layout(
    title="Wave on High E String",
    xaxis_title="Position along string",
    yaxis_title="Amplitude",
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True),
)

# Show the interactive plot
fig.show()
