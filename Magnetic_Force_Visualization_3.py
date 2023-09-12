import numpy as np
import pandas as pd
import plotly.express as px

def calculate_magnetic_force(charge, velocity, magnetic_field, angle):
    force = charge * np.linalg.norm(velocity) * np.linalg.norm(magnetic_field) * np.sin(angle)
    return force

# Create a DataFrame to store results
results = pd.DataFrame(columns=['Charge (C)', 'Velocity (m/s)', 'Magnetic Field (T)', 'Angle (rad)', 'Force (N)'])

# Example data
charge = 1.6e-19
velocity = np.array([1, 0, 0])
magnetic_field = np.array([0, 0, 1])
angle = np.pi / 4  # 45 degrees

force = calculate_magnetic_force(charge, velocity, magnetic_field, angle)

# Add data to the DataFrame
results.loc[0] = [charge, np.linalg.norm(velocity), np.linalg.norm(magnetic_field), angle, force]

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(results, x='Velocity (m/s)', y='Magnetic Field (T)', z='Force (N)',
                    text='Charge (C)', title='Magnetic Force Visualization')

# Customize the plot appearance
fig.update_traces(marker=dict(size=5, opacity=0.8),
                  selector=dict(mode='markers+text'))

# Set axis labels
fig.update_layout(scene=dict(xaxis_title='Velocity (m/s)', yaxis_title='Magnetic Field (T)', zaxis_title='Force (N)'))

# Show the interactive plot
fig.show()
