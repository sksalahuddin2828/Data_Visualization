import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Data Preparation
voltage = 12.0
resistor_values = [4, 6, 9]
current_series = voltage / np.array(resistor_values)
current_parallel = voltage / np.sum(1 / np.array(resistor_values))
power_series = current_series ** 2 * np.array(resistor_values)
power_parallel = current_parallel ** 2 * np.array(resistor_values)

# Create a pandas DataFrame for easy data manipulation
df = pd.DataFrame({
    'Resistor': ['R1', 'R2', 'R3'],
    'Resistance (Ohms)': resistor_values,
    'Current (A) - Series': current_series,
    'Current (A) - Parallel': current_parallel,
    'Power (W) - Series': power_series,
    'Power (W) - Parallel': power_parallel
})

# Latex formatting for equations
sp.init_printing(use_latex=True)
V, R, I, P = sp.symbols('V R I P')
eq_current_series = sp.Eq(I, V / R)
eq_power_series = sp.Eq(P, I**2 * R)
eq_current_parallel = sp.Eq(I, V / (R + R + R))
eq_power_parallel = sp.Eq(P, I**2 * (R + R + R))

# Display equations
display(eq_current_series, eq_power_series, eq_current_parallel, eq_power_parallel)

# Create a Plotly table for data display
table = go.Figure(data=[go.Table(
    header=dict(values=['Resistor', 'Resistance (Ohms)', 'Current (A) - Series', 'Current (A) - Parallel',
                        'Power (W) - Series', 'Power (W) - Parallel'],
                fill=dict(color='lightblue'),
                align='left'),
    cells=dict(values=[df['Resistor'], df['Resistance (Ohms)'], df['Current (A) - Series'], df['Current (A) - Parallel'],
                       df['Power (W) - Series'], df['Power (W) - Parallel']],
               fill=dict(color='lightgray'),
               align='left'))
])

# Create an interactive bar chart using Plotly
fig = px.bar(df, x='Resistor', y=['Power (W) - Series', 'Power (W) - Parallel'],
             title='Power Dissipation in Series vs. Parallel', labels={'Resistor': 'Resistors', 'value': 'Power (W)'})
fig.update_traces(marker_color=['blue', 'red'])
fig.update_layout(xaxis_title="Resistors", yaxis_title="Power (W)")
fig.update_layout(barmode='group')

# Create a beautiful Matplotlib visualization with LaTeX formatting for equations
def power_formatter(x, pos):
    return r'$%1.1f \, \mathrm{W}$' % x

formatter = FuncFormatter(power_formatter)
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(df['Resistor'], df['Power (W) - Series'], label='Series', color='blue', alpha=0.6)
ax.bar(df['Resistor'], df['Power (W) - Parallel'], label='Parallel', color='red', alpha=0.6)
ax.set_xlabel('Resistors')
ax.set_ylabel('Power (W)')
ax.set_title('Power Dissipation in Series vs. Parallel')
ax.yaxis.set_major_formatter(formatter)
ax.legend()

# Show the Plotly table and interactive chart
table.show()

# Show the Matplotlib visualization
plt.show()
