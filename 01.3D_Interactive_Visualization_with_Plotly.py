import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create data points for a 3D plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Create a figure
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])

# Add surface plot to the figure
surface = go.Surface(z=Z, colorscale='Viridis')
fig.add_trace(surface, row=1, col=1)

# Update layout for better presentation
fig.update_layout(
    title="3D Interactive Visualization with Plotly",
    scene=dict(
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        zaxis_title='Z-axis',
    ),
    scene_camera=dict(
        eye=dict(x=1.7, y=-1.7, z=0.5),
        up=dict(x=0, y=0, z=1)
    )
)

# Animation settings
frames = [go.Frame(data=[go.Surface(z=Z + np.sin(i / 10) * 2, colorscale='Viridis')]) for i in range(100)]
updatemenus = [dict(type='buttons', showactive=False, buttons=[dict(label='Play', method='animate', args=[None, dict(frame=dict(duration=50, redraw=True), fromcurrent=True, mode='immediate')]), dict(label='Pause', method='animate', args=[[None], dict(frame=dict(duration=0, redraw=False), mode='immediate')])])]
sliders = [dict(steps=[dict(args=[['frame{}'.format(k)], dict(mode='immediate', frame=dict(duration=50, redraw=True), transition=dict(duration=0))], label=str(k)) for k in range(100)], pad=dict(t=0, b=0), currentvalue=dict(visible=True, prefix='Frame: ', xanchor='center'), transition=dict(duration=0), x=0.1, len=0.9)]

# Add animation and sliders to the figure
fig.update(frames=frames)
fig.update_layout(updatemenus=updatemenus, sliders=sliders)

# Show the plot
fig.show()
