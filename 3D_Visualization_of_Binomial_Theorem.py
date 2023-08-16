import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy import symbols, expand
from mpl_toolkits.mplot3d import Axes3D

def binomial_theorem(a, b, n):
    coeffs = [expand((a + b)**n).coeff(a, k) for k in range(n+1)]
    terms = [f"{coeff}*{a}^{k}*{b}^{n-k}" for k, coeff in enumerate(coeffs)]
    expression = " + ".join(terms)
    return expression

a, b = symbols('a b')
n = 4
result = binomial_theorem(a, b, n)
print(f"(a + b)^{n} =", result)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a_vals = np.linspace(-2, 2, 100)
b_vals = np.linspace(-2, 2, 100)
a_vals, b_vals = np.meshgrid(a_vals, b_vals)
expression_values = (a_vals + b_vals)**n

ax.plot_surface(a_vals, b_vals, expression_values, cmap='viridis')
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('Expression Value')
ax.set_title('3D Visualization of Binomial Theorem')
plt.show()
