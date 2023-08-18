import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbols and variables
x = sp.symbols('x')
a = 0
b = 2
f = x**2  # Define a function

# Calculate the definite integral
definite_integral = sp.integrate(f, (x, a, b))

# Create a numeric function for plotting
f_numeric = sp.lambdify(x, f, 'numpy')
x_vals = np.linspace(a, b, 100)
y_vals = f_numeric(x_vals)

# Create a filled area plot to visualize the integral
fig, ax = plt.subplots()
ax.fill_between(x_vals, y_vals, alpha=0.3, label=f'Integral = {definite_integral:.2f}')
ax.plot(x_vals, y_vals, label='f(x) = x^2')
ax.legend()
ax.set_title('Definite Integral and Area Under the Curve')
plt.show()
