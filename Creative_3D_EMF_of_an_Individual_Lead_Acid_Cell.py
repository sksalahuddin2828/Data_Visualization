import numpy as np
import pandas as pd
import plotly.express as px

# Constants
total_emf = 12.0  # Total EMF of the automobile battery in volts
num_cells = 6    # Number of lead-acid cells in series

# Calculate the EMF of an individual cell
emf_individual_cell = total_emf / num_cells

# Create a DataFrame to store data points for visualization
resistance_range = np.linspace(0, 1, 100)
voltage_drop_range = np.linspace(0, 1, 100)
resistance, voltage_drop = np.meshgrid(resistance_range, voltage_drop_range)
emf_values = emf_individual_cell - resistance * emf_individual_cell - voltage_drop * emf_individual_cell

df = pd.DataFrame({'Resistance': resistance.flatten(),
                   'Voltage Drop': voltage_drop.flatten(),
                   'EMF': emf_values.flatten()})

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(df, x='Resistance', y='Voltage Drop', z='EMF',
                     color='EMF', title='EMF of an Individual Lead-Acid Cell',
                     labels={'EMF': 'EMF of Individual Cell (V)'})
fig.update_traces(marker=dict(size=5))

# Customize the layout
fig.update_layout(scene=dict(xaxis_title='Cell Resistance',
                             yaxis_title='Internal Voltage Drop',
                             zaxis_title='EMF (V)'),
                  margin=dict(l=0, r=0, b=0, t=40))

# Show the interactive plot
fig.show()
