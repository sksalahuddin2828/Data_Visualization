import numpy as np
import sympy as sp
import pandas as pd
import plotly.express as px

# Given resistor values
resistor_values = [36.0, 50.0, 700.0]

# Calculate all possible combinations of resistor values
combinations = []
for i in range(2**len(resistor_values)):
    combination = []
    for j in range(len(resistor_values)):
        if (i >> j) & 1:
            combination.append(resistor_values[j])
    if len(combination) == len(resistor_values):  # Check if all resistors are used
        combinations.append(combination)

# Calculate the equivalent resistance for each combination
equivalent_resistances = []
for combination in combinations:
    equivalent_resistance = np.sum(1 / np.array(combination))
    equivalent_resistances.append(equivalent_resistance)

# Find the largest and smallest equivalent resistances
largest_resistance = max(equivalent_resistances)
smallest_resistance = min(equivalent_resistances)

# Create a DataFrame for the results
data = pd.DataFrame({
    'Resistor 1 (ohms)': [comb[0] for comb in combinations],
    'Resistor 2 (ohms)': [comb[1] for comb in combinations],
    'Equivalent Resistance (ohms)': equivalent_resistances
})

# Print the results
print(f"Largest Resistance: {largest_resistance} ohms")
print(f"Smallest Resistance: {smallest_resistance} ohms")

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(data, x='Resistor 1 (ohms)', y='Resistor 2 (ohms)', z='Equivalent Resistance (ohms)',
                    color='Equivalent Resistance (ohms)', opacity=0.7, title='Equivalent Resistance Combinations')
fig.update_layout(scene=dict(xaxis_title='Resistor 1 (ohms)', yaxis_title='Resistor 2 (ohms)',
                             zaxis_title='Equivalent Resistance (ohms)'))
fig.show()
