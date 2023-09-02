import numpy as np
import pandas as pd
import plotly.express as px

# Function to calculate the operating voltage of each bulb with one burnt-out bulb
def calculate_voltage_with_burnt_out(total_voltage, num_bulbs, remaining_bulbs):
    return total_voltage / remaining_bulbs

# Constants
total_voltage = 120  # Total voltage in the circuit
num_bulbs = 40      # Number of bulbs in the circuit

# Create a list of remaining bulbs from 1 to num_bulbs - 1 (one bulb burnt out)
remaining_bulbs_list = list(range(1, num_bulbs))

# Calculate the operating voltage for each remaining bulb count
voltage_with_burnt_out_list = [calculate_voltage_with_burnt_out(total_voltage, num_bulbs, rb) for rb in remaining_bulbs_list]

# Create a DataFrame for visualization using Pandas
data = pd.DataFrame({'Remaining Bulbs': remaining_bulbs_list, 'Operating Voltage (V)': voltage_with_burnt_out_list})

# Create an interactive plot using Plotly
fig = px.line(data, x='Remaining Bulbs', y='Operating Voltage (V)', title='Operating Voltage vs. Remaining Bulbs')
fig.update_xaxes(title_text='Remaining Bulbs')
fig.update_yaxes(title_text='Operating Voltage (V)')

# Show the interactive plot
fig.show()
