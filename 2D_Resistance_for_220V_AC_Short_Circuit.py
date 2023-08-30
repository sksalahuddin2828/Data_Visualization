import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
import torch
import sklearn
import scipy

# Given data
voltage_a = 220  # Volts
power_peak_kw = 96.8  # kW

# (a) Calculate resistance for 220V AC short circuit
# Convert power to watts
power_peak_w = power_peak_kw * 1000

# Using P = V^2 / R, solve for resistance
resistance_a = voltage_a**2 / power_peak_w

# (b) Calculate average power for 120V AC voltage
voltage_b = 120  # Volts

# Using P = V^2 / R, solve for power
power_avg_w = voltage_b**2 / resistance_a

# Print results
print("Resistance for 220V AC short circuit:", resistance_a, "ohms")
print("Average power for 120V AC voltage:", power_avg_w, "Watts")

# Create a plot
voltages = np.linspace(100, 250, 100)
powers = voltages**2 / resistance_a

plt.figure(figsize=(10, 6))
plt.plot(voltages, powers)
plt.xlabel("Voltage (V)")
plt.ylabel("Power (W)")
plt.title("Power vs. Voltage")
plt.grid(True)
plt.show()
