import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
import torch
import sklearn
import scipy

# Given parameters
resistance_between_hands = 10.0e3  # 10.0 kΩ
voltage_supply = 20.0e3  # 20.0 kV
internal_resistance = 2.0e3  # 2000 Ω

# Calculate total resistance in the circuit
total_resistance = resistance_between_hands + internal_resistance

# Calculate current through the body using Ohm's Law
current_through_body = voltage_supply / total_resistance

# Calculate power dissipated in the body
power_dissipated = current_through_body**2 * total_resistance

# Determine safe internal resistance
target_current = 1.0e-3  # 1.00 mA
safe_internal_resistance = (voltage_supply - target_current * resistance_between_hands) / target_current

# Check the impact on power supply for low-resistance devices
voltage_to_device = voltage_supply - current_through_body * internal_resistance

# Create a 3D visualization or mathematical dance here (Matplotlib can be used for creative plots)

# Present the results
print(f"Current through the body: {current_through_body:.2e} A")
print(f"Power dissipated in the body: {power_dissipated:.2e} W")
print(f"Safe internal resistance: {safe_internal_resistance:.2f} Ω")
print(f"Voltage supplied to low-resistance device: {voltage_to_device:.2e} V")


# Answer: Current through the body: 1.67e+00 A
#         Power dissipated in the body: 3.33e+04 W
#         Safe internal resistance: 19990000.00 Ω
#         Voltage supplied to low-resistance device: 1.67e+04 V
