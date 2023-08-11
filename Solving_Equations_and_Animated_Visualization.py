import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import sympy as sp

# Example 2: Solve 3x^2 - 5x + 2 = 0
x = sp.symbols('x')
equation = 3*x**2 - 5*x + 2
solutions = sp.solve(equation, x)
print("Example 2 Solutions:", solutions)

# Example 3: Solve 3x + 9 = 2x + 18
equation = 3*x + 9 - (2*x + 18)
solution = sp.solve(equation, x)
print("Example 3 Solution:", solution[0])

# Example 4: Solve x + 2y = 1 and x = y
y = sp.symbols('y')
equation1 = x + 2*y - 1
equation2 = x - y
solutions = sp.solve([equation1, equation2], (x, y))
print("Example 4 Solutions:", solutions)

# Example 5: Solve x = 12(x + 2)
equation = x - 12*(x + 2)
solution = sp.solve(equation, x)
print("Example 5 Solution:", solution[0])

# Example 6: Solve 7x + 21 = 6x + 26
equation = 7*x + 21 - (6*x + 26)
solution = sp.solve(equation, x)
print("Example 6 Solution:", solution[0])

# Create a DataFrame for animation
animation_data = pd.DataFrame({'x': np.linspace(-10, 10, 400)})

# Example 2 Animation
animation_data['y'] = 3*animation_data['x']**2 - 5*animation_data['x'] + 2
fig2 = px.scatter(animation_data, x='x', y='y', title="Example 2 Animation")
fig2.update_traces(marker=dict(size=8, color='red'))

# Example 3 Animation
animation_data['y'] = 3*animation_data['x'] + 9 - (2*animation_data['x'] + 18)
fig3 = px.scatter(animation_data, x='x', y='y', title="Example 3 Animation")
fig3.update_traces(marker=dict(size=8, color='green'))

# Example 4 Animation
animation_data['y'] = animation_data['x'] + 2*animation_data['x'] - 1
fig4 = px.scatter(animation_data, x='x', y='y', title="Example 4 Animation")
fig4.update_traces(marker=dict(size=8, color='blue'))

# Example 5 Animation
animation_data['y'] = animation_data['x'] - 12*(animation_data['x'] + 2)
fig5 = px.scatter(animation_data, x='x', y='y', title="Example 5 Animation")
fig5.update_traces(marker=dict(size=8, color='purple'))

# Example 6 Animation
animation_data['y'] = 7*animation_data['x'] + 21 - (6*animation_data['x'] + 26)
fig6 = px.scatter(animation_data, x='x', y='y', title="Example 6 Animation")
fig6.update_traces(marker=dict(size=8, color='orange'))

# Create subplots
fig = make_subplots(rows=2, cols=3, subplot_titles=("Example 2", "Example 3", "Example 4", "Example 5", "Example 6"))
fig.add_trace(fig2.data[0], row=1, col=1)
fig.add_trace(fig3.data[0], row=1, col=2)
fig.add_trace(fig4.data[0], row=1, col=3)
fig.add_trace(fig5.data[0], row=2, col=1)
fig.add_trace(fig6.data[0], row=2, col=2)

# Update layout for subplots
fig.update_layout(title_text="Solving Equations and Animated Visualization", showlegend=False)

# Show the plot
fig.show()
