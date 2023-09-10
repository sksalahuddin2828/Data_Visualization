import numpy as np

# Given values
C = 160e-6  # Capacitance in Farads
R = 31.2e3  # Resistance in Ohms

# Calculate the time constant
tau = R * C
print(f"The time constant (τ) is {tau} seconds")

# Given values
V = 450  # Voltage in Volts
m = 2.50e-3  # Mass in kg
c = 1.67e3  # Specific heat capacity in J/(kg°C)

# Calculate the energy dissipated in the resistor
Q = 0.5 * C * V**2

# Calculate the temperature increase
delta_T = Q / (m * c)
print(f"The temperature increase is {delta_T} °C")

# Given resistivity of pure carbon at room temperature (25°C)
rho_room_temp = 1.0e-5  # Ohm-meter

# Calculate the new resistance at the elevated temperature
new_R = R * (1 + delta_T / 25)  # Assuming a linear relationship with temperature
print(f"The new resistance is {new_R} Ohms")

# Answer: The time constant (τ) is 4.992 seconds
#         The temperature increase is 3.8802395209580847 °C
#         The new resistance is 36042.53892215569 Ohms
