import numpy as np
import matplotlib.pyplot as plt

# Circuit parameters
R = 100  # Resistance (Ohms)
C = 0.01  # Capacitance (Farads)
Qo = 0  # Initial charge (Coulombs)
tau = R * C  # Time constant

# Time values
t = np.linspace(0, 5 * tau, 1000)

# Charging process equation
Q = Qo * (1 - np.exp(-t / tau))

# Create the charge versus time graph
plt.figure(figsize=(10, 6))
plt.plot(t, Q)
plt.xlabel('Time (s)')
plt.ylabel('Charge (Coulombs)')
plt.title('Charging a Capacitor')
plt.grid(True)
plt.show()
