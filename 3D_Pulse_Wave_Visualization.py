import numpy as np
import plotly.graph_objects as go

def pulse_wave(x, A, v):
    return A * np.exp(-x/v)

x_values = np.linspace(0, 10, 100)
A = 1.0  # Amplitude
v = 2.0  # Wave speed

y_values = pulse_wave(x_values, A, v)

fig = go.Figure()

# Adding the surface plot with a color scale and custom surface style
surface = go.Surface(z=y_values, x=x_values, y=[0], colorscale='Viridis', showscale=True)
fig.add_trace(surface)

# Adding markers along the wave
markers = go.Scatter3d(x=x_values, y=[0] * len(x_values), z=y_values,
                       mode='markers', marker=dict(size=5, color='red'), name='Markers')
fig.add_trace(markers)

fig.update_layout(
    title='Creative Pulse Wave Visualization',
    scene=dict(
        xaxis_title='x (m)',
        yaxis_title='Amplitude',
        zaxis_title='Wave Height',
    ),
)

fig.show()
