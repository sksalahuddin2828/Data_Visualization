import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Create example data
current_data = np.linspace(0.001, 1, 100)
duration_data = np.linspace(0.1, 5, 100)
shock_hazard_data = np.outer(current_data, duration_data)  # Use outer product to create 2D array

# Create figure
fig = go.Figure()

# Add initial frame
initial_trace = go.Heatmap(z=shock_hazard_data, x=duration_data, y=current_data)
fig.add_trace(initial_trace)

# Create a dictionary to store animation frames
animation_frames = []

# Add animation frames
for i in range(1, shock_hazard_data.shape[0]):
    frame_data = shock_hazard_data[i, :]
    frame_trace = go.Heatmap(z=[frame_data], x=duration_data, y=current_data)
    animation_frames.append(go.Frame(data=[frame_trace]))

# Add frames to the figure
fig.frames = animation_frames

# Customize layout
fig.update_layout(
    title='Dynamic Shock Hazard Animation',
    xaxis_title='Duration (s)',
    yaxis_title='Current (A)',
    coloraxis_colorbar_title='Shock Hazard'
)

# Add play and pause buttons
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
    method='animate', args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True, 'transition': {'duration': 0}}]),
    dict(label='Pause', method='animate', args=[[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate', 'transition': {'duration': 0}}])])])

# Add animation slider
fig.update_layout(sliders=[dict(currentvalue={'prefix': 'Frame: '}, steps=[dict(args=[f.name, {'frame': {'duration': 100, 'redraw': True}, 'mode': 'immediate'}], label=str(i)) for i, f in enumerate(fig.frames)])])

fig.show()
