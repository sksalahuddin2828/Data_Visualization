import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd
from sympy import symbols, expand
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

# Binomial theorem function remains the same

a, b = symbols('a b')
n = 4
result = binomial_theorem(a, b, n)
print(f"(a + b)^{n} =", result)

# Create a DataFrame for the expression values
a_vals = np.linspace(-2, 2, 100)
b_vals = np.linspace(-2, 2, 100)
a_vals, b_vals = np.meshgrid(a_vals, b_vals)
expression_values = (a_vals + b_vals)**n

df = pd.DataFrame({'a': a_vals.flatten(), 'b': b_vals.flatten(), 'expression': expression_values.flatten()})

# Interactive 3D Visualization using Plotly
fig = go.Figure(data=[go.Surface(z=expression_values, x=a_vals, y=b_vals)])
fig.update_layout(scene=dict(xaxis_title='a', yaxis_title='b', zaxis_title='Expression Value'),
                  title='Interactive 3D Visualization of Binomial Theorem')
fig.show()

# Additional creative visualization using Pandas
df['abs_expression'] = np.abs(df['expression'])
df['expression_color'] = np.log(df['abs_expression'] + 1)  # Adjust color intensity

plt.scatter(df['a'], df['b'], c=df['expression_color'], cmap='viridis', s=20)
plt.colorbar().set_label('Log-scaled Expression Value')
plt.xlabel('a')
plt.ylabel('b')
plt.title('Scatter Plot with Expression Value Color Map')
plt.show()

# Custom Function and Animation
def custom_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2)) / (x**2 + y**2)

fig, ax = plt.subplots()
x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
x_vals, y_vals = np.meshgrid(x_vals, y_vals)
z_vals = custom_function(x_vals, y_vals)

plot = ax.pcolormesh(x_vals, y_vals, z_vals, shading='auto')
plt.colorbar(plot, ax=ax, label='Function Value')

def animate(frame):
    z_vals_animated = custom_function(x_vals, y_vals + frame * 0.1)
    plot.set_array(z_vals_animated.flatten())
    return plot,

ani = FuncAnimation(fig, animate, frames=50, blit=True)
HTML(ani.to_jshtml())

# Explanation of Theory, Equations, and Formulas
theory_explanation = """
The binomial theorem describes the expansion of (a + b)^n.
For example, for n = 4:
(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4.
This expansion can be visualized using 3D plots and scatter plots.
"""

print(theory_explanation)
