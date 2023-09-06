import numpy as np
import pandas as pd
import plotly.express as px

# Given parameters
resistance_between_hands = 10.0e3  # 10.0 kΩ
voltage_supply = 20.0e3  # 20.0 kV

# Create a range of internal resistance values
internal_resistance_values = np.linspace(0, 5e3, 100)  # Vary internal resistance from 0 to 5000 Ω

# Calculate current through the body for each internal resistance value
current_values = voltage_supply / (resistance_between_hands + internal_resistance_values)

# Calculate power dissipated in the body for each internal resistance value
power_values = current_values**2 * (resistance_between_hands + internal_resistance_values)

# Create a DataFrame to store the data
df = pd.DataFrame({'Internal Resistance (Ω)': internal_resistance_values,
                   'Current (A)': current_values,
                   'Power (W)': power_values})

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(df, x='Internal Resistance (Ω)', y='Current (A)', z='Power (W)',
                     title='Effect of Internal Resistance on Current and Power',
                     labels={'Power (W)': 'Power (Watts)'})

# Customize the appearance and layout
fig.update_traces(marker=dict(size=3), selector=dict(mode='markers+lines'))
fig.update_layout(scene=dict(xaxis_title='Internal Resistance (Ω)',
                             yaxis_title='Current (A)',
                             zaxis_title='Power (W)'),
                  margin=dict(l=0, r=0, b=0, t=40))

# Show the interactive plot
fig.show()
