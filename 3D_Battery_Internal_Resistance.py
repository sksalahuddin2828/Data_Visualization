import numpy as np

# Given data
emf = 12.0  # V
terminal_voltage = 16.0  # V
charging_current = 10.0  # A

# Calculate internal resistance (R) using Ohm's law
R = (emf - terminal_voltage) / charging_current
print(f"The battery's internal resistance is {R} ohms.")

# Answer: The battery's internal resistance is -0.4 ohms.

import numpy as np
import pandas as pd
import plotly.express as px

# Given data
emf = 12.0  # V
terminal_voltage = 16.0  # V
charging_current = 10.0  # A

# Calculate internal resistance (R) using Ohm's law
R = (emf - terminal_voltage) / charging_current

# Create a DataFrame for visualization
df = pd.DataFrame({'Voltage': np.linspace(0, emf, 50)})
df['Current'] = (emf - df['Voltage']) / R

# Create an interactive 3D scatter plot
fig = px.scatter_3d(df, x='Voltage', y='Current', z='Voltage', color='Current',
                     title='Battery Internal Resistance',
                     labels={'Voltage': 'Terminal Voltage (V)', 'Current': 'Charging Current (A)'})
fig.update_traces(marker=dict(size=5))
fig.update_layout(scene=dict(xaxis_title='Terminal Voltage (V)', yaxis_title='Charging Current (A)',
                             zaxis_title='Voltage (V)'))
fig.show()

print(f"The battery's internal resistance is {R} ohms.")
