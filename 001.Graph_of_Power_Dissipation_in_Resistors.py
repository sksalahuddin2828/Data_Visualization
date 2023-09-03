import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
import plotly.graph_objects as go

V = 12.0  # Voltage output of the battery
R1 = 1.00
R2 = 6.00
R3 = 13.0

Rs = R1 + R2 + R3
I = V / Rs
V1 = I * R1
V2 = I * R2
V3 = I * R3
P1 = I**2 * R1
P2 = I**2 * R2
P3 = I**2 * R3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.bar(['R1', 'R2', 'R3'], [V1, V2, V3], zs=0, zdir='y', width=0.5, color=['r', 'g', 'b'])

ax.set_xlabel('Resistors')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Current (A)')

plt.show()

voltage_data = pd.DataFrame({'Resistor': ['R1', 'R2', 'R3'], 'Voltage (V)': [V1, V2, V3]})

fig = px.bar(voltage_data, x='Resistor', y='Voltage (V)', color='Resistor', title='Voltage Drops in Resistors')
fig.show()

power_data = pd.DataFrame({'Resistor': ['R1', 'R2', 'R3'], 'Power (W)': [P1, P2, P3]})

plt.pie(power_data['Power (W)'], labels=power_data['Resistor'], autopct='%1.1f%%', startangle=90)
plt.title('Power Dissipation in Resistors')
plt.show()
