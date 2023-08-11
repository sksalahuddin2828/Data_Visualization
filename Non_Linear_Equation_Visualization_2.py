import numpy as np
import matplotlib.pyplot as plt

# Define the non-linear equation
def nonlinear_equation(x):
    return np.sqrt(25 - x**2), -np.sqrt(25 - x**2)

# Generate x values
x = np.linspace(-5, 5, 400)

# Calculate corresponding y values using the equation
y1, y2 = nonlinear_equation(x)

# Create the plot using Matplotlib
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='x^2 + y^2 = 25')
plt.plot(x, y2)
plt.title('Non-linear Equation Visualization')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

