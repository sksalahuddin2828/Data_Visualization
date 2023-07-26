import numpy as np
import matplotlib.pyplot as plt

# Define the functions f(x) and g(x)
def f(x):
    return 2 + np.sqrt(x + 1) + np.cbrt(1 - x)

def g(x):
    return np.log((np.log(1 - x) / np.log(1 + x)) ** 2) / np.log(1 - x ** 2)

# Generate x values
x_values = np.linspace(-0.99, 0.99, 1000)

# Calculate y values for f(x) and g(x)
y_f = f(x_values)
y_g = g(x_values)

# Plot the functions
plt.plot(x_values, y_f, label='f(x) = 2 + sqrt(x+1) + cbrt(1 - x)')
plt.plot(x_values, y_g, label='g(x) = log((log(1 - x) / log(1 + x))^2) / log(1 - x^2)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Visualization of f(x) and g(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
