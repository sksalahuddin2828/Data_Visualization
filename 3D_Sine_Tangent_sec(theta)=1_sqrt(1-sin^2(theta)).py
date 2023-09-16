import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt

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
theta_values = np.linspace(0, 2 * np.pi, 400)
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

# Explanation
explanation = """
The secant function can be expressed in terms of sine and tangent as follows:

1. Secant in terms of Sine:
   sec(theta) = 1 / sqrt(1 - sin^2(theta))

2. Secant in terms of Tangent:
   sec(theta) = sqrt(1 + tan^2(theta))

Here, we calculate and visualize these secant functions for a range of theta values. 
The 3D surface plots show how secant varies with respect to sine and tangent.

In the plot for "Secant in terms of Sine," we see that secant approaches infinity 
whenever sin(theta) is close to 1 or -1 (dividing by zero). It's undefined at these points.

In the plot for "Secant in terms of Tangent," secant approaches infinity whenever tan(theta) is undefined, 
which occurs when cos(theta) is zero (dividing by zero).

Please note that these plots provide insights into the behavior of secant in relation to 
sine and tangent for various theta values.
"""

# Create an interactive 3D surface plot for Secant in terms of Sine
fig1 = px.scatter_3d(data, x='Theta', y='Sin(theta)', z='Secant in terms of Sine', title='Secant in Terms of Sine')
fig1.update_traces(marker=dict(size=5))

# Create an interactive 3D surface plot for Secant in terms of Tangent
fig2 = px.scatter_3d(data, x='Theta', y='Tan(theta)', z='Secant in terms of Tangent', title='Secant in Terms of Tangent')
fig2.update_traces(marker=dict(size=5))

# Show the interactive plots
fig1.show()
fig2.show()

# Display the explanation
print(explanation)

# Plot secant in terms of theta
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.plot(theta_values, sec_sine_values, label='sec(theta) = 1 / sqrt(1 - sin^2(theta))')
plt.xlabel('Theta')
plt.ylabel('sec(theta)')
plt.title('Secant in Terms of Sine')
plt.legend()

plt.subplot(122)
plt.plot(theta_values, sec_tangent_values, label='sec(theta) = sqrt(1 + tan^2(theta))')
plt.xlabel('Theta')
plt.ylabel('sec(theta)')
plt.title('Secant in Terms of Tangent')
plt.legend()

plt.tight_layout()
plt.show()
