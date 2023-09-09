import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
import torch
from sklearn.linear_model import LinearRegression
from scipy.optimize import fsolve

# Step 2: Calculate the Resistance for the Galvanometer to be Used as a Voltmeter
galvanometer_resistance = 40.0  # Ω
sensitivity = 25.0e-6  # A
full_scale_voltage = 0.500e-3  # V

# Calculate the required series resistance
required_resistance = full_scale_voltage / sensitivity - galvanometer_resistance
print(f"Required resistance in series: {required_resistance:.2f} Ω")

# Step 3: Explain Unreasonability and Assumptions
# Include a textual explanation of what is unreasonable and the assumptions responsible.

# Step 4: Create a 3D Visualization
# Generate data points
sensitivity_range = np.linspace(1e-6, 50e-6, 100)
full_scale_voltage_range = np.linspace(1e-3, 1, 100)
sensitivity_mesh, full_scale_voltage_mesh = np.meshgrid(sensitivity_range, full_scale_voltage_range)

# Calculate required resistance for each combination
required_resistance_mesh = full_scale_voltage_mesh / sensitivity_mesh - galvanometer_resistance

# Create a 3D plot using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(sensitivity_mesh, full_scale_voltage_mesh, required_resistance_mesh)

# Label the axes
ax.set_xlabel('Sensitivity (A)')
ax.set_ylabel('Full-scale Voltage (V)')
ax.set_zlabel('Required Resistance (Ω)')

# Show the plot
plt.title('Required Resistance for Galvanometer to be Used as a Voltmeter')
plt.show()

# Step 4 (alternative): Create an Interactive 3D Plot using Plotly
fig = px.scatter_3d(x=sensitivity_mesh.flatten(), y=full_scale_voltage_mesh.flatten(), z=required_resistance_mesh.flatten())
fig.update_layout(scene=dict(xaxis_title='Sensitivity (A)', yaxis_title='Full-scale Voltage (V)', zaxis_title='Required Resistance (Ω)'),
                  title='Required Resistance for Galvanometer to be Used as a Voltmeter')
fig.show()

# Step 5: Enhance Data Presentation with Pandas and Numpy
# Create a dataframe to store the sensitivity, full-scale voltage, and required resistance data
data = {'Sensitivity (A)': sensitivity_mesh.flatten(),
        'Full-scale Voltage (V)': full_scale_voltage_mesh.flatten(),
        'Required Resistance (Ω)': required_resistance_mesh.flatten()}
df = pd.DataFrame(data)

# Display the first few rows of the dataframe
print(df.head())
