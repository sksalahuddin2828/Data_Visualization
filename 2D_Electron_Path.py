import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
m = 9.11e-31  # Mass of an electron in kg
v = 6.00e7  # Velocity of the electron in m/s
q = 1.60e-19  # Charge of an electron in C
B = 0.500  # Magnetic field strength in T

# Calculate radius of curvature
r = (m * v) / (q * B)

# Create a pandas DataFrame for clear presentation
data = {
    "Quantity": ["Mass (m)", "Velocity (v)", "Charge (q)", "Magnetic Field (B)", "Radius (r)"],
    "Value": [m, v, q, B, r],
    "Unit": ["kg", "m/s", "C", "T", "m"]
}

df = pd.DataFrame(data)

# 3D Visualization of Electron Path
t = np.linspace(0, 2 * np.pi, 100)  # Time points
x = r * np.cos(t)  # X-coordinate
y = r * np.sin(t)  # Y-coordinate

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the path of the electron
ax.plot(x, y, t, label='Electron Path')

# Label axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Time')
ax.legend()

# Show the plot
plt.show()

# Display the DataFrame
print(df)
