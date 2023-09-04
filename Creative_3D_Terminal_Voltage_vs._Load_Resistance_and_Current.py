import numpy as np
import pandas as pd
import plotly.express as px

# Given values
emf = 12.0  # V
internal_resistance = 0.1  # Ohms

# Create a range of load resistances
load_resistance = np.linspace(1, 20, 100)

# Calculate current and terminal voltage
current = emf / (load_resistance + internal_resistance)
terminal_voltage = emf - current * internal_resistance

# Create a DataFrame to store the data
data = pd.DataFrame({'Load Resistance (Ω)': load_resistance, 'Current (A)': current, 'Terminal Voltage (V)': terminal_voltage})

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(data_frame=data, x='Load Resistance (Ω)', y='Current (A)', z='Terminal Voltage (V)',
                    color='Terminal Voltage (V)', title='Terminal Voltage vs. Load Resistance and Current',
                    labels={'Load Resistance (Ω)': 'Load Resistance', 'Current (A)': 'Current', 'Terminal Voltage (V)': 'Terminal Voltage'})
fig.update_traces(marker=dict(size=5))

# Show the interactive plot
fig.show()
