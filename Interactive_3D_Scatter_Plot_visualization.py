import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp

# Create a pandas DataFrame with sample data
data = {'X': np.random.uniform(-5, 5, 100),
        'Y': np.random.uniform(-5, 5, 100)}
df = pd.DataFrame(data)

# Define a function for the Z values
df['Z'] = df['X']**2 - df['Y']**2

# Calculate positive 'size' values for visualization
df['Size'] = df['Z'].apply(lambda x: max(0.1, abs(x)))

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(df, x='X', y='Y', z='Z',
                    color='Z', size='Size', opacity=0.8,
                    title='Interactive 3D Scatter Plot')
fig.update_layout(scene=dict(zaxis_title='Z'))
fig.show()
