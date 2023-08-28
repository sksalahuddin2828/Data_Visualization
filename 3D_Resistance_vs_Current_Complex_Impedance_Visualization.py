import numpy as np
import pandas as pd
import sympy as sp
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Define the given values
V1 = 120  # Voltage for the first device (in volts)
V2 = 240  # Voltage for the second device (in volts)
P = 1000  # Power consumption for both devices (in watts)

# Calculate resistance ratios, current ratios, and power increase factor
R1 = V1**2 / P
R2 = V2**2 / P
resistance_ratio = R2 / R1
I1 = V1 / R1
I2 = V2 / R2
current_ratio = I2 / I1
power_increase_factor = (V2 / V1)**2

# Create a Pandas DataFrame for tabular representation
data = {'Device': ['Device 1', 'Device 2'],
        'Voltage (V)': [V1, V2],
        'Current (A)': [I1, I2],
        'Resistance (Ω)': [R1, R2]}
df = pd.DataFrame(data)

# Create interactive visualizations using Plotly
bar_fig = px.bar(df, x='Device', y='Current (A)', title='Current Consumption Comparison',
                 text='Current (A)', color='Device', labels={'Current (A)': 'Current'})
bar_fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')

scatter_fig = px.scatter(df, x='Resistance (Ω)', y='Current (A)', title='Resistance vs. Current',
                         text='Device', color='Device', labels={'Resistance (Ω)': 'Resistance', 'Current (A)': 'Current'})
scatter_fig.update_traces(textposition='top center')

# Explanation of concepts using LaTeX equations and additional theory
equation_text = (
    "Resistance (R) = \\frac{Voltage (V)^2}{Power (P)}\n"
    "Current (I) = \\frac{Voltage (V)}{Resistance (R)}\n"
    "Power Increase Factor = \\left(\\frac{Voltage_2}{Voltage_1}\\right)^2"
)

theory_text = (
    "When voltage increases while power remains constant, resistance and current must change accordingly.\n"
    "Higher voltage leads to increased current and altered resistance values."
)

# Create an animated complex impedance visualization using Plotly
t = np.linspace(0, 2*np.pi, 100)
Z1 = R1 * np.exp(1j*t)  # Complex impedance for Device 1
Z2 = R2 * np.exp(1j*t)  # Complex impedance for Device 2

fig = go.Figure()

# Add traces for complex impedance
fig.add_trace(go.Scatter(x=Z1.real, y=Z1.imag, mode='lines', name='Device 1'))
fig.add_trace(go.Scatter(x=Z2.real, y=Z2.imag, mode='lines', name='Device 2'))

fig.update_layout(title='Complex Impedance Visualization',
                  xaxis_title='Real Part of Impedance',
                  yaxis_title='Imaginary Part of Impedance')

# Display the interactive complex impedance visualization
fig.show()

# Display the animated plot and other visualizations
HTML(ani.to_jshtml())
bar_fig.show()
scatter_fig.show()
print(equation_text)
print(theory_text)
