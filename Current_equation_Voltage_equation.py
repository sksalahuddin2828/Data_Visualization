import numpy as np
import pandas as pd
import sympy as sp

# Define the symbolic variables
emf = sp.Symbol('emf')
R_load = sp.Symbol('R_load')
r = sp.Symbol('r')
I = sp.Symbol('I')
V = sp.Symbol('V')

# Define the equations
current_equation = sp.Eq(I, emf / (R_load + r))
voltage_equation = sp.Eq(V, emf - I * r)

# Substitute the values
values = {'emf': 12.0, 'R_load': 10.1, 'r': 0.1}
current = sp.solve(current_equation.subs(values), I)[0]
terminal_voltage = voltage_equation.subs({**values, I: current}).rhs.evalf()

print("Current:", current)
print("Terminal Voltage:", terminal_voltage)

# Answer: Current: 1.17647058823529
#         Terminal Voltage: 11.8823529411765
