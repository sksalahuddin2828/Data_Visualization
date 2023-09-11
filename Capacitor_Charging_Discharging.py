import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Constants
R = 1.0  # Resistance (Ohms)
C = 1.0  # Capacitance (Farads)
Q0 = 1.0  # Initial charge (Coulombs)
tau = R * C  # Time constant

# Time values
t = np.linspace(0, 5 * tau, 500)

# Charge functions for charging and discharging
Q_charging = Q0 * (1 - np.exp(-t / tau))
Q_discharging = Q0 * np.exp(-t / tau)

# Create plots
plt.figure(figsize=(12, 6))

# Plot charging
plt.subplot(121)
plt.plot(t, Q_charging, label='Charging')
plt.xlabel('Time (s)')
plt.ylabel('Charge (C)')
plt.title('Capacitor Charging')
plt.grid()
plt.legend()

# Plot discharging
plt.subplot(122)
plt.plot(t, Q_discharging, label='Discharging')
plt.xlabel('Time (s)')
plt.ylabel('Charge (C)')
plt.title('Capacitor Discharging')
plt.grid()
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
