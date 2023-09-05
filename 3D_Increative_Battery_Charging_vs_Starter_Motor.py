import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Constants
emf = 12.0  # Volts
internal_resistance = 0.050  # Ohms
current_charge = 60.0  # Amperes
current_starter = 60.0  # Amperes

# (a) Potential difference across terminals during charging
voltage_charge = emf - current_charge * internal_resistance

# (b) Rate of thermal energy dissipation during charging
thermal_energy_charge = current_charge ** 2 * internal_resistance

# (c) Rate of electric energy conversion to chemical energy during charging
electric_to_chemical_charge = voltage_charge * current_charge

# (d) Potential difference and thermal energy during starter motor use
voltage_starter = emf - current_starter * internal_resistance
thermal_energy_starter = current_starter ** 2 * internal_resistance

# Create a Pandas DataFrame
data = pd.DataFrame({
    'Process': ['Charging', 'Starter'],
    'Potential Difference (Volts)': [voltage_charge, voltage_starter],
    'Thermal Energy Dissipation (Watts)': [thermal_energy_charge, thermal_energy_starter]
})

# Create a 3D Scatter plot using Plotly
fig = px.scatter_3d(data, x='Process', y='Potential Difference (Volts)',
                    z='Thermal Energy Dissipation (Watts)',
                    text='Process', title='Battery Charging vs. Starter Motor',
                    labels={'Process': 'Process Name'},
                    template='plotly_dark')

# Add mathematical expressions as annotations
annotations = [
    go.layout.Annotation(
        x='Charging', y=voltage_charge, text=f'Potential Difference = {voltage_charge} V',
        showarrow=True, arrowhead=2, ax=10, ay=-30, font=dict(size=10, color='white'),
        bordercolor='#c7c7c7', borderwidth=2, borderpad=4, bgcolor='black', opacity=0.8),
    go.layout.Annotation(
        x='Starter', y=voltage_starter, text=f'Potential Difference = {voltage_starter} V',
        showarrow=True, arrowhead=2, ax=-10, ay=30, font=dict(size=10, color='white'),
        bordercolor='#c7c7c7', borderwidth=2, borderpad=4, bgcolor='black', opacity=0.8)
]

# Update the layout with annotations
fig.update_layout(annotations=annotations)

# Show the interactive Plotly 3D plot
fig.show()
