import numpy as np
import pandas as pd
import sympy as sp

# (a) Current needed to transmit 100 MW at 25.0 kV
power = 100e6  # 100 MW in watts
voltage = 25e3  # 25.0 kV in volts
current = power / voltage
print(f"(a) Current needed: {current:.2f} A")

# (b) Power loss in a 1.00-Ω transmission line
line_resistance = 1.00  # Ω
current_loss = current  # Using the current calculated in (a)
power_loss = line_resistance * (current_loss ** 2)
print(f"(b) Power loss: {power_loss:.2f} W")

# (c) Percent power loss
percent_loss = (power_loss / power) * 100
print(f"(c) Percent loss: {percent_loss:.2f}%")
