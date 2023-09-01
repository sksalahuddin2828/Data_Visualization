import numpy as np
import sympy as sp

# Constants
voltage = 120  # Volts
fuse_current = 15  # Amperes

# Power ratings of devices
toaster_power = 1800  # Watts
frying_pan_power = 1400  # Watts
lamp_power = 75  # Watts

# Calculate currents
toaster_current = toaster_power / voltage
frying_pan_current = frying_pan_power / voltage
lamp_current = lamp_power / voltage

# Total current
total_current = toaster_current + frying_pan_current + lamp_current

# Check if the fuse will blow
fuse_blown = total_current > fuse_current

# Print results
print(f"Current drawn by the toaster: {toaster_current} A")
print(f"Current drawn by the frying pan: {frying_pan_current} A")
print(f"Current drawn by the lamp: {lamp_current} A")
print(f"Total current: {total_current} A")

if fuse_blown:
    print("The combination will blow the 15-A fuse.")
else:
    print("The combination will not blow the 15-A fuse.")


# Answer: Current drawn by the toaster: 15.0 A
#         Current drawn by the frying pan: 11.666666666666666 A
#         Current drawn by the lamp: 0.625 A
#         Total current: 27.291666666666664 A
#         The combination will blow the 15-A fuse.
