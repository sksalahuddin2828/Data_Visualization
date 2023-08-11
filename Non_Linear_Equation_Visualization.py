import numpy as np
import matplotlib.pyplot as plt

# Define the non-linear equation
def nonlinear_equation(x):
    return 4 * x**2 + 5 * x + 3

# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate corresponding y values using the equation
y = nonlinear_equation(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 4x^2 + 5x + 3')
plt.title('Non-linear Equation Visualization')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
