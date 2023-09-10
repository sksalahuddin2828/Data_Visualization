import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio

# Capacitor and resistor values
capacitors = [2.00e-6, 7.50e-6]
resistors = [25.0e3, 100.0e3]
time = np.linspace(0, 0.02, 200)  # Time values for simulation (0 to 20 ms)

# Create a DataFrame to store data
data = pd.DataFrame(columns=["Resistance (Ohms)", "Capacitance (Farads)", "Time (s)", "Voltage (V)"])

# Calculate voltage across the capacitor for different combinations
for C in capacitors:
    for R in resistors:
        voltage = 5.0 * (1 - np.exp(-time / (R * C)))  # Voltage across the capacitor in an RC circuit
        data = data.append({"Resistance (Ohms)": R, "Capacitance (Farads)": C, "Time (s)": time, "Voltage (V)": voltage}, ignore_index=True)

# Create an animated plot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])
animation_frames = []
for _, row in data.iterrows():
    trace = go.Scatter(x=row["Time (s)"], y=row["Voltage (V)"], name=f'RC={row["Resistance (Ohms)"]}/{row["Capacitance (Farads)"]}')
    animation_frames.append(go.Frame(data=[trace], name=str(row.name)))
fig.add_trace(animation_frames[0].data[0])

# Define animation settings
animation_settings = dict(frame=dict(duration=100, redraw=True), fromcurrent=True)

# Create buttons to control animation
play_button = dict(label='Play', method='animate', args=[None, animation_settings])
pause_button = dict(label='Pause', method='animate', args=[[None], animation_settings])
reset_button = dict(label='Reset', method='animate', args=[[0], animation_settings])

# Set layout and axis labels
fig.update_layout(title='Charging and Discharging of Capacitors in an RC Circuit',
                  xaxis_title='Time (s)',
                  yaxis_title='Voltage (V)')

# Show the plot
pio.show(fig)
