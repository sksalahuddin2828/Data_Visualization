import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd
from sympy import symbols, expand

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
