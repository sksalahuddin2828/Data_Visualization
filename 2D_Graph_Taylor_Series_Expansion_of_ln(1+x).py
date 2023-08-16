import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define the symbolic variable
x = sp.Symbol('x')

# Define the equation
equation = sp.ln(1 + x)

# Calculate the Taylor series expansion of the equation
taylor_series = sp.series(equation, x, n=10).removeO()

# Convert the symbolic expression to a numeric function
taylor_func = sp.lambdify(x, taylor_series, 'numpy')

# Generate x values
x_vals = np.linspace(-1, 1, 500)

# Calculate y values using the Taylor function
y_vals = taylor_func(x_vals)

# Create a colorful plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_vals, y_vals, label='Taylor Series Expansion')
ax.plot(x_vals, np.log(1 + x_vals), label='ln(1+x)', linestyle='dashed')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Taylor Series Expansion of ln(1+x)')
ax.legend()
ax.grid(True)
plt.show()
