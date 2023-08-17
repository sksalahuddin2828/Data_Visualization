import sympy as sp

# Define symbols and expressions
x, y = sp.symbols('x y')
expression = sp.sin(x) + sp.cos(y)

# Explain the expression using markdown and LaTeX
expression_text = """
Consider the expression:
\[ f(x, y) = \sin(x) + \cos(y) \]
"""

# Display the expression
display(expression_text)

import pandas as pd
import plotly.express as px

# Generate random data for demonstration
data = {'x': np.random.randint(1, 10, 50), 'y': np.random.randint(1, 10, 50)}
df = pd.DataFrame(data)

# Create a scatter plot using Plotly Express
scatter_plot = px.scatter(df, x='x', y='y', title='Scatter Plot')

# Display the scatter plot
scatter_plot.show()
