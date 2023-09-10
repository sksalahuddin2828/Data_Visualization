import sympy as sp

# Define symbols
R_flash = 0.0400  # Flash lamp resistance (Ω)
RC_constant = 0.100e-6  # RC time constant (s)
R_charge = 800e3  # Charging resistance (Ω)

# Define symbols
C, τ = sp.symbols('C τ')

# Solve for C in part (a)
eq_a = sp.Eq(RC_constant, R_flash * C)
capacitor_value_expr = sp.solve(eq_a, C)[0]  # Get the symbolic expression

# Solve for τ in part (b)
eq_b = sp.Eq(τ, R_charge * C)
time_constant_expr = sp.solve(eq_b, τ)[0]  # Get the symbolic expression

# Evaluate the expressions numerically
capacitor_value = sp.N(capacitor_value_expr)
time_constant = sp.N(time_constant_expr)

print(f"Capacitor Value: {capacitor_value} F")
print(f"Time Constant: {time_constant} s")

# Answer: Capacitor Value: 0.00000250000000000000 F
#         Time Constant: 800000.0*C s


import sympy as sp
import pandas as pd
import numpy as np
import plotly.express as px

# Define symbols
R_flash = 0.0400  # Flash lamp resistance (Ω)
RC_constant = 0.100e-6  # RC time constant (s)
R_charge = 800e3  # Charging resistance (Ω)

# Define symbols
C, τ = sp.symbols('C τ')

# Solve for C in part (a)
eq_a = sp.Eq(RC_constant, R_flash * C)
capacitor_value_expr = sp.solve(eq_a, C)[0]  # Get the symbolic expression

# Solve for τ in part (b)
eq_b = sp.Eq(τ, R_charge * C)
time_constant_expr = sp.solve(eq_b, τ)[0]  # Get the symbolic expression

# Evaluate the expressions numerically
capacitor_value = sp.N(capacitor_value_expr)
time_constant = sp.N(time_constant_expr)

# Create a DataFrame with string values
data = {'Parameter': ['Capacitor Value (F)', 'Time Constant (s)'],
        'Value': [str(capacitor_value), str(time_constant)]}
df = pd.DataFrame(data)

# Create a bar chart
fig = px.bar(df, x='Parameter', y='Value', text='Value', title='Capacitor and Time Constant Calculation')
fig.update_traces(textposition='outside')
fig.update_layout(yaxis_title='Value')
fig.show()

# Create 3D visualization
resistance_values = np.linspace(0.01, 0.2, 100)
capacitance_values = np.linspace(1e-6, 10e-6, 100)
time_constant_values = resistance_values * capacitance_values

fig_3d = px.scatter_3d(x=resistance_values, y=capacitance_values, z=time_constant_values,
                        labels={'x': 'Resistance (Ω)', 'y': 'Capacitance (F)', 'z': 'Time Constant (s)'},
                        title='3D Relationship between Resistance, Capacitance, and Time Constant')
fig_3d.show()
