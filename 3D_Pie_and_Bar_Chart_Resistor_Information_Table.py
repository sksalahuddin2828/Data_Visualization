import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define the resistor values
R1 = 10  # Ohms
R2 = 20  # Ohms
R3 = 30  # Ohms

# Define the total resistance in series
Rs = R1 + R2 + R3

# Define the voltage source
V = 50  # Volts

# Calculate the current using Ohm's law (I = V / Rs)
I = V / Rs

# Calculate the voltage drops across each resistor
V1 = I * R1
V2 = I * R2
V3 = I * R3

# Create a pie chart to visualize voltage drops
labels = ['R1', 'R2', 'R3']
voltages = [V1, V2, V3]
colors = ['#ff9999', '#66b3ff', '#99ff99']

fig_pie = go.Figure(data=[go.Pie(labels=labels, values=voltages, textinfo='percent+label', marker=dict(colors=colors))])
fig_pie.update_layout(title='Voltage Drops Across Resistors in Series (Pie Chart)')

# Create a bar chart to visualize voltage drops
resistors = ['R1', 'R2', 'R3']
voltages = [V1, V2, V3]

fig_bar = go.Figure(data=[go.Bar(x=resistors, y=voltages, marker=dict(color=colors))])
fig_bar.update_layout(title='Voltage Drops Across Resistors in Series (Bar Chart)', xaxis_title='Resistor', yaxis_title='Voltage Drop (V)')

# Symbolic representation of the equation V = V1 + V2 + V3
V, V1, V2, V3 = sp.symbols('V V1 V2 V3')
eq = sp.Eq(V, V1 + V2 + V3)
solution = sp.solve(eq, V)
symbolic_equation = f'Symbolic equation: {eq}'

# Extract numeric values from SymPy expressions
V1_numeric = V1.evalf(subs={V: solution[0]})
V2_numeric = V2.evalf(subs={V: solution[0]})
V3_numeric = V3.evalf(subs={V: solution[0]})
symbolic_solution_numeric = solution[0].evalf()

# Create a Pandas DataFrame to display calculations with numeric values
data = {'Resistor': ['R1', 'R2', 'R3', 'Total'],
        'Resistance (Ω)': [R1, R2, R3, Rs],
        'Voltage Drop (V)': [V1_numeric, V2_numeric, V3_numeric, symbolic_solution_numeric],
        'Current (A)': [I, I, I, I]}
df = pd.DataFrame(data)

# Create subplots for visualization
fig_subplots = make_subplots(rows=1, cols=2, subplot_titles=('Voltage Drops (Bar Chart)', 'Symbolic Equation'))

# Add figures to subplots
fig_subplots.add_trace(fig_bar.data[0], row=1, col=1)
fig_subplots.add_trace(go.Scatter(x=[0], y=[0], text=[symbolic_equation], mode='text'), row=1, col=2)

# Update subplot layout
fig_subplots.update_layout(
    title_text='Resistor Network Analysis',
    title_x=0.5,
    title_font=dict(size=24),
    showlegend=False
)

# Display the pie chart and subplots side by side
fig_pie.show()
fig_subplots.show()

# Create a separate figure for the table with numeric values
fig_table = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Resistor, df['Resistance (Ω)'], df['Voltage Drop (V)'], df['Current (A)']],
               fill_color='lavender',
               align='left'))
])
fig_table.update_layout(title='Resistor Information Table')

# Show the table with numeric values separately
fig_table.show()
