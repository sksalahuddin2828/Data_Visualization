import numpy as np
import pandas as pd
import plotly.express as px

# Constants
emf = 12.0  # EMF in volts
internal_resistance = 0.100  # Internal resistance in ohms
loads = np.linspace(0.1, 5.0, 50)  # Load resistance values from 0.1 to 5.0 ohms
internal_resistances = np.linspace(0.1, 2.0, 50)  # Internal resistance values from 0.1 to 2.0 ohms

# Initialize empty lists to store data
load_resistance_list = []
internal_resistance_list = []
terminal_voltage_list = []
power_dissipated_list = []

# Calculate and store data
for load_resistance in loads:
    for internal_resistance in internal_resistances:
        V = emf - (emf / (internal_resistance + 10.0)) * load_resistance
        power = ((emf / (internal_resistance + 10.0)) * load_resistance) ** 2 * 10.0
        load_resistance_list.append(load_resistance)
        internal_resistance_list.append(internal_resistance)
        terminal_voltage_list.append(V)
        power_dissipated_list.append(power)

# Create a Pandas DataFrame
df = pd.DataFrame({
    'Load Resistance (Ω)': load_resistance_list,
    'Internal Resistance (Ω)': internal_resistance_list,
    'Terminal Voltage (V)': terminal_voltage_list,
    'Power Dissipated (W)': power_dissipated_list
})

# Create interactive 3D visualization using Plotly
fig = px.scatter_3d(df, x='Load Resistance (Ω)', y='Internal Resistance (Ω)', z='Terminal Voltage (V)',
                     color='Power Dissipated (W)', title='Terminal Voltage vs. Load and Internal Resistance',
                     labels={'Load Resistance (Ω)': 'Load Resistance (Ω)',
                             'Internal Resistance (Ω)': 'Internal Resistance (Ω)',
                             'Terminal Voltage (V)': 'Terminal Voltage (V)',
                             'Power Dissipated (W)': 'Power Dissipated (W)'},
                     color_continuous_scale='viridis')

fig.update_traces(marker=dict(size=5),
                  selector=dict(mode='markers'))

# Customize layout
fig.update_layout(scene=dict(xaxis_title='Load Resistance (Ω)',
                             yaxis_title='Internal Resistance (Ω)',
                             zaxis_title='Terminal Voltage (V)'),
                  coloraxis_showscale=True)

# Show the interactive plot
fig.show()
