import numpy as np
import pandas as pd
import sympy as sp

# Given values
Pave = 100e6  # 100 MW in watts
Vrms = 200e3  # 200 kV in volts
R = 1.0       # Resistance in ohms

# (a) Calculate the current (Irms = Pave / Vrms)
Irms = Pave / Vrms
print("Current:", Irms, "A")

# (b) Calculate power dissipated in the transmission lines
P_dissipated = Irms**2 * R
print("Power Dissipated:", P_dissipated, "W")

# (c) Calculate the percentage of power lost
percentage_loss = (P_dissipated / Pave) * 100
print("Percentage Loss:", percentage_loss, "%")
