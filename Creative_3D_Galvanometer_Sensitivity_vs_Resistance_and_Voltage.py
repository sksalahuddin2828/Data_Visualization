import numpy as np
import sympy as sp
import pandas as pd
import plotly.express as px

# Define the variables
R_vol = 1e6  # 1.00 MΩ
V_scale = 30.0  # 30.0 V
I_galv = sp.Symbol('I_galv')  # Current in the galvanometer (sensitivity)

# Define the equation for sensitivity
sensitivity_eq = sp.Eq(V_scale, I_galv * R_vol)

# Solve for sensitivity
sensitivity_solution = sp.solve(sensitivity_eq, I_galv)

# Create a meshgrid for resistance and voltage
resistance_range = np.linspace(1e5, 1e7, 100)  # Range of resistance values (10^5 to 10^7 Ω)
voltage_range = np.linspace(10, 50, 100)  # Range of voltage values (10 to 50 V)
R, V = np.meshgrid(resistance_range, voltage_range)

# Convert the sensitivity equation to a numpy function
sensitivity_func = sp.lambdify(I_galv, sensitivity_solution[0], 'numpy')

# Calculate sensitivity for each combination of resistance and voltage
sensitivity = sensitivity_func(0.0)  # Pass 0.0 as a placeholder for I_galv

# Create a DataFrame for the data
data = pd.DataFrame({
    'Log(R)': np.log10(R.flatten()),  # Flatten R array
    'Voltage (V)': V.flatten(),  # Flatten V array
    'Sensitivity (A/V)': np.full_like(R, sensitivity).flatten(),  # Flatten sensitivity array
})

# Create an interactive 3D surface plot using Plotly Express
fig = px.scatter_3d(
    data,
    x='Log(R)',
    y='Voltage (V)',
    z='Sensitivity (A/V)',
    color='Sensitivity (A/V)',
    labels={'Sensitivity (A/V)': 'Sensitivity (A/V)'},
    title='Galvanometer Sensitivity vs. Resistance and Voltage',
    opacity=0.8,
)

# Customize the layout
fig.update_layout(scene=dict(
    xaxis_title='Log(R) (Ω)',
    yaxis_title='Voltage (V)',
    zaxis_title='Sensitivity (A/V)',
))

# Show the interactive plot
fig.show()
