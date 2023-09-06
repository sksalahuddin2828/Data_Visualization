# Import necessary libraries
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define constants
emf_nicad = 1.25  # Nicad cell emf (V)
emf_alkaline = 1.58  # Alkaline cell emf (V)
resistance_radio = 3.20  # Radio resistance (Ω)
internal_resistance_nicad = 0.0400  # Internal resistance of Nicad cell (Ω)
internal_resistance_alkaline = 0.200  # Internal resistance of Alkaline cell (Ω)

# Create a range of load resistances for visualization
load_resistances = np.linspace(0, 10, 100)

# Calculate power delivered for Nicad and Alkaline cells
power_nicad = (emf_nicad ** 2 * load_resistances) / ((internal_resistance_nicad + load_resistances) ** 2)
power_alkaline = (emf_alkaline ** 2 * load_resistances) / ((internal_resistance_alkaline + load_resistances) ** 2)

# Create a Pandas DataFrame for data manipulation
df = pd.DataFrame({
    'Load Resistance (Ω)': load_resistances,
    'Power Nicad (W)': power_nicad,
    'Power Alkaline (W)': power_alkaline
})

# Create interactive Plotly visualizations
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                    subplot_titles=('Power vs. Load Resistance (Nicad)', 'Power vs. Load Resistance (Alkaline)'))

# Add power vs. load resistance traces
fig.add_trace(go.Scatter(x=df['Load Resistance (Ω)'], y=df['Power Nicad (W)'],
                         mode='lines', name='Nicad', line=dict(color='blue')), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Load Resistance (Ω)'], y=df['Power Alkaline (W)'],
                         mode='lines', name='Alkaline', line=dict(color='green')), row=2, col=1)

# Update layout and axis labels
fig.update_layout(
    title='Power Delivered to Radio vs. Load Resistance',
    xaxis=dict(title='Load Resistance (Ω)'),
    yaxis=dict(title='Power (Watts)'),
)

# Create interactive sliders for battery voltage and internal resistance
battery_voltage_slider = dict(value=emf_nicad, currentvalue=dict(prefix="Battery Voltage (V): "), step=0.01)
internal_resistance_slider = dict(value=internal_resistance_nicad, currentvalue=dict(prefix="Internal Resistance (Ω): "), step=0.01)

# Create interactive sliders for battery voltage and internal resistance
battery_voltage_slider = dict(currentvalue=dict(prefix="Battery Voltage (V): "), steps=[
    {"args": [[emf_nicad], {"frame": {"duration": 300, "redraw": True}, "transition": {"duration": 300}}],
     "label": "Nicad", "method": "animate", "value": emf_nicad},
    {"args": [[emf_alkaline], {"frame": {"duration": 300, "redraw": True}, "transition": {"duration": 300}}],
     "label": "Alkaline", "method": "animate", "value": emf_alkaline},
])

internal_resistance_slider = dict(currentvalue=dict(prefix="Internal Resistance (Ω): "), steps=[
    {"args": [[internal_resistance_nicad], {"frame": {"duration": 300, "redraw": True}, "transition": {"duration": 300}}],
     "label": "Nicad", "method": "animate", "value": internal_resistance_nicad},
    {"args": [[internal_resistance_alkaline], {"frame": {"duration": 300, "redraw": True}, "transition": {"duration": 300}}],
     "label": "Alkaline", "method": "animate", "value": internal_resistance_alkaline},
])

# Create an interactive slider for battery type (Nicad or Alkaline)
battery_type_slider = dict(
    currentvalue={"prefix": "Battery Type: "},
    steps=[
        {"label": "Nicad", "method": "update", "args": [{"visible": [True, False]}]},
        {"label": "Alkaline", "method": "update", "args": [{"visible": [False, True]}]}
    ],
)

# Update the layout to include sliders
fig.update_layout(
    sliders=[battery_type_slider, battery_voltage_slider, internal_resistance_slider],
)

# Show the interactive plot
fig.show()
