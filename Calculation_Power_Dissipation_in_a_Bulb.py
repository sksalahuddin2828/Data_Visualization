import numpy as np
import sympy as sp

# Given values
voltage_source = 120  # V
wire_resistance = 0.400  # Ω
bulb_power_nominal = 75.0  # W
current_total = 15.0  # A

# Calculate the power dissipated by the bulb
current_bulb = sp.symbols('I_bulb')
bulb_resistance = voltage_source / current_bulb  # Ohm's Law
bulb_power = current_bulb**2 * bulb_resistance

# Solve for current through the bulb
eq = sp.Eq(current_total, current_bulb)
solutions = sp.solve(eq, current_bulb)

if solutions:
    power_dissipated = bulb_power.subs(current_bulb, solutions[0])
    print(f"Power dissipated by the bulb: {power_dissipated} W")
else:
    print("No valid solution found for current through the bulb.")

# Answer: 
    print(f"Power dissipated by the bulb: {power_dissipated} W")
else:
    print("No valid solution found for current through the bulb.")

# Answer: Power dissipated by the bulb: 1800.00000000000 W
