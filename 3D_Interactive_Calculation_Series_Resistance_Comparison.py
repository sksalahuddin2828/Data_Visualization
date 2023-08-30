import numpy as np
import pandas as pd
import plotly.express as px

# Generating data
R1_vals = np.linspace(0, 500, 50)
R2_vals = np.linspace(0, 500, 50)
R1_vals, R2_vals = np.meshgrid(R1_vals, R2_vals)
Rs_vals = R1_vals + R2_vals

# Create a DataFrame for the plot
data = pd.DataFrame({'R1': R1_vals.flatten(), 'R2': R2_vals.flatten(), 'Rs': Rs_vals.flatten()})

# Create an interactive scatter plot
fig = px.scatter(data, x='R1', y='R2', color='Rs',
                 labels={'R1': 'R1', 'R2': 'R2', 'Rs': 'Rs'},
                 title='Interactive Series Resistance Comparison',
                 hover_data={'R1': True, 'R2': True, 'Rs': True},
                 color_continuous_scale='viridis')

# Show the plot
fig.show()
