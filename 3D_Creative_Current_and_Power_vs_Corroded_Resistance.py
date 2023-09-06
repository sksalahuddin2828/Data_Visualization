import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
from plotly.subplots import make_subplots

battery_voltage = 12.0  # V
internal_resistance_battery = 0.0100  # Ω
starter_motor_resistance = 0.0500  # Ω
corroded_resistance = 0.0900  # Ω

total_resistance = internal_resistance_battery + starter_motor_resistance
current = battery_voltage / total_resistance
print(f"Current to the motor: {current:.4f} A")

voltage_applied = current * starter_motor_resistance
print(f"Voltage applied to the motor: {voltage_applied:.4f} V")

power = current * voltage_applied
print(f"Power supplied to the motor: {power:.4f} W")

# Create a range of corroded resistances
corroded_resistances = np.linspace(0.0100, 0.1000, 100)

# Calculate current, voltage, and power for each corroded resistance
currents = battery_voltage / (internal_resistance_battery + corroded_resistances)
voltages = currents * starter_motor_resistance
powers = currents * voltages

# Create a Pandas DataFrame
data = pd.DataFrame({'Corroded Resistance (Ω)': corroded_resistances,
                     'Current (A)': currents,
                     'Power (W)': powers})

# Create an interactive line plot using Plotly Express
fig = px.line(data, x='Corroded Resistance (Ω)', y=['Current (A)', 'Power (W)'],
              title='Current and Power vs. Corroded Resistance')
fig.update_xaxes(title_text='Corroded Resistance (Ω)')
fig.update_yaxes(title_text='Value')
fig.show()

# Define a symbolic variable for the resistance
R = sp.symbols('R')

# Create an expression for power as a function of resistance
power_expression = (battery_voltage**2 * R) / (R**2 + (internal_resistance_battery + starter_motor_resistance)**2)

# Plot the power function using SymPy
sp.plot(power_expression, (R, 0.01, 0.1), show=False, title='Power vs. Resistance')

# Create a figure with subplots for animations
fig = make_subplots(rows=1, cols=2, subplot_titles=['Voltage vs. Time', 'Current vs. Time'])

# Create a time vector
time = np.linspace(0, 10, 100)

# Initialize lists to store animation frames
frames_voltage = []
frames_current = []

# Create animated visualizations
for t in time:
    voltage_t = battery_voltage * np.sin(t)  # Simulating voltage variation
    current_t = voltage_t / total_resistance
    frames_voltage.append(go.Scatter(x=[t], y=[voltage_t], mode='lines+markers', name='Voltage', line=dict(color='blue')))
    frames_current.append(go.Scatter(x=[t], y=[current_t], mode='lines+markers', name='Current', line=dict(color='red')))

# Add animations using animation_frame
for frame in frames_voltage:
    fig.add_trace(frame, row=1, col=1)

for frame in frames_current:
    fig.add_trace(frame, row=1, col=2)

# Update layout
fig.update_xaxes(title_text='Time (s)', row=1, col=1)
fig.update_xaxes(title_text='Time (s)', row=1, col=2)
fig.update_yaxes(title_text='Voltage (V)', row=1, col=1)
fig.update_yaxes(title_text='Current (A)', row=1, col=2)

# Show the animated plot
fig.show()
