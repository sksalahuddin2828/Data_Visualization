import numpy as np
import sympy as sp
import pandas as pd

# Define symbols
I0, V0, R = sp.symbols('I0 V0 R')

# Equations
Irms_expr = I0 * sp.sqrt(2)
Vrms_expr = V0 * sp.sqrt(2)
Pave_expr = Irms_expr * Vrms_expr
Ohms_law_expr = Irms_expr - Vrms_expr / R

# Substituting values
values = {I0: 1, V0: 2, R: 3}
Irms_value = Irms_expr.subs(values)
Vrms_value = Vrms_expr.subs(values)
Pave_value = Pave_expr.subs(values)
Ohms_law_value = Ohms_law_expr.subs(values)

print("Irms:", Irms_value)
print("Vrms:", Vrms_value)
print("Pave:", Pave_value)
print("Ohm's Law:", Ohms_law_value)

data = {'Parameter': ['Irms', 'Vrms', 'Pave', "Ohm's Law"],
        'Value': [Irms_value, Vrms_value, Pave_value, Ohms_law_value]}
df = pd.DataFrame(data)
print(df)


# Answer: Irms: sqrt(2)
#         Vrms: 2*sqrt(2)
#         Pave: 4
#         Ohm's Law: sqrt(2)/3
#            Parameter      Value
#         0       Irms    sqrt(2)
#         1       Vrms  2*sqrt(2)
#         2       Pave          4
#         3  Ohm's Law  sqrt(2)/3
