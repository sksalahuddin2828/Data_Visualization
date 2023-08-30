import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import matplotlib.pyplot as plt
from scipy.constants import e

# Given data
current = 10.0  # A
time = 5.00e-3  # seconds
energy_dissipated = 500  # J
mass = 8.00  # kg

# Calculate charge passed
charge = current * time

# Calculate voltage applied
voltage = energy_dissipated / charge

# Calculate resistance
resistance = voltage / current

# Calculate temperature increase using specific heat capacity of tissue
specific_heat_tissue = 3500  # J/kg°C
temperature_increase = energy_dissipated / (mass * specific_heat_tissue)

# Display results
print("Charge passed:", charge, "C")
print("Voltage applied:", voltage, "V")
print("Resistance:", resistance, "ohms")
print("Temperature increase:", temperature_increase, "°C")

# Create symbolic variables for equations
I, t, Q, V, R, m, c, ΔT = sp.symbols('I t Q V R m c ΔT')

# Define equations and solve for specific variables
equations = {
    Q: I * t,
    V: energy_dissipated / Q,
    R: V / I,
    ΔT: energy_dissipated / (m * c),
}

# Explain the equations using LaTeX-style expressions
equation_explanations = {
    Q: "Charge (C) = Current (A) \\times Time (s)",
    V: "Voltage (V) = Energy (J) / Charge (C)",
    R: "Resistance (Ω) = Voltage (V) / Current (A)",
    ΔT: "Temperature Increase (°C) = Energy (J) / (Mass (kg) \\times Specific Heat (J/kg°C))",
}

# Display equations with explanations
for symbol, explanation in equation_explanations.items():
    display(sp.Eq(symbol, equations[symbol]))
    print(explanation)

# Create a DataFrame for visualization
data = {'Parameter': ['Charge Passed', 'Voltage Applied', 'Resistance', 'Temperature Increase'],
        'Value': [charge, voltage, resistance, temperature_increase]}
df = pd.DataFrame(data)

# Create an interactive bar plot using Plotly Express
fig_bar = px.bar(df, x='Parameter', y='Value', title='Electrical Parameters and Temperature Increase')
fig_bar.update_traces(marker_color='blue')

# Display interactive bar plot
fig_bar.show()

# Create an animation for current path through tissue
fig_animation = px.scatter_3d(x=x, y=y, z=z, title='Electrical Current Path Through Tissue Animation',
                              animation_frame=x, range_x=[0, cube_size], range_y=[0, cube_size], range_z=[0, cube_size])
fig_animation.update_traces(marker=dict(size=4, color='blue'))

# Display animation
fig_animation.show()
