import numpy as np

# Function to calculate the normal operating voltage of each bulb in a series circuit
def calculate_voltage_in_series(total_voltage, num_bulbs):
    return total_voltage / num_bulbs

# Function to calculate the operating voltage of each bulb in a series circuit with one burnt-out bulb
def calculate_voltage_with_burnt_out(total_voltage, num_bulbs, remaining_bulbs):
    return total_voltage / remaining_bulbs

# Constants
total_voltage = 120  # Total voltage in the circuit
num_bulbs = 40      # Number of bulbs in the circuit
remaining_bulbs = 39  # Number of remaining bulbs when one burns out

# Calculate the normal operating voltage of each bulb
normal_voltage = calculate_voltage_in_series(total_voltage, num_bulbs)
print(f"Normal operating voltage of each bulb: {normal_voltage} V")

# Calculate the operating voltage of each bulb with one burnt-out bulb
voltage_with_burnt_out = calculate_voltage_with_burnt_out(total_voltage, num_bulbs, remaining_bulbs)
print(f"Operating voltage of each bulb with one burnt-out bulb: {voltage_with_burnt_out} V")

# Answer: Normal operating voltage of each bulb: 3.0 V
#         Operating voltage of each bulb with one burnt-out bulb: 3.076923076923077 V
