# To resolve this, you can try updating the 'bokeh' library to the latest version. You can do this by running the following command in your Python environment.
# pip install --upgrade bokeh

import numpy as np
import pandas as pd
import sympy as sp
import plotly.express as px
import holoviews as hv
from holoviews import opts

# Define the universe U and create a pandas DataFrame for propositions
U = np.linspace(-5, 5, 100)
df = pd.DataFrame({'x': U})

# Define the proposition p(x) and evaluate it for each value of x
x = sp.Symbol('x')
p = x**2 - 4
df['p(x)'] = df['x'].apply(lambda val: p.subs(x, val))

# Convert sympy expressions to regular Python numbers
df['p(x)'] = df['p(x)'].apply(lambda val: float(val))

# Create interactive scatter plot using Plotly
fig_plotly = px.scatter(df, x='x', y='p(x)', color='p(x)', title="Interactive Scatter Plot")
fig_plotly.show()

# Enable the 'plotly' backend for Holoviews
hv.extension('plotly')

# Create interactive 3D plot using Holoviews with the 'plotly' backend
scatter_plot = hv.Points(df, kdims=['x', 'p(x)'], vdims='p(x)').opts(
    opts.Scatter3D(width=700, height=500, color='p(x)', cmap='viridis', title="Interactive 3D Plot")
)
scatter_plot

# Here's how to set the backend to 'bokeh':
# hv.extension('bokeh')

# And here's how to set the backend to 'matplotlib':
# hv.extension('matplotlib')
