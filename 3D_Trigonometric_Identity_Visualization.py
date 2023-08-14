import plotly.graph_objects as go
import numpy as np

alpha_vals = np.linspace(0, 2 * np.pi, 100)
beta_vals = np.linspace(0, 2 * np.pi, 100)

# Calculate left and right sides of the identity
left_side_vals = np.cos(alpha_vals) + np.cos(beta_vals)
right_side_vals = 2 * np.cos(0.5 * (alpha_vals + beta_vals)) * np.cos(0.5 * (alpha_vals - beta_vals))

# Create the figure
fig = go.Figure()

# Add traces for left and right sides
fig.add_trace(go.Scatter(x=alpha_vals, y=left_side_vals, mode='lines', name='cos(α) + cos(β)'))
fig.add_trace(go.Scatter(x=alpha_vals, y=right_side_vals, mode='lines', name='2cos(1/2(α+β))cos(1/2(α-β))'))

# Customize layout
fig.update_layout(
    title='Trigonometric Identity Visualization',
    xaxis_title='α',
    yaxis_title='Value',
    legend=dict(x=0.02, y=0.98),
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True)
)

# Show the interactive plot
fig.show()
