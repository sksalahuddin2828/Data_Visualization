import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
C = 8.00e-6  # Capacitance (F)
R = 1.00e3   # Resistance (Ω)
V_initial = 10.0e3  # Initial voltage (V)
V_final = 5.00e2    # Final voltage (V)

# Part (a) - Calculate the time constant (τ)
tau = R * C

# Part (b) - Calculate the time it takes to decline to V_final
t = -tau * np.log(V_final / V_initial)

# Create a 3D visualization of the exponential decay
t_values = np.linspace(0, 3 * tau, 1000)  # Time values
V_values = V_initial * np.exp(-t_values / tau)  # Voltage values

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(t_values, V_values, t_values, lw=2)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Time (s)')
ax.set_title('Capacitor Discharge Over Time')
plt.show()

# Print results
print(f"(a) Time Constant (τ): {tau:.4f} seconds")
print(f"(b) Time to Decline to {V_final} V: {t:.4f} seconds")
