import numpy as np
import pandas as pd
import plotly.express as px

# Define the capacitor value (in Farads)
C = 0.500e-6  # 0.500 μF

# Define the range of resistor values
R_range = np.linspace(0.1, 10.0, 100)  # Change the range as needed

# Calculate time constants for the range of resistor values
time_constants = R_range * C

# Create a Pandas DataFrame to store the data
data = pd.DataFrame({'Resistor (Ohms)': R_range, 'Capacitor (F)': [C] * len(R_range), 'Time Constant (s)': time_constants})

# Create an interactive 3D surface plot using Plotly
fig = px.scatter_3d(data, x='Resistor (Ohms)', y='Capacitor (F)', z='Time Constant (s)',
                    title='Time Constant vs. Resistor and Capacitor',
                    labels={'Time Constant (s)': 'Time Constant (s)'})
fig.update_traces(marker=dict(size=5))  # Adjust marker size

# Add interactivity to the plot (hover information)
fig.update_layout(hovermode="closest")

# Customize the scene and layout
fig.update_layout(scene=dict(xaxis_title='Resistor (Ohms)', yaxis_title='Capacitor (F)'),
                  scene_camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)),
                  margin=dict(l=0, r=0, b=0, t=40))  # Adjust margins and camera position

# Show the interactive plot
fig.show()
