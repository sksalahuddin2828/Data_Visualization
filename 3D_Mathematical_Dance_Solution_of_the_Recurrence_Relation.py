import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

def recurrence_relation(x, h):
    return (4 * f(x + h) - 2 * f(x)) / 2

def f(x):
    return 1 + np.sin(x) * np.exp(-x / 5)

x_values = np.linspace(-10, 10, 100)  # Define the range of x values
h = 0.1  # Define the value of h

f_values = [f(x) for x in x_values]
for i in range(2, len(x_values)):
    f_next = recurrence_relation(x_values[i], h)
    f_values.append(f_next)

plt.figure(figsize=(12, 8))

# Plot the solution with mathematical functions
plt.plot(x_values, f_values[:len(x_values)], color='purple', linewidth=2.5, label='Solution of Recurrence Relation')
plt.plot(x_values, np.sin(x_values), 'r--', label='sin(x)')
plt.plot(x_values, np.exp(-x_values / 5), 'g-.', label='e^(-x/5)')

# Add artistic elements (dance movements)
plt.plot(x_values, f_values[:len(x_values)], 'bo', markersize=8, label='Dance Movements')
plt.scatter(x_values, f_values[:len(x_values)], c=f_values[:len(x_values)], cmap='viridis', s=100, edgecolors='k')

# Add a background gradient for visual appeal
plt.gca().set_facecolor('#f0f0f0')
plt.colorbar(label='Value of f(x)', cmap='viridis')

# Add title and labels
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Mathematical Dance: Solution of the Recurrence Relation')
plt.legend()
plt.grid(True)

plt.show()
