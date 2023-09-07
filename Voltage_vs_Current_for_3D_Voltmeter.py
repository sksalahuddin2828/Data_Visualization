import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import plotly.graph_objects as go

# Define Constants
R_voltmeter = 25.0e3  # Resistance of the voltmeter in ohms
V_scale = 100.0       # Voltage scale in volts

# Calculate Sensitivity (Current for Full-Scale Deflection)
I_sensitivity = V_scale / R_voltmeter

# Define Symbolic Variables for Mathematical Expression
I, V, R = sp.symbols('I V R')

# Create Mathematical Expression
ohms_law_expr = sp.Eq(V, I * R)

# Solve for Current (I) at Full-Scale Deflection
sensitivity_equation = ohms_law_expr.subs([(V, V_scale), (R, R_voltmeter)])
sensitivity_solution = sp.solve(sensitivity_equation, I)[0]

# Convert to Numeric Value
sensitivity_numeric = float(sensitivity_solution.evalf())

# Print Sensitivity
print(f"Sensitivity of the galvanometer (Current for Full-Scale Deflection): {sensitivity_numeric} A")

# Data for Visualization
current_values = np.linspace(0, I_sensitivity * 2, 100)
voltage_values = current_values * R_voltmeter

# Create Pandas DataFrame
data = pd.DataFrame({'Current (A)': current_values, 'Voltage (V)': voltage_values})

# Create Plotly 3D Scatter Plot
fig = px.scatter_3d(data, x='Current (A)', y='Voltage (V)', z='Voltage (V)',
                    title='Voltage vs. Current for Voltmeter')
fig.update_traces(marker=dict(size=3), selector=dict(mode='markers+text'))
fig.update_layout(scene=dict(xaxis_title='Current (A)', yaxis_title='Voltage (V)', zaxis_title='Voltage (V)'))

# Create a Table
table = go.Figure(data=[go.Table(
    header=dict(values=["Current (A)", "Voltage (V)"]),
    cells=dict(values=[data['Current (A)'], data['Voltage (V)']])
)])

# Show Sensitivity Point
sensitivity_point = pd.DataFrame({'Current (A)': [I_sensitivity], 'Voltage (V)': [V_scale]})
fig.add_trace(go.Scatter3d(x=sensitivity_point['Current (A)'], y=sensitivity_point['Voltage (V)'],
                           z=sensitivity_point['Voltage (V)'], mode='markers+text',
                           text='Sensitivity Point', textposition='top right',
                           marker=dict(size=5, color='red')))

# Display the 3D Scatter Plot and Table
fig.show()
table.show()
