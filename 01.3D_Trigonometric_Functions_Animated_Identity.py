import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

theta_vals = np.linspace(0, 2 * np.pi, 100)
tan_vals = np.tan(theta_vals)
cot_vals = 1 / np.tan(theta_vals)
tan_cot_identity = tan_vals * cot_vals

# Create subplots
fig = make_subplots(rows=2, cols=1, subplot_titles=("Trigonometric Functions", "Animated Identity"))

# Add traces for trigonometric functions
fig.add_trace(go.Scatter(x=theta_vals, y=tan_vals, mode='lines', name='$tan(θ)$'), row=1, col=1)
fig.add_trace(go.Scatter(x=theta_vals, y=cot_vals, mode='lines', name='$cot(θ)$'), row=1, col=1)

# Customize layout for the first subplot
fig.update_xaxes(title_text="$θ$", showgrid=True, row=1, col=1)
fig.update_yaxes(title_text="Value", showgrid=True, row=1, col=1)

# Animate the tan(cot(θ)) identity
animation_trace = go.Scatter(x=theta_vals, y=tan_cot_identity, mode='lines', showlegend=False)

# Customize layout for the second subplot
fig.add_trace(animation_trace, row=2, col=1)
fig.update_xaxes(title_text="$θ$", showgrid=True, row=2, col=1)
fig.update_yaxes(title_text="$tan(θ) \cdot cot(θ)$", showgrid=True, row=2, col=1)

# Create animation frames
frames = [go.Frame(data=[go.Scatter(x=theta_vals[:i], y=tan_cot_identity[:i], mode='lines', showlegend=False)], name=str(i)) for i in range(2, len(theta_vals))]

# Add frames to the figure
fig.frames = frames
animation_settings = dict(frame=dict(duration=50, redraw=True), fromcurrent=True)
fig.update(frames=frames, layout_updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play', method='animate', args=[None, animation_settings])])])

# Add explanatory text using annotations
fig.update_layout(annotations=[
    go.layout.Annotation(
        x=1.6, y=0.8,
        xref="x2", yref="y2",
        text="tan(θ) * cot(θ)",
        font=dict(size=18),
        showarrow=False
    )
])

# Show the interactive plot
fig.show()
