import sympy as sp
import numpy as np
import pandas as pd
import plotly.express as px

# Define symbols
t, V0, R, C = sp.symbols('t V0 R C')

# Define the equation
equation = sp.Eq(V0 * sp.exp(-t / (R * C)), 0)

# Calculate the discharge time numerically
from scipy.optimize import fsolve

# Define a function to find the root of the equation
def find_discharge_time(t):
    return V0_val * np.exp(-t / (R_val * C_val))

# Initial guess for the root
initial_guess = 0.1  # You may need to adjust this based on your specific case

# Find the root (time to reach zero voltage)
time_to_zero = fsolve(find_discharge_time, initial_guess)

print(f"Time to reach zero voltage: {time_to_zero[0]} seconds")

# Generate discharge curve data
t_vals = np.linspace(0, float(time_to_zero[0]), 100)
V_vals = [V0_val * np.exp(-t / (R_val * C_val)) for t in t_vals]

# Create a DataFrame for the data
df = pd.DataFrame({'Time (s)': t_vals, 'Voltage (V)': V_vals})

# Create an interactive 3D plot using Plotly
fig = px.line_3d(df, x='Time (s)', y='Voltage (V)', z='Voltage (V)', title='Capacitor Discharge')
fig.update_traces(line=dict(width=4))  # Adjust line width for visibility

# Show the Plotly figure
fig.show()
