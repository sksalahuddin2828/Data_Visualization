import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Generating data
R1_vals = np.linspace(1, 100, 20)
R2_vals = np.linspace(1, 100, 20)
R1_vals, R2_vals = np.meshgrid(R1_vals, R2_vals)

# Calculate effective resistances
Reff_vals = 1 / (1/R1_vals + 1/R2_vals)

# Create a DataFrame for the plot
data = pd.DataFrame({
    'R1': R1_vals.flatten(),
    'R2': R2_vals.flatten(),
    'Reff': Reff_vals.flatten()
})

# Create a scatter plot
fig = go.Figure(data=go.Scatter3d(
    x=data['R1'],
    y=data['R2'],
    z=data['Reff'],
    mode='markers',
    marker=dict(size=5, color=data['Reff'], colorscale='Viridis'),
    text=data.apply(lambda row: f"R1: {row['R1']}, R2: {row['R2']}, Reff: {row['Reff']:.2f}", axis=1)
))

# Add labels and title
fig.update_layout(scene=dict(xaxis_title='R1', yaxis_title='R2', zaxis_title='Reff'),
                  title='Effective Resistance in Parallel')

# Show the plot
fig.show()

# Create an animated scatter plot
animation_frames = [go.Frame(data=[go.Scatter3d(
    x=data['R1'],
    y=data['R2'],
    z=data['Reff'],
    mode='markers',
    marker=dict(size=5, color=data['Reff'], colorscale='Viridis'),
    text=data.apply(lambda row: f"R1: {row['R1']}, R2: {row['R2']}, Reff: {row['Reff']:.2f}", axis=1)
)]) for reff in data['Reff']]

fig = go.Figure(data=[go.Scatter3d(
    x=data['R1'],
    y=data['R2'],
    z=data['Reff'],
    mode='markers',
    marker=dict(size=5, color=data['Reff'], colorscale='Viridis'),
    text=data.apply(lambda row: f"R1: {row['R1']}, R2: {row['R2']}, Reff: {row['Reff']:.2f}", axis=1)
)], frames=animation_frames)

# Add labels and title
fig.update_layout(scene=dict(xaxis_title='R1', yaxis_title='R2', zaxis_title='Reff'),
                  title='Effective Resistance Animation in Parallel')

# Define animation settings
animation_settings = dict(frame=dict(duration=300, redraw=True), fromcurrent=True)
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                  method='animate', args=[None, animation_settings])])])

# Show the animated plot
fig.show()
