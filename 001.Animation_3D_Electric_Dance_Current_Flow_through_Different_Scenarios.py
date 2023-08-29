import numpy as np
import pandas as pd
import plotly.graph_objects as go
import sympy as sp
from sympy.plotting import plot
from IPython.display import display, HTML

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
display(df)

# Mathematical expressions and visualizations with sympy
x = sp.symbols('x')
equation = sp.Eq(x**2 + 2*x + 1, 0)
solutions = sp.solve(equation, x)
display(HTML("<b>Solutions to the equation:</b>"))
display(solutions)

# Plot the equation
p = plot(equation.rhs, show=False)
p.title = "Plot of $x^2 + 2x + 1$"
p.xlabel = 'x'
p.ylabel = 'y'
p.show()

# Create an animated electric dance visualization using Plotly
t = np.linspace(0, 2*np.pi, 100)
rubber_currents = current_rubber * np.sin(t)
grass_currents = current_wet_grass * np.sin(t)

fig = go.Figure()

fig.add_trace(go.Scatter(x=t, y=rubber_currents, mode='lines', name='Rubber Mat'))
fig.add_trace(go.Scatter(x=t, y=grass_currents, mode='lines', name='Wet Grass'))

fig.update_layout(
    title='Electric Dance: Current Flow through Different Scenarios',
    xaxis_title='Time',
    yaxis_title='Current (mA)',
    font=dict(family='Arial', size=14),
    plot_bgcolor='rgba(240, 240, 240, 0.8)',
    legend=dict(x=0.02, y=0.98)
)

frames = []

for i in np.linspace(0, 2*np.pi, 36):
    frame_data = [go.Scatter(x=t, y=rubber_currents * np.sin(i), mode='lines', name='Rubber Mat'),
                  go.Scatter(x=t, y=grass_currents * np.sin(i), mode='lines', name='Wet Grass')]
    frames.append(go.Frame(data=frame_data))

fig.frames = frames

animation_settings = {
    'frame': {'duration': 100, 'redraw': True},
    'fromcurrent': True,
    'transition': {'duration': 0}
}

fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play', method='animate', args=[None, animation_settings]),
                                                                             dict(label='Pause', method='animate', args=[[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate'}])])])

# Display the animation
fig.show()
