import numpy as np
import sympy as sp

# Given values
Vrms = 120  # RMS voltage in volts
Irms = 10   # RMS current in amperes
R = 10      # Resistance in ohms

# Calculate average power using different formulas
Pave_formula1 = Irms * Vrms
Pave_formula2 = Vrms**2 / R
Pave_formula3 = (Irms**2) * R

print("Average Power (Formula 1):", Pave_formula1)
print("Average Power (Formula 2):", Pave_formula2)
print("Average Power (Formula 3):", Pave_formula3)


# Answer: Average Power (Formula 1): 1200
#         Average Power (Formula 2): 1440.0
#         Average Power (Formula 3): 1000