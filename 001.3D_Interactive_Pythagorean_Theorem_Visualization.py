import numpy as np
import pandas as pd
import plotly.express as px

# Create an Interactive DataFrame
data = []
for a in np.linspace(1, 10, 10):
    for b in np.linspace(1, 10, 10):
        c = np.sqrt(a**2 + b**2)
        data.append({'a': a, 'b': b, 'c': c})
df = pd.DataFrame(data)

# Create Interactive 3D Scatter Plot using Plotly
fig = px.scatter_3d(df, x='a', y='b', z='c', color='c',
                    title='Interactive Pythagorean Theorem Visualization',
                    labels={'a': 'Side a', 'b': 'Side b', 'c': 'Hypotenuse c'},
                    size_max=10)

# Add a Surface Plane
a_range = np.linspace(0, 11, 20)
b_range = np.linspace(0, 11, 20)
a_grid, b_grid = np.meshgrid(a_range, b_range)
c_grid = np.sqrt(a_grid**2 + b_grid**2)
fig.add_surface(x=a_grid, y=b_grid, z=c_grid, colorscale='Blues')

# Show Interactive Plot
fig.show()
