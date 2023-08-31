import numpy as np
import pandas as pd
import plotly.graph_objects as go
from IPython.display import HTML, display

# Create a pandas DataFrame with sample data
data = {'X': np.random.uniform(-5, 5, 100),
        'Y': np.random.uniform(-5, 5, 100)}
df = pd.DataFrame(data)

# Define a function for the Z values
df['Z'] = df['X']**2 - df['Y']**2

# Calculate positive 'size' values for visualization
df['Size'] = df['Z'].apply(lambda x: max(0.1, abs(x)))

# Create an interactive 3D scatter plot using Plotly
scatter_plot = go.FigureWidget(data=[go.Scatter3d(x=df['X'], y=df['Y'], z=df['Z'],
                                                  mode='markers',
                                                  marker=dict(size=df['Size'], color=df['Z'], opacity=0.8))])
scatter_plot.update_layout(scene=dict(zaxis_title='Z', bgcolor='white'),
                           title='Interactive 3D Scatter Plot')
scatter_plot.show()
