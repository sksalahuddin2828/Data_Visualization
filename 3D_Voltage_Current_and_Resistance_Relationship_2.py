import numpy as np
import pandas as pd
import sympy as sp
import plotly.express as px
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the given values
V1 = 120  # Voltage for the first device (in volts)
V2 = 240  # Voltage for the second device (in volts)
P = 1000  # Power consumption for both devices (in watts)

# Calculate resistance ratios
R1 = V1**2 / P
R2 = V2**2 / P
resistance_ratio = R2 / R1

# Calculate current ratios
I1 = V1 / R1
I2 = V2 / R2
current_ratio = I2 / I1

# Calculate power increase factor
power_increase_factor = (V2 / V1)**2

# Create a Pandas DataFrame for tabular representation
data = {'Device': ['Device 1', 'Device 2'],
        'Voltage (V)': [V1, V2],
        'Current (A)': [I1, I2],
        'Resistance (Ω)': [R1, R2]}
df = pd.DataFrame(data)

# Create an interactive bar chart using Plotly
bar_fig = px.bar(df, x='Device', y='Current (A)', title='Current Consumption Comparison',
                 text='Current (A)', color='Device', labels={'Current (A)': 'Current'})
bar_fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')

# Create an interactive scatter plot using Plotly
scatter_fig = px.scatter(df, x='Resistance (Ω)', y='Current (A)', title='Resistance vs. Current',
                         text='Device', color='Device', labels={'Resistance (Ω)': 'Resistance', 'Current (A)': 'Current'})
scatter_fig.update_traces(textposition='top center')

# Explanation of concepts using LaTeX equations
equation_text = (
    "Resistance (R) = \\frac{Voltage (V)^2}{Power (P)}\n"
    "Current (I) = \\frac{Voltage (V)}{Resistance (R)}\n"
    "Power Increase Factor = \\left(\\frac{Voltage_2}{Voltage_1}\\right)^2"
)

# Create a 3D visualization using Matplotlib
voltage_range = np.linspace(0, 300, 100)
current_range = np.linspace(0, 10, 100)
voltage_grid, current_grid = np.meshgrid(voltage_range, current_range)
resistance_grid = voltage_grid / current_grid

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(voltage_grid, current_grid, resistance_grid, cmap='viridis')
ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Current (A)')
ax.set_zlabel('Resistance (Ω)')
ax.set_title('Voltage, Current, and Resistance Relationship')

# Display the plots and explanations
plt.show()
bar_fig.show()
scatter_fig.show()
print(equation_text)
