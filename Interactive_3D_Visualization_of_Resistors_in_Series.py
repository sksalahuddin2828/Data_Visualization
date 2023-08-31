import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px

# Given resistances
total_resistance = 0.500e6  # 0.500 MΩ
first_resistance = 900e3     # 900 kΩ

# Calculate the second resistance in series
second_resistance = total_resistance - first_resistance

# Generate data for interactive plot
resistor_values = np.linspace(0, 1e6, 100)
second_resistor_values = total_resistance - resistor_values
data = {'First Resistor': resistor_values, 'Second Resistor': second_resistor_values, 'Total Resistance': total_resistance}

df = pd.DataFrame(data)

# Create an interactive scatter plot using Plotly Express
fig = px.scatter_3d(df, x='First Resistor', y='Second Resistor', z='Total Resistance',
                    title='Interactive 3D Visualization of Resistors in Series',
                    labels={'First Resistor': 'First Resistor (Ω)', 'Second Resistor': 'Second Resistor (Ω)', 'Total Resistance': 'Total Resistance (Ω)'})

# Show the plot
fig.show()
