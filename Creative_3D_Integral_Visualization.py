import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px

# Define the symbolic variable
x, a = sp.symbols('x a')

# Define the integrand
integral_expr = sp.sqrt(a**2 + x**2)

# Solve the integral symbolically
integral_result = sp.integrate(integral_expr, x)

# Create a function from the symbolic expression
integral_func = sp.lambdify((x, a), integral_result, 'numpy')

# Generate x values for plotting
x_vals = np.linspace(-10, 10, 400)

# Generate a values for plotting
a_vals = np.linspace(0.1, 5, 100)

# Create a meshgrid for 3D plotting
X, A = np.meshgrid(x_vals, a_vals)

# Calculate the integral values using the function
integral_vals = integral_func(X, A)

# Create a DataFrame for the plotly line plot
integral_df = pd.DataFrame({'x': x_vals, 'Integral': integral_vals[0]})

# Create an interactive line plot using Plotly
fig = px.line(integral_df, x='x', y='Integral', title='Integral Plot')
fig.show()

# Create a 3D plot using Matplotlib
fig_3d = plt.figure()
ax = fig_3d.add_subplot(111, projection='3d')
ax.plot_surface(X, A, integral_vals)
ax.set_xlabel('x')
ax.set_ylabel('a')
ax.set_zlabel('Integral')
ax.set_title('3D Integral Visualization')
plt.show()
