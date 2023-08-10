import numpy as np
import plotly.graph_objects as go

# Given values for the high E string
linear_density_high_E = 3.09e-4  # kg/m
tension_high_E = 56.40  # N

# Given values for the low E string
linear_density_low_E = 5.78e-3  # kg/m

# Calculate wave speed using the formula: v = sqrt(FT / μ)
wave_speed_high_E = np.sqrt(tension_high_E / linear_density_high_E)

print(f"Wave speed on high E string: {wave_speed_high_E:.2f} m/s")

# Calculate tension needed for the low E string to match wave speed
tension_low_E = linear_density_low_E * wave_speed_high_E**2

print(f"Tension needed for low E string: {tension_low_E:.2f} N")

# Visualization
x = np.linspace(0, 1, 100)  # Points along the string

# Example sine waves for visualization
wave_high_E = np.sin(2 * np.pi * x)
wave_low_E = 0.5 * np.sin(2 * np.pi * x)

# Create a Plotly figure
fig = go.Figure()

# Add scatter traces for the waves
fig.add_trace(go.Scatter(x=x, y=wave_high_E, mode='lines', name='High E String'))
fig.add_trace(go.Scatter(x=x, y=wave_low_E, mode='lines', name='Low E String'))

# Update layout for title, labels, and legend
fig.update_layout(
    title="Wave Comparison: High E vs. Low E String",
    xaxis_title="Position along string",
    yaxis_title="Amplitude",
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True),
    legend=dict(x=0.02, y=0.95),
)

# Show the interactive plot
fig.show()


# Answer: Wave speed on high E string: 427.23 m/s
#         Tension needed for low E string: 1054.99 N
