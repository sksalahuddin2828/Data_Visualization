# Solution of: d/dx csc(x) = −cot(x) csc(x)

import sympy as sp

x = sp.symbols('x')
equation = sp.diff(1/sp.sin(x), x) + sp.cot(x) * (1/sp.sin(x))

solution = sp.simplify(equation)
print("Solution:", solution)

import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x_vals = np.linspace(0.01, np.pi - 0.01, 300)  # Avoiding singularity at x = 0 and x = pi

# Calculate the equation and its solution
equation_vals = -np.cos(x_vals) / (np.sin(x_vals) ** 2)
solution_vals = -1 / np.sin(x_vals)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_vals, equation_vals, label=r'$-\frac{\cos(x)}{\sin^2(x)}$', linewidth=2)
plt.plot(x_vals, solution_vals, label=r'$-\frac{1}{\sin(x)}$', linestyle='dashed', linewidth=2)

# Highlight important points
plt.scatter(np.pi/2, 1, color='red', label='Singularity at π/2', s=80)
plt.scatter(np.pi/4, -2**0.5, color='green', label='Minimum at π/4', s=80)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Creative Visualization of Solution: d/dx csc(x) = −cot(x) csc(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Add annotations
plt.annotate("Singularity", xy=(np.pi/2, 1), xytext=(np.pi/2 + 0.2, 1.5),
             arrowprops=dict(facecolor='red', shrink=0.05))
plt.annotate("Minimum", xy=(np.pi/4, -2**0.5), xytext=(np.pi/4 + 0.2, -2),
             arrowprops=dict(facecolor='green', shrink=0.05))

# Add legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
