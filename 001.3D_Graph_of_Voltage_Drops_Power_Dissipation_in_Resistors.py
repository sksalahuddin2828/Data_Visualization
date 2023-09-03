import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
from mpl_toolkits.mplot3d import Axes3D

# Define circuit parameters
V = 12.0  # Voltage output of the battery
R1 = 1.00
R2 = 6.00
R3 = 13.0

# Calculate circuit quantities
Rs = R1 + R2 + R3
I = V / Rs
V1 = I * R1
V2 = I * R2
V3 = I * R3
P1 = I**2 * R1
P2 = I**2 * R2
P3 = I**2 * R3

# Create DataFrame for voltage data
voltage_data = pd.DataFrame({'Resistor': ['R1', 'R2', 'R3'], 'Voltage (V)': [V1, V2, V3]})

# Create an interactive bar chart for voltage drops
fig_voltage = px.bar(voltage_data, x='Resistor', y='Voltage (V)', color='Resistor',
                     title='Voltage Drops in Resistors', labels={'Resistor': 'Resistor Number'})

fig_voltage.update_traces(marker_line_width=2, marker_line_color="black")
fig_voltage.update_layout(xaxis_title="Resistor Number", yaxis_title="Voltage (V)", showlegend=False)

# Create DataFrame for power data
power_data = pd.DataFrame({'Resistor': ['R1', 'R2', 'R3'], 'Power (W)': [P1, P2, P3]})

# Create an interactive pie chart for power dissipation
fig_power = px.pie(power_data, names='Resistor', values='Power (W)',
                   title='Power Dissipation in Resistors', hole=0.4)

fig_power.update_traces(textinfo='percent+label', pull=[0, 0.2, 0], 
                        marker=dict(colors=['red', 'green', 'blue']))

# Mathematical calculations and expressions
# Calculate total resistance symbolically
R_total = symbols('R_total')
eq = Eq(R_total, R1 + R2 + R3)
total_resistance = solve(eq, R_total)[0]

# Theoretical explanation
theory_text = f"The total resistance of the circuit is {total_resistance} Ω. " \
              f"The current flowing through the circuit is {I:.2f} A. " \
              "The voltage drop in each resistor is calculated using Ohm's law (V = IR). " \
              f"The power dissipated by each resistor is calculated as P = I^2 * R."

# Create a figure for the theoretical explanation
fig_theory = go.Figure()
fig_theory.add_trace(go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 0, 0, 0, 0], mode='text',
                               text=[theory_text, '', '', '', ''], showlegend=False))

# Display both plots side by side
fig_voltage.show()
fig_power.show()

# Display the theoretical explanation
fig_theory.update_xaxes(showticklabels=False)
fig_theory.update_yaxes(showticklabels=False)
fig_theory.update_layout(title_text="Theory and Equations", title_x=0.5)
fig_theory.show()

# 3D Visualization of Voltage Drops
fig_3d = plt.figure()
ax = fig_3d.add_subplot(111, projection='3d')

resistors = ['R1', 'R2', 'R3']
voltage_values = [V1, V2, V3]
colors = ['r', 'g', 'b']

ax.bar(resistors, voltage_values, zs=0, zdir='y', width=0.5, color=colors)

ax.set_xlabel('Resistors')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Current (A)')

plt.title("3D Voltage Drops Visualization")
plt.show()
