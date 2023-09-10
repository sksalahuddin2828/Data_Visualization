import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
C = 100e-12  # Capacitance in Farads
R = 75e6    # Resistance in Ohms
Vf = 1.0    # Final voltage
Vi = 0.0    # Initial voltage
t = sp.symbols('t')  # Time as a symbol

# Exponential charging equation
Vt = Vi + (Vf - Vi) * (1 - sp.exp(-t / (R * C)))

# Solve for the time when Vt reaches 90% of Vf
target_voltage = 0.90 * Vf
solution = sp.solve(Vt - target_voltage, t)

if solution:
    charging_time = float(solution[0])
else:
    charging_time = None

# Create a 3D visualization
time_values = np.linspace(0, charging_time, 100)
voltage_values = [float(Vt.subs(t, t_val)) for t_val in time_values]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Charge')

ax.plot(time_values, voltage_values, np.zeros_like(time_values), label='Charge Curve')
ax.scatter(charging_time, target_voltage, 0, color='red', label=f'90% of Final Voltage ({charging_time:.2f}s)')
ax.legend()

plt.title('Capacitor Charging Dynamics')
plt.show()

# Print the charging time
if charging_time is not None:
    print(f"Time required to charge the capacitor to 90% of its final voltage: {charging_time:.2f} seconds")
else:
    print("The capacitor cannot reach 90% of its final voltage in a reasonable time.")
