import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

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

# Create interactive 3D scatter plot
fig = make_subplots(rows=1, cols=2,
                    specs=[[{'type': 'surface'}, {'type': 'scatter'}]],
                    subplot_titles=('Terminal Voltage vs. Load and Internal Resistance',
                                    'Power Dissipated vs. Load Resistance'))

# 3D Surface Plot for Terminal Voltage
surface_plot = go.Surface(x=df['Load Resistance (Ω)'], y=df['Internal Resistance (Ω)'],
                          z=df['Terminal Voltage (V)'], colorscale='Viridis')
fig.add_trace(surface_plot, row=1, col=1)

# Scatter Plot for Power Dissipated vs. Load Resistance
scatter_plot_power = go.Scatter(x=df['Load Resistance (Ω)'], y=df['Power Dissipated (W)'],
                                mode='lines', name='Power Dissipated')
fig.add_trace(scatter_plot_power, row=1, col=2)

# Update subplot titles and axis labels
fig.update_layout(title_text='Battery Analysis',
                  xaxis=dict(title='Load Resistance (Ω)'),
                  coloraxis=dict(colorbar_title='Value'))

# Add annotations with mathematical expressions
annotations = [
    dict(
        x=df['Load Resistance (Ω)'].max(),
        y=df['Internal Resistance (Ω)'].max(),
        text=f"Terminal Voltage = {emf} - ({emf} / (R_internal + 10)) * R_load",
        showarrow=False,
        font=dict(size=10)
    ),
    dict(
        x=df['Load Resistance (Ω)'].max(),
        y=df['Internal Resistance (Ω)'].min(),
        text=f"Power Dissipated = ({emf} / (R_internal + 10)) * R_load) ^ 2 * 10",
        showarrow=False,
        font=dict(size=10)
    )
]
fig.update_layout(annotations=annotations)

# Show the interactive plot
fig.show()
