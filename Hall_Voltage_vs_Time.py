import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Constants
L = 0.075  # Length of the wire (in meters)
v = 0.1  # Velocity of the wire (in m/s)
B = 1.5  # Magnetic field strength (in Tesla)

# Calculate the induced Hall voltage
E = v * B  # Electric field induced (Hall voltage)

# Create a 3D visualization of the wire's motion and the magnetic field
t = np.linspace(0, 1, 100)
x = L * t
y = np.zeros_like(t)
z = np.zeros_like(t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Wire Path', linewidth=2)
ax.quiver(0, 0, 0, 0, 0, B, label='Magnetic Field', color='r', alpha=0.5, linewidth=0.5, arrow_length_ratio=0.1)

# Plot the Hall voltage as a function of time
t_values = np.linspace(0, 1, 100)
E_values = np.full_like(t_values, E)

plt.figure()
plt.plot(t_values, E_values)
plt.xlabel('Time (s)')
plt.ylabel('Hall Voltage (V)')
plt.title('Hall Voltage vs Time')

# Add mathematical expressions
sp.init_printing()
L, v, B, t, E = sp.symbols('L v B t E')
expr = sp.Eq(E, v * B)
display(expr)

# Show the 3D plot and mathematical expressions
plt.show()
