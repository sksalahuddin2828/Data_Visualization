import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Constants
R = 500  # Resistance in ohms
C = 1.50e-6  # Capacitance in farads
E = 6.16  # EMF in volts
t = np.linspace(0, 5, 100)  # Time values for visualization
RC = R * C  # RC time constant

# (a) Initial current (I0)
I0 = E / R

# (b) RC time constant
RC = R * C

# (c) Current after one time constant (t = RC)
t1 = RC
I1 = I0 * np.exp(-t1 / RC)

# (d) Voltage on the capacitor after one time constant (t = RC)
Vc1 = E * (1 - np.exp(-t1 / RC))

# Create a symbolic expression for current as a function of time
t_sym = sp.symbols('t')
I_sym = I0 * sp.exp(-t_sym / RC)

# Create a symbolic expression for voltage on the capacitor as a function of time
Vc_sym = E * (1 - sp.exp(-t_sym / RC))

# Visualization using matplotlib
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot current as a function of time
ax.plot(t, I0 * np.exp(-t / RC), t, np.zeros_like(t), t, np.ones_like(t) * I1, lw=2)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Current (A)')
ax.set_zlabel('Current vs. Time')
ax.set_title('Current vs. Time')
ax.legend(['Initial Current', 'Zero Current', 'Current after 1 Time Constant'])

# Save the 3D plot as an image
plt.savefig('current_vs_time.png')
plt.show()

# Visualization for voltage on the capacitor
plt.figure(figsize=(8, 6))
plt.plot(t, E * (1 - np.exp(-t / RC)), lw=2)
plt.xlabel('Time (s)')
plt.ylabel('Voltage on Capacitor (V)')
plt.title('Voltage on Capacitor vs. Time')
plt.grid(True)
plt.savefig('voltage_on_capacitor.png')
plt.show()

# Display symbolic expressions for I(t) and Vc(t)
print(f"I(t) = {I_sym}")
print(f"Vc(t) = {Vc_sym}")
