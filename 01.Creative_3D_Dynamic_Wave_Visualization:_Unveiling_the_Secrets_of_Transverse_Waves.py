import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Given wave function parameters
A = 0.2
k = 6.28
omega = 1.57

# Calculate wave characteristics
wavelength = 2 * np.pi / k
period = 2 * np.pi / omega
wave_speed = omega / k

# Create x values
x_values = np.linspace(0, 10, 400)

# Calculate y values for a single time point
y_values = A * np.sin(k * x_values - omega * 0)

# Create a line plot for the wave
wave_fig = go.Figure(go.Scatter(x=x_values, y=y_values))
wave_fig.update_layout(title="Transverse Wave on a String",
                      xaxis_title="Position (x)", yaxis_title="Amplitude (y)")

# Create a 3D surface plot
t_values = np.linspace(0, 10, 200)
X, T = np.meshgrid(x_values, t_values)
y_values_3d = A * np.sin(k * X - omega * T)

surface_fig = go.Figure(data=[go.Surface(z=y_values_3d, x=X, y=T)])
surface_fig.update_layout(title="3D Visualization of Transverse Wave",
                          scene=dict(xaxis_title="Position (x)", yaxis_title="Time (t)", zaxis_title="Amplitude (y)"))

# Display calculated information
info_text = f"Amplitude: {A}\nWavelength: {wavelength:.2f} m\nPeriod: {period:.2f} s\nWave Speed: {wave_speed:.2f} m/s"

# Arrange figures using subplots
fig = make_subplots(rows=2, cols=1, subplot_titles=["Wave Plot", "3D Surface Plot"])
fig.add_trace(wave_fig.data[0], row=1, col=1)
fig.update_xaxes(title_text="Position (x)", row=1, col=1)
fig.update_yaxes(title_text="Amplitude (y)", row=1, col=1)

fig2 = make_subplots(rows=1, cols=1, subplot_titles=[""])
fig2.add_trace(surface_fig.data[0])
fig2.update_layout(scene=dict(xaxis_title="Position (x)", yaxis_title="Time (t)", zaxis_title="Amplitude (y)"))

# Display both figures
fig.show()
fig2.show()
