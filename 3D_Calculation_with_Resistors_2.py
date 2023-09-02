import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp

# Resistances in ohms
resistor_values = [1e2, 2.5e3, 4e3]
resistor_names = ['R1', 'R2', 'R3']

# Create a DataFrame to store resistor data
resistor_df = pd.DataFrame({'Resistor': resistor_names, 'Resistance (Ohms)': resistor_values})

# Calculate total resistance in series
total_resistance_series = np.sum(resistor_values)

# Calculate total resistance in parallel
total_resistance_parallel = 1 / np.sum(1 / np.array(resistor_values))

# Equivalent resistance in series formula
eq_series = 'R_eq_series = R1 + R2 + R3'

# Equivalent resistance in parallel formula
eq_parallel = '1 / R_eq_parallel = 1 / R1 + 1 / R2 + 1 / R3'

# Explanation for series and parallel resistors
series_explanation = "In a series connection, resistors are connected end to end, and their resistances simply add up."
parallel_explanation = "In a parallel connection, the reciprocal of the equivalent resistance is the sum of the reciprocals of the individual resistances."

# Create symbolic variables for equations
R1, R2, R3, R_eq_series, R_eq_parallel = sp.symbols('R1 R2 R3 R_eq_series R_eq_parallel')

# Define equations
eq_series = sp.Eq(R_eq_series, R1 + R2 + R3)
eq_parallel = sp.Eq(1 / R_eq_parallel, 1 / R1 + 1 / R2 + 1 / R3)

# Solve for equivalent resistances
eq_series_solution = sp.solve(eq_series.subs({R1: resistor_values[0], R2: resistor_values[1], R3: resistor_values[2]}), R_eq_series)
eq_parallel_solution = sp.solve(eq_parallel.subs({R1: resistor_values[0], R2: resistor_values[1], R3: resistor_values[2]}), R_eq_parallel)

# Convert SymPy solutions to numeric values
eq_series_value = float(eq_series_solution[0])
eq_parallel_value = float(eq_parallel_solution[0])

# Display the equivalent resistances
print(f"Total Resistance in Series: {total_resistance_series:.2f} ohms")
print(f"Total Resistance in Parallel: {total_resistance_parallel:.2f} ohms")
print(f"Equivalent Resistance in Series: {eq_series_value:.2f} ohms")
print(f"Equivalent Resistance in Parallel: {eq_parallel_value:.2f} ohms")

# Create an interactive 3D plot using Plotly
fig = px.scatter_3d(resistor_df, x='Resistor', y='Resistance (Ohms)', z='Resistance (Ohms)',
                    text='Resistor', title='Resistors in 3D')

# Customize the plot appearance
fig.update_traces(marker=dict(size=5, symbol='square', opacity=0.7),
                  selector=dict(mode='markers+text'))

# Update axis labels
fig.update_layout(scene=dict(xaxis_title='Resistor', yaxis_title='', zaxis_title='Resistance (Ohms)'),
                  scene_camera=dict(up=dict(x=0, y=0, z=1)))

# Show the interactive plot
fig.show()

# Display mathematical equations and explanations
print("\nMathematical Equations and Explanations:")
print(f"Equivalent Resistance in Series: ${sp.latex(eq_series)}$ - {series_explanation}")
print(f"Equivalent Resistance in Parallel: ${sp.latex(eq_parallel)}$ - {parallel_explanation}")
