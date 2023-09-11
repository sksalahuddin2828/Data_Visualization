import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt

# Define symbols for the variables
R, C, V, t = sp.symbols('R C V t')

# Define the RC time constant (τ) equation
tau = R * C

# Define the current equation (I) as a function of time
I = (V / R) * sp.exp(-t / tau)

# Create a function to calculate τ and I for given R and V values
def calculate_tau_and_current(R_value, V_value):
    tau_value = float(tau.subs({R: R_value, C: 1}))  # Convert to float
    return tau_value

# Example usage:
R_values = np.linspace(1, 20, 20)  # Range of resistance values
V_value = 100  # Fixed voltage

# Calculate τ for the range of resistance values
tau_values = [calculate_tau_and_current(R_value, V_value) for R_value in R_values]

# Create a DataFrame for the results
data = pd.DataFrame({'Resistance (R)': R_values, 'RC Time Constant (τ)': tau_values})

# Create 3D surface plot of τ vs. R
fig = px.scatter_3d(data, x='Resistance (R)', y='RC Time Constant (τ)', z=np.zeros(len(R_values)))
fig.update_traces(marker=dict(size=5), selector=dict(mode='markers'))
fig.update_layout(scene=dict(zaxis_title=''))
fig.update_layout(title='RC Time Constant vs. Resistance',
                  scene_aspectmode='cube',
                  scene=dict(xaxis_title='Resistance (R)', yaxis_title='RC Time Constant (τ)'))

# Show the 3D plot
fig.show()

# Plot τ and I as functions of time for a specific resistance
R_value = 10  # Selected resistance
tau = calculate_tau_and_current(R_value, V_value)
t_values = np.linspace(0, 5 * tau, 100)
I_values = [(V_value / R_value) * np.exp(-t_value / tau) for t_value in t_values]

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.plot(t_values, I_values)
plt.xlabel('Time')
plt.ylabel('Current (I)')
plt.title(f'Current vs. Time for R = {R_value}')

plt.tight_layout()
plt.show()
