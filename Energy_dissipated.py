import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint

V = 3.00  # Voltage (V)
P_avg = 0.500  # Average power (W)
t_flash = 0.250  # Effective flash duration (s)

# (a) Calculate energy dissipated
energy = P_avg * t_flash  # (a)

# (b) Calculate charge moved through the lamp using Q = P_avg * t_flash / V
Q = energy / V  # (b)

# (c) Capacitance calculation using Q = C * V
C = Q / V  # (c)

# (d) Calculate resistance using R = V^2 / P_avg
R = V**2 / P_avg  # (d)

print(f"(a) Energy dissipated: {energy} Joules")
print(f"(b) Charge moved through the lamp: {Q} Coulombs")
print(f"(c) Capacitance: {C} Farads")
print(f"(d) Resistance of the lamp: {R} Ohms")

# Answer: (a) Energy dissipated: 0.125 Joules
#         (b) Charge moved through the lamp: 0.041666666666666664 Coulombs
#         (c) Capacitance: 0.013888888888888888 Farads
#         (d) Resistance of the lamp: 18.0 Ohms
