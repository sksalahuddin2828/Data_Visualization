import numpy as np
import pandas as pd
import plotly.express as px

# Define the range of x values
x_vals = np.linspace(0.1, 5, 100)

# Define a range of 'm' values
m_values = np.linspace(-2, 2, 50)

# Create a DataFrame to store results
results_df = pd.DataFrame(columns=['x', 'm', 'integral'])

# Calculate integrals for each 'm'
for m in m_values:
    integral = x_vals ** m
    results_df = results_df.append(pd.DataFrame({'x': x_vals, 'm': m, 'integral': integral}))

# Create an interactive 3D surface plot
fig = px.scatter_3d(results_df, x='x', y='m', z='integral', title='Interactive Integral Visualization',
                    labels={'x': 'x values', 'm': 'm values', 'integral': 'Integral Result'})

# Show the interactive plot
fig.show()
