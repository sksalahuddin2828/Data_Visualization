import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sympy import Symbol, Eq, solve
import math

# Define the given values
emf = 10.0  # EMF of the battery in volts
load_resistance = 0.500  # Load resistance in ohms

# Calculate current using Ohm's Law (V = IR)
I = emf / load_resistance

# Calculate power dissipated using P = I^2 * R
P_load = I**2 * load_resistance

# Create a DataFrame to store the data
df = pd.DataFrame({
    'EMF (Volts)': [emf],
    'Load Resistance (Ohms)': [load_resistance],
    'Current (A)': [I],
    'Power (Watts)': [P_load]
})

# Visualization using Plotly
# Create a scatter plot for the battery characteristics
fig = px.scatter(df, x='Load Resistance (Ohms)', y='Current (A)',
                 title='Battery Characteristics', labels={'Load Resistance (Ohms)': 'Load Resistance'},
                 text='Power (Watts)')

# Customize the plot
fig.update_traces(marker=dict(size=12), selector=dict(mode='markers+text'))
fig.update_xaxes(title_text='Load Resistance (Ohms)')
fig.update_yaxes(title_text='Current (A)')
fig.update_layout(autosize=False, width=600, height=500)

# Create a 3D surface plot for power dissipation
emf_values = np.linspace(1.0, 15.0, 100)
load_resistance_values = np.linspace(0.1, 1.0, 100)
EMF, Load_Resistance = np.meshgrid(emf_values, load_resistance_values)
Power = (EMF / Load_Resistance)**2 * Load_Resistance

surface_fig = go.Figure(data=[go.Surface(z=Power, x=EMF, y=Load_Resistance)])
surface_fig.update_layout(scene=dict(zaxis_title='Power (Watts)', xaxis_title='EMF (Volts)',
                                     yaxis_title='Load Resistance (Ohms)'),
                         title='Power Dissipation in Battery Circuit')
surface_fig.update_layout(autosize=False, width=600, height=500)

# Mathematical expression and equation solving using SymPy
V, I, R = Symbol('V'), Symbol('I'), Symbol('R')
equation = Eq(V, I * R)
current_equation = equation.subs({V: emf, R: load_resistance})
current_solution = solve(current_equation, I)[0]

print(f'Current (I) = {current_solution:.2f} A')
print(f'Power Dissipation (P) = {P_load:.2f} W')

# Show the Plotly plots
fig.show()
surface_fig.show()
