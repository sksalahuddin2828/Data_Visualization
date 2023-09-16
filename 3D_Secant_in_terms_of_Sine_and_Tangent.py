import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Define the symbolic variable theta
theta = sp.symbols('theta')

# Calculate secant in terms of sine
sec_sine = 1 / sp.sqrt(1 - sp.sin(theta)**2)

# Calculate secant in terms of tangent
sec_tangent = sp.sqrt(1 + sp.tan(theta)**2)

# Create numpy functions for secant in terms of sine and tangent
sec_sine_func = sp.lambdify(theta, sec_sine, 'numpy')
sec_tangent_func = sp.lambdify(theta, sec_tangent, 'numpy')

# Generate data for theta values
theta_values = np.linspace(0, 2 * np.pi, 100)
sin_values = np.sin(theta_values)
tan_values = np.tan(theta_values)

# Calculate secant values
sec_sine_values = sec_sine_func(theta_values)
sec_tangent_values = sec_tangent_func(theta_values)

# Create a DataFrame for the data
data = pd.DataFrame({
    'Theta': theta_values,
    'Sin(theta)': sin_values,
    'Tan(theta)': tan_values,
    'Secant in terms of Sine': sec_sine_values,
    'Secant in terms of Tangent': sec_tangent_values
})

# Create an interactive 3D surface plot for Secant in terms of Sine
fig1 = px.scatter_3d(data, x='Theta', y='Sin(theta)', z='Secant in terms of Sine', title='Secant in Terms of Sine')
fig1.update_traces(marker=dict(size=5))

# Create an interactive 3D surface plot for Secant in terms of Tangent
fig2 = px.scatter_3d(data, x='Theta', y='Tan(theta)', z='Secant in terms of Tangent', title='Secant in Terms of Tangent')
fig2.update_traces(marker=dict(size=5))

# Show the interactive plots
fig1.show()
fig2.show()
