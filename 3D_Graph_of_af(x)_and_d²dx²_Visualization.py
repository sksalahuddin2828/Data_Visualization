import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define Symbol and Function
x = sp.symbols('x')
f_x = sp.sin(x)  # Example function

# Define the Function af(x) = a * f(x)
a = sp.symbols('a')
af_x = a * f_x

# Calculate the Second Derivative of af(x)
second_derivative = sp.diff(af_x, x, 2)

# Numeric Functions for Visualization
f_numeric = sp.lambdify(x, af_x.subs(a, 10), 'numpy')
second_derivative_numeric = sp.lambdify(x, second_derivative.subs(a, 10), 'numpy')

# Create Visualization
x_vals = np.linspace(-10, 10, 400)
y_vals_af = f_numeric(x_vals)
y_vals_second_derivative = second_derivative_numeric(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals_af, label='$af(x)$', color='blue')
plt.plot(x_vals, y_vals_second_derivative, label='$\\frac{d^2}{dx^2}(af(x))$', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Visualization of $af(x)$ and $\\frac{d^2}{dx^2}(af(x))$')
plt.legend()
plt.grid()
plt.show()
