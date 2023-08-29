import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
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

# Visualization using matplotlib
plt.figure(figsize=(8, 6))
plt.bar(df['Scenario'], df['Current (mA)'])
plt.title('Current Through a Person in Different Scenarios')
plt.xlabel('Scenario')
plt.ylabel('Current (mA)')
plt.show()

# Visualization using plotly
fig = px.bar(df, x='Scenario', y='Current (mA)', title='Current Through a Person in Different Scenarios')
fig.show()

# Mathematical dance with sympy
x = sp.symbols('x')
equation = sp.Eq(x**2 + 2*x + 1, 0)
solutions = sp.solve(equation, x)
print("Solutions to the equation:", solutions)
