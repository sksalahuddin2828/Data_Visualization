import numpy as np
import sympy as sp

# Given values
R_bulb = 2.30  # Resistance of flashlight bulb in ohms
V_cell = 1.58  # Voltage of alkaline cell in volts
R_internal = 0.100  # Internal resistance of the cell in ohms

# (a) Calculate the current
V_total = V_cell
I = V_total / (R_bulb + R_internal)

# (b) Calculate the power supplied to the bulb using I^2R_bulb
P_bulb = I**2 * R_bulb

# (c) Calculate the power supplied to the bulb using V^2/R_bulb
P_bulb_alt = V_total**2 / R_bulb

# Display the results
print(f"(a) Current flowing through the bulb: {I:.2f} A")
print(f"(b) Power supplied to the bulb using I^2R_bulb: {P_bulb:.2f} W")
print(f"(c) Power supplied to the bulb using V^2/R_bulb: {P_bulb_alt:.2f} W")


# Answer: (a) Current flowing through the bulb: 0.66 A
#         (b) Power supplied to the bulb using I^2R_bulb: 1.00 W
#         (c) Power supplied to the bulb using V^2/R_bulb: 1.09 W
