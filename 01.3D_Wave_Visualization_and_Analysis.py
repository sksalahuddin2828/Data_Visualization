import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Constants
A = 1.0
k = 2.0
ω = 3.0
ϕ = np.pi / 4.0

# Generate data
x = np.linspace(0, 10, 100)  # Spatial coordinates
t = np.linspace(0, 5, 50)    # Time coordinates

X, T = np.meshgrid(x, t)     # Meshgrid for 3D plot

# Calculate wave function
y = A * np.sin(k * X - ω * T + ϕ)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, y, cmap='viridis')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Time')
ax.set_zlabel('Amplitude')
ax.set_title('Wave Propagation')

plt.show()

# Calculate wave functions
y1 = A * np.sin(k * X - ω * T)
y2 = A * np.sin(2 * k * X + 2 * ω * T)
yR = y1 + y2

# Create 3D subplots for individual waves and resulting wave using Plotly
fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'surface'}, {'type': 'surface'}, {'type': 'surface'}]])
fig.add_trace(go.Surface(x=X, y=T, z=y1, colorscale='viridis', name='Wave 1'), row=1, col=1)
fig.add_trace(go.Surface(x=X, y=T, z=y2, colorscale='plasma', name='Wave 2'), row=1, col=2)
fig.add_trace(go.Surface(x=X, y=T, z=yR, colorscale='inferno', name='Resulting Wave'), row=1, col=3)

# Update subplot titles and labels
fig.update_layout(scene=dict(
    xaxis_title='Spatial Coordinate (X)',
    yaxis_title='Time',
    zaxis_title='Amplitude'
))

fig.update_layout(title='Wave Properties and Resulting Wave in 3D')

# Calculate velocity of resulting wave using the wave equation
# Calculate velocity of resulting wave using the wave equation
v_resulting = np.full_like(X, ω / k)

# Create a Plotly surface plot for the resulting wave velocity
velocity_fig = go.Figure(data=[
    go.Surface(x=X, y=T, z=v_resulting, colorscale='plasma')
])

# Update z-axis layout with tick suffix
velocity_fig.update_layout(scene=dict(zaxis=dict(ticksuffix=' units')))
velocity_fig.update_layout(title='Velocity of Resulting Wave in 3D')

# Display using Plotly
fig.show()
velocity_fig.show()
