import numpy as np
import pandas as pd
import sympy as sp
import plotly.graph_objs as go
import plotly.express as px

# Define the universe U (e.g., integers from -5 to 5)
U = np.arange(-5, 6)

# Define the proposition p(x)
x = sp.Symbol('x')
p = x**2 - 4

# Evaluate the proposition for each value of x in the universe U
propositions = [p.subs(x, val) for val in U]

# Convert sympy expressions to regular Python numbers
propositions = [float(val) for val in propositions]

# Create a DataFrame to represent the propositions for each value of x
df = pd.DataFrame({'x': U, 'p(x)': propositions})

# Filter the values of x where the proposition p(x) is true
true_propositions = df[df['p(x)'] > 0]

# Create an interactive 3D scatter plot using Plotly Express
fig = px.scatter_3d(df, x='x', y='p(x)', z=np.zeros(len(df)), color='p(x)',
                    color_continuous_scale='viridis', opacity=0.7,
                    title='Interactive 3D Visualization of Propositions with Existential Quantifier',
                    labels={'x': 'x', 'p(x)': 'p(x)', 'color': 'Truth Value'})

# Create a scatter trace for true propositions
trace_true = go.Scatter3d(x=true_propositions['x'], y=true_propositions['p(x)'],
                          z=np.zeros(len(true_propositions)), mode='markers',
                          marker=dict(size=5, color='green'), name='True')

# Create a scatter trace for false propositions
trace_false = go.Scatter3d(x=df[df['p(x)'] <= 0]['x'], y=df[df['p(x)'] <= 0]['p(x)'],
                           z=np.zeros(len(df[df['p(x)'] <= 0])), mode='markers',
                           marker=dict(size=5, color='red'), name='False')

# Add the custom traces to the figure
fig.add_trace(trace_true)
fig.add_trace(trace_false)

# Set axis labels and camera position for a better view
fig.update_layout(scene=dict(xaxis_title='x', yaxis_title='p(x)', zaxis_title='Truth Value'),
                  scene_camera=dict(eye=dict(x=-1.5, y=-1.5, z=1)))

# Show the interactive 3D plot
fig.show()
