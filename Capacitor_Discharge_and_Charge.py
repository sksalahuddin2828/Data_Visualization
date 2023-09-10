import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

R = 100  # Resistance in ohms
C = 0.01  # Capacitance in Farads (for example)
V0 = 10  # Initial voltage in volts

tau = R * C
print(f"Time Constant (tau): {tau} seconds")

percent = 0.0025  # 0.250% in decimal form
discharge_time = -tau * np.log(1 - percent)
print(f"Discharge Time: {discharge_time} seconds")

charge_percent = 0.865
charge_time = tau * np.log(charge_percent)
print(f"Charge Time: {charge_time} seconds")

# Time values
t = np.linspace(0, 5 * tau, 500)  # Adjust the time range as needed

# Voltage during discharge
voltage_discharge = V0 * np.exp(-t / tau)

# Voltage during charge
voltage_charge = V0 * (1 - np.exp(-t / tau))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, voltage_discharge, label="Discharge")
plt.plot(t, voltage_charge, label="Charge")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (Volts)")
plt.title("Capacitor Discharge and Charge")
plt.legend()
plt.grid(True)
plt.show()
