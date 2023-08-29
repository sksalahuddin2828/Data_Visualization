import numpy as np
import pandas as pd
import plotly.graph_objects as go
import sympy as sp
from sympy.plotting import plot

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

# Mathematical expressions and visualizations with sympy
x = sp.symbols('x')
equation = sp.Eq(x**2 + 2*x + 1, 0)
solutions = sp.solve(equation, x)
print("Solutions to the equation:", solutions)

# Plot the equation
p = plot(equation.rhs, show=False)
p.title = "Plot of $x^2 + 2x + 1$"
p.xlabel = 'x'
p.ylabel = 'y'
p.show()

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

# Animation using Plotly (Placeholder for illustration)
frames = []

# For each frame, update the bar heights
for i in range(1, 21):
    frame = go.Frame(data=[go.Bar(
        x=df['Scenario'],
        y=df['Current (mA)'] * i / 20,
        text=df['Current (mA)'],
        textposition='auto',
        marker_color=['rgba(255, 100, 100, 0.7)', 'rgba(100, 100, 255, 0.7)']
    )])
    frames.append(frame)

fig.frames = frames

# Set animation settings
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                          method='animate',
                                          args=[None, {'frame': {'duration': 200, 'redraw': True}, 'fromcurrent': True, 'transition': {'duration': 0}}]),
                                                                                     dict(label='Pause',
                                                                                          method='animate',
                                                                                          args=[[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate', 'transition': {'duration': 0}}])])])

# Show the animation
fig.show()
