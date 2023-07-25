import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import sympy as sp

x = sp.symbols('x')
equation = sp.log(2*x, x) + sp.log(3*x, x) + sp.log(4*x, x) - 1000
solution = sp.solve(equation, x)

if len(solution) > 0:
    x_val = solution[0]
    print(f"The value of x is: {x_val}")
else:
    print("No solution found.")

x_vals = np.linspace(1, 1000, 1000)
log_values = np.log(2*x_vals)/np.log(x_vals) + np.log(3*x_vals)/np.log(x_vals) + np.log(4*x_vals)/np.log(x_vals)

plt.plot(x_vals, log_values)
plt.xlabel('x')
plt.ylabel('log equation value')
plt.title('Visualization of log equation')
plt.grid(True)
plt.show()
