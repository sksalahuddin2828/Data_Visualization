import numpy as np
import matplotlib.pyplot as plt

# Define the linear equation
def linear_equation(x):
    return (8 - 3*x) / 2

# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate corresponding y values using the equation
y = linear_equation(x)

# Create the plot using Matplotlib
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='3x + 2y = 8')
plt.title('Linear Equation Visualization')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
