import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

theta_vals = np.linspace(0, 2 * np.pi, 100)
tan_vals = np.tan(theta_vals)

# Create subplots
fig = make_subplots(rows=2, cols=1, subplot_titles=("Tangent Function", "Periodic Behavior Animation"))

# Add trace for tangent function
fig.add_trace(go.Scatter(x=theta_vals, y=tan_vals, mode='lines', name='$tan(θ)$'), row=1, col=1)

# Customize layout for the first subplot
fig.update_xaxes(title_text="$θ$", showgrid=True, row=1, col=1)
fig.update_yaxes(title_text="tan(θ)", showgrid=True, row=1, col=1)

# Animate the periodic behavior of the tangent function
animation_trace = go.Scatter(x=theta_vals[:2], y=tan_vals[:2], mode='lines', showlegend=False)

# Customize layout for the second subplot
fig.add_trace(animation_trace, row=2, col=1)
fig.update_xaxes(title_text="$θ$", showgrid=True, row=2, col=1)
fig.update_yaxes(title_text="tan(θ)", showgrid=True, row=2, col=1)

# Create animation frames
frames = [go.Frame(data=[go.Scatter(x=theta_vals[:i], y=tan_vals[:i], mode='lines', showlegend=False)], name=str(i)) for i in range(2, len(theta_vals), 5)]

# Add frames to the figure
fig.frames = frames
animation_settings = dict(frame=dict(duration=100, redraw=True), fromcurrent=True)
fig.update(frames=frames, layout_updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play', method='animate', args=[None, animation_settings])])])

# Add informative annotations
annotations = [
    go.layout.Annotation(
        x=theta_vals[i], y=tan_vals[i],
        xref="x2", yref="y2",
        text=f"θ = {theta_vals[i]:.2f}\n tan(θ) = {tan_vals[i]:.2f}",
        font=dict(size=10),
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        ax=20,
        ay=-40
    ) for i in range(0, len(theta_vals), 10)
]
fig.update_layout(annotations=annotations)

# Show the interactive plot
fig.show()
