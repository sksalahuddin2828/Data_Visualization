import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd
from sympy import symbols
from math import factorial
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

def binomial_theorem(a, n):
    pos_coeffs = [factorial(n) / (factorial(k) * factorial(n - k)) for k in range(n + 1)]
    neg_coeffs = [(-1)**k * factorial(n) / (factorial(k) * factorial(n - k)) for k in range(n + 1)]
    pos_expression = " + ".join([f"{coeff}*x^{k}" for k, coeff in enumerate(pos_coeffs)])
    neg_expression = " + ".join([f"{coeff}*x^{k}" for k, coeff in enumerate(neg_coeffs)])
    return pos_expression, neg_expression

x = symbols('x')
n = 5
pos_result, neg_result = binomial_theorem(x, n)
print(f"(1 + x)^{n} =", pos_result)
print(f"(1 - x)^{n} =", neg_result)

# Create x values
x_vals = np.linspace(-0.9, 0.9, 100)

# Positive binomial expansion
pos_expansion = np.array([eval(pos_result.replace('^', '**').replace('x', str(x_val))) for x_val in x_vals])

# Negative binomial expansion
neg_expansion = np.array([eval(neg_result.replace('^', '**').replace('x', str(x_val))) for x_val in x_vals])

# Create beautiful plot using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(x_vals, pos_expansion, label=f"(1 + x)^{n}")
plt.plot(x_vals, neg_expansion, label=f"(1 - x)^{n}")
plt.xlabel('x')
plt.ylabel('Expansion Value')
plt.title(f"Binomial Expansion (n = {n})")
plt.legend()
plt.grid()
plt.show()
