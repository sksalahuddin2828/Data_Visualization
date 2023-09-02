import numpy as np
import pandas as pd
import plotly.express as px

# Resistances in ohms
resistor_values = [1e2, 2.5e3, 4e3]
resistor_names = ['R1', 'R2', 'R3']

# Create a DataFrame to store resistor data
resistor_df = pd.DataFrame({'Resistor': resistor_names, 'Resistance (Ohms)': resistor_values})

# Calculate total resistance in series
total_resistance_series = np.sum(resistor_values)

# Calculate total resistance in parallel
total_resistance_parallel = 1 / np.sum(1 / np.array(resistor_values))

print(f"Total Resistance in Series: {total_resistance_series:.2f} ohms")
print(f"Total Resistance in Parallel: {total_resistance_parallel:.2f} ohms")

# Create an interactive 3D plot using Plotly
fig = px.scatter_3d(resistor_df, x='Resistor', y='Resistance (Ohms)', z='Resistance (Ohms)',
                    text='Resistor', title='Resistors in 3D')

# Customize the plot appearance
fig.update_traces(marker=dict(size=5, symbol='square', opacity=0.7),
                  selector=dict(mode='markers+text'))

# Update axis labels
fig.update_layout(scene=dict(xaxis_title='Resistor', yaxis_title='', zaxis_title='Resistance (Ohms)'),
                  scene_camera=dict(up=dict(x=0, y=0, z=1)))

# Show the interactive plot
fig.show()
