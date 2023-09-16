import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given values
v = 12
angle_deg = 45
x_horizontal = 15
g = 10

# Convert angle to radians
angle_rad = np.radians(angle_deg)

# Calculate the vertical component using trigonometry
v_vertical = v * np.sin(angle_rad)

# Calculate the time of flight using kinematic equations
t_flight = (2 * v_vertical) / g

# Create a time array for trajectory calculation
t = np.linspace(0, t_flight, num=100)

# Calculate horizontal and vertical positions at each time step
x = x_horizontal * t
y = v_vertical * t - 0.5 * g * t**2

# Create a pandas DataFrame for the trajectory data
trajectory_df = pd.DataFrame({'Time (s)': t, 'Horizontal Position (m)': x, 'Vertical Position (m)': y})

# Create an interactive 2D plot using Plotly
fig = px.line(trajectory_df, x='Horizontal Position (m)', y='Vertical Position (m)',
              title='Projectile Motion', labels={'Horizontal Position (m)': 'Horizontal Position (m)',
                                                    'Vertical Position (m)': 'Vertical Position (m)'})

# Add annotations for important points
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=10, color='red'), name='Start (0, 0)'))
fig.add_trace(go.Scatter(x=[x_horizontal], y=[0], mode='markers', marker=dict(size=10, color='green'), name='Landing'))

# Customize layout
fig.update_layout(
    xaxis_title='Horizontal Position (m)',
    yaxis_title='Vertical Position (m)',
    showlegend=True,
    hovermode='closest',
    annotations=[
        dict(x=0, y=0, text='Start (0, 0)', showarrow=True, arrowhead=2, ax=0, ay=-40),
        dict(x=x_horizontal, y=0, text='Landing', showarrow=True, arrowhead=2, ax=0, ay=-40),
    ]
)

# Display the interactive plot
fig.show()
