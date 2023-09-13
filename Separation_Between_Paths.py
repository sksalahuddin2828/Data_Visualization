import numpy as np
import sympy as sp

# Constants
mass_U235 = 3.90e-25  # Mass of uranium-235 ion (kg)
mass_U238 = 3.95e-25  # Mass of uranium-238 ion (kg)
velocity = 3.00e5      # Velocity of ions (m/s)
magnetic_field = 0.250  # Magnetic field strength (T)
charge_U235 = 3        # Charge of uranium-235 ion
charge_U238 = 3        # Charge of uranium-238 ion

# Calculate radius of semicircle path for each ion
radius_U235 = (mass_U235 * velocity) / (charge_U235 * magnetic_field)
radius_U238 = (mass_U238 * velocity) / (charge_U238 * magnetic_field)

# Calculate the separation between their paths when they hit a target
separation = radius_U238 - radius_U235

print(f"Separation between paths: {separation:.4f} meters")

# Answer: Separation between paths: 0.0000 meters
