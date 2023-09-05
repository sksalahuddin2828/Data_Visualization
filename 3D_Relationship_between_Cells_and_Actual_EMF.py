import numpy as np
import sympy as sp
import pandas as pd
import plotly.express as px

emf_single_cell = 1.54  # EMF of a single cell in volts
desired_voltage = 9  # Desired battery voltage in volts

# Calculate the number of cells needed
num_cells = np.ceil(desired_voltage / emf_single_cell).astype(int)
print(f"(a) Number of cells needed: {num_cells}")

actual_emf = num_cells * emf_single_cell
print(f"(b) Actual EMF of the 9-V battery: {actual_emf} V")

# Create a DataFrame with the data
data = pd.DataFrame({'Number of Cells': np.arange(1, 21), 'Actual EMF (V)': np.arange(1, 21) * emf_single_cell})

# Create an interactive line plot
fig = px.line(data, x='Number of Cells', y='Actual EMF (V)', title='Relationship between Cells and Actual EMF')
fig.update_traces(mode='markers+lines')

# Add labels and title
fig.update_xaxes(title_text='Number of Cells')
fig.update_yaxes(title_text='Actual EMF (V)')

# Show the interactive plot
fig.show()
