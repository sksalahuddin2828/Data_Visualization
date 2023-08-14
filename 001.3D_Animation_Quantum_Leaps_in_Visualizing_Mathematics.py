import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Define the range of alpha and beta values
alpha_vals = np.linspace(0, 2 * np.pi, 100)
beta_vals = np.linspace(0, 2 * np.pi, 100)

# Calculate left and right sides of the identity
left_side_vals = np.cos(alpha_vals) + np.cos(beta_vals)
right_side_vals = 2 * np.cos(0.5 * (alpha_vals + beta_vals)) * np.cos(0.5 * (alpha_vals - beta_vals))

# Create subplots
fig = make_subplots(rows=2, cols=1, subplot_titles=("Trigonometric Identity", "Animated Transformation"))

# Add traces for the trigonometric identity
fig.add_trace(go.Scatter(x=alpha_vals, y=left_side_vals, mode='lines', name='$\cos(\\alpha) + \cos(\\beta)$'), row=1, col=1)
fig.add_trace(go.Scatter(x=alpha_vals, y=right_side_vals, mode='lines', name='$2\cos\\left(\\frac{1}{2}(\\alpha+\\beta)\\right)\cos\\left(\\frac{1}{2}(\\alpha-\\beta)\\right)$'), row=1, col=1)

# Customize layout for the first subplot
fig.update_xaxes(title_text="$\\alpha$", showgrid=True, row=1, col=1)
fig.update_yaxes(title_text="Value", showgrid=True, row=1, col=1)

# Animate transformation using a parametric equation
t_vals = np.linspace(0, 2 * np.pi, 100)
x_vals = np.cos(t_vals)
y_vals = np.sin(t_vals)

# Add traces for animation
transition_trace = go.Scatter(x=x_vals, y=y_vals, mode='lines+markers', line=dict(color='red'), showlegend=False)
animation_trace = go.Scatter(x=[x_vals[0]], y=[y_vals[0]], mode='markers', marker=dict(size=10, color='blue'), showlegend=False)

# Add traces to the second subplot
fig.add_trace(transition_trace, row=2, col=1)
fig.add_trace(animation_trace, row=2, col=1)

# Customize layout for the second subplot
fig.update_xaxes(title_text="X", showgrid=False, row=2, col=1)
fig.update_yaxes(title_text="Y", showgrid=False, row=2, col=1)

# Create animation frames
frames = [go.Frame(data=[go.Scatter(x=[x_vals[i]], y=[y_vals[i]], mode='markers', marker=dict(size=10, color='blue'), showlegend=False)], name=str(i)) for i in range(len(x_vals))]

# Add frames to the figure
fig.frames = frames
animation_settings = dict(frame=dict(duration=50, redraw=True), fromcurrent=True)
fig.update(frames=[go.Frame(data=[go.Scatter(x=[x_vals[i]], y=[y_vals[i]], mode='markers', marker=dict(size=10, color='blue'), showlegend=False)], name=str(i)) for i in range(len(x_vals))], layout_updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play', method='animate', args=[None, animation_settings])])])

# Show the interactive plot
fig.show()
