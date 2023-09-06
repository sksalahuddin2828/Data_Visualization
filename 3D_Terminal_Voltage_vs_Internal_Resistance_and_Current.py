import numpy as np
import sympy as sp
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given data
delta_V = 2.00  # Change in terminal voltage (in volts)
delta_I = 5.00  # Change in current supplied (in amperes)

# Define variables
R_internal = sp.Symbol('R_internal')  # Internal resistance (in ohms)
I = sp.Symbol('I')  # Current supplied (in amperes)
V_emf = sp.Symbol('V_emf')  # Electromotive force (in volts)

# Ohm's Law: V = E - I * R, where V is terminal voltage, E is emf, and R is internal resistance
equation = sp.Eq(delta_V, V_emf - (I + delta_I) * (R_internal))

# Solve for internal resistance
internal_resistance_solution = sp.solve(equation, R_internal)

# Check if emf can be found
if internal_resistance_solution:
    emf_value = sp.solve(sp.Eq(delta_V, V_emf - I * internal_resistance_solution[0]), V_emf)
    if emf_value:
        emf = float(emf_value[0])  # Convert SymPy expression to float
        print(f"Internal Resistance: {internal_resistance_solution[0]} ohms")
        print(f"Electromotive Force (emf): {emf} volts")
    else:
        print("Emf cannot be determined with the given information.")
else:
    print("Internal resistance solution not found.")

# Create a Pandas DataFrame for visualization
df = pd.DataFrame({'Internal Resistance (ohms)': np.linspace(0, 10, 100)})
df['Current (A)'] = I_values = np.linspace(0, 10, 100)
df['Terminal Voltage (V)'] = emf - (I_values + delta_I) * df['Internal Resistance (ohms)']

# Convert DataFrame to NumPy arrays
internal_resistance_values = df['Internal Resistance (ohms)'].to_numpy()
terminal_voltage_values = df['Terminal Voltage (V)'].to_numpy()

# Create an interactive 3D scatter plot using Plotly Express
fig1 = px.scatter_3d(df, x=internal_resistance_values, y=I_values, z=terminal_voltage_values,
                      title='Terminal Voltage vs Internal Resistance and Current')
fig1.update_traces(marker=dict(size=5))
fig1.show()

# Create an interactive 2D plot using Plotly
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=internal_resistance_values, y=terminal_voltage_values,
                         mode='lines', name='Terminal Voltage vs Internal Resistance'))
fig2.update_xaxes(title='Internal Resistance (ohms)')
fig2.update_yaxes(title='Terminal Voltage (V)')
fig2.update_layout(title='Terminal Voltage vs Internal Resistance',
                   xaxis=dict(showline=True, linewidth=2),
                   yaxis=dict(showline=True, linewidth=2))
fig2.show()
