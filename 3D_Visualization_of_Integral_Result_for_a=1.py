import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.integrate import quad
from mpl_toolkits.mplot3d import Axes3D

# Define the symbols
x, a = sp.symbols('x a')

# Define the integral
integral = sp.integrate(a**2 - x**2, x)

# Calculate the integral
result = integral + 12 * a * sp.ln(sp.Abs(x + a * x - a))

# Display the result
print("Result of the integral:")
sp.pprint(result)

# Create interactive 3D plot
x_vals = np.linspace(-5, 5, 100)
a_vals = np.linspace(0.1, 2, 50)
X, A = np.meshgrid(x_vals, a_vals)
Z = X + A * X - A

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, A, Z, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('a')
ax.set_zlabel('Result')
ax.set_title('3D Visualization of Result')

plt.show()

# Create a dynamic line plot using plotly
x_vals = np.linspace(-5, 5, 100)
y_vals = [float(result.evalf(subs={x: val, a: 1})) for val in x_vals]  # Convert to float

df = pd.DataFrame({'x': x_vals, 'y': y_vals})
fig = px.line(df, x='x', y='y', title='Integral Result for a=1')
fig.update_xaxes(title_text='x')
fig.update_yaxes(title_text='Result')

fig.show()
