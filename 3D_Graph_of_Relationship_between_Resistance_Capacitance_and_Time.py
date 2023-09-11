import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt

# Define symbols for resistance, capacitance, and time
R, C, t = symbols('R C t')

# Define the equation τ = RC
equation = Eq(R * C, t)

# Solve the equation for R * C
resistance = 10  # Example resistance value in ohms
capacitance = 5  # Example capacitance value in farads
time_result = solve(equation.subs({R: resistance, C: capacitance}), t)[0]

# Verify that the units are in seconds (s)
units_verification = (resistance, capacitance, time_result)
print(f"Resistance: {resistance} ohms")
print(f"Capacitance: {capacitance} farads")
print(f"Time (τ): {time_result} seconds")
print(f"Units Verification: Resistance * Capacitance = Time: {units_verification} seconds")

# Generate a range of resistance and capacitance values
resistance_values = np.linspace(1, 20, 100)
capacitance_values = np.linspace(1, 10, 100)
resistance_values, capacitance_values = np.meshgrid(resistance_values, capacitance_values)
time_values = resistance_values * capacitance_values

# Create a DataFrame for the 3D data
df = pd.DataFrame({'Resistance': resistance_values.flatten(),
                   'Capacitance': capacitance_values.flatten(),
                   'Time': time_values.flatten()})

# Create a 3D scatter plot using Plotly
fig = px.scatter_3d(df, x='Resistance', y='Capacitance', z='Time',
                     labels={'Resistance': 'Resistance (Ω)', 'Capacitance': 'Capacitance (F)', 'Time': 'Time (s)'},
                     title='Relationship between Resistance, Capacitance, and Time')
fig.show()

# Create an interactive 2D plot for Resistance vs. Time using Plotly
fig2 = px.scatter(df, x='Resistance', y='Time', trendline='ols', labels={'Resistance': 'Resistance (Ω)', 'Time': 'Time (s)'},
                 title='Resistance vs. Time')
fig2.update_traces(marker=dict(size=5))
fig2.show()

# Create a 2D plot for Capacitance vs. Time using Matplotlib
plt.figure(figsize=(8, 6))
plt.plot(df['Capacitance'], df['Time'], 'b.')
plt.xlabel('Capacitance (F)')
plt.ylabel('Time (s)')
plt.title('Capacitance vs. Time')
plt.grid(True)
plt.show()
