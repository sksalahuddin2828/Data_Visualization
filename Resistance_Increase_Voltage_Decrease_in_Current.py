import numpy as np
import matplotlib.pyplot as plt

# Constants
R1 = 0.0200  # Resistance of ammeter in ohms
R2 = 10.00   # Resistance of the resistor in ohms
V = 12.0     # Voltage in volts (you can change this as needed)

# Part (b): Calculate Resistance of the Combination
R_total = R1 + R2

# Part (c): Calculate Percent Decrease in Current
I1 = V / R2
I2 = V / R_total
percent_decrease_current = ((I1 - I2) / I1) * 100

# Part (d): Calculate Percent Increase in Voltage
V1 = I1 * R2
V2 = I2 * R_total
percent_increase_voltage = ((V2 - V1) / V1) * 100

# Display results and visualizations
print("Total Resistance (R_total): {:.4f} ohms".format(R_total))
print("Percent Decrease in Current: {:.2f}%".format(percent_decrease_current))
print("Percent Increase in Voltage: {:.2f}%".format(percent_increase_voltage))

# Answer: Total Resistance (R_total): 10.0200 ohms
#         Percent Decrease in Current: 0.20%
#         Percent Increase in Voltage: 0.00%
