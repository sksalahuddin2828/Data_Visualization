import numpy as np
import pandas as pd
import plotly.graph_objects as go
import sympy as sp

# Given data
voltage = 120  # Voltage in volts
resistance_rubber = 300e3  # Resistance in ohms
resistance_wet_grass = 4000e3  # Resistance in ohms

# Calculate current using Ohm's law: I = V / R
current_rubber = voltage / resistance_rubber
current_wet_grass = voltage / resistance_wet_grass

# Create a DataFrame to present the results
data = {
    'Scenario': ['Rubber Mat', 'Wet Grass'],
    'Resistance (kΩ)': [resistance_rubber / 1e3, resistance_wet_grass / 1e3],
    'Current (mA)': [current_rubber * 1e3, current_wet_grass * 1e3]
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Custom visualization using Plotly
fig = go.Figure()

fig.add_trace(go.Bar(
    x=df['Scenario'],
    y=df['Current (mA)'],
    text=df['Current (mA)'],
    textposition='auto',
    marker_color=['rgba(255, 100, 100, 0.7)', 'rgba(100, 100, 255, 0.7)']
))

fig.update_layout(
    title='Current Through a Person in Different Scenarios',
    xaxis_title='Scenario',
    yaxis_title='Current (mA)',
    font=dict(family='Arial', size=14),
    plot_bgcolor='rgba(240, 240, 240, 0.8)'
)

fig.show()

# Mathematical dance with sympy
x = sp.symbols('x')
equation = sp.Eq(x**2 + 2*x + 1, 0)
solutions = sp.solve(equation, x)
print("Solutions to the equation:", solutions)
