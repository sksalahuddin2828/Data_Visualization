import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Generating data
R1_vals = np.linspace(0, 500, 50)
R2_vals = np.linspace(0, 500, 50)
R1_vals, R2_vals = np.meshgrid(R1_vals, R2_vals)
Rs_vals = R1_vals + R2_vals

# Create an interactive 3D surface plot
fig = go.Figure(data=[go.Surface(z=Rs_vals, x=R1_vals, y=R2_vals)])
fig.update_layout(scene=dict(xaxis_title='R1', yaxis_title='R2', zaxis_title='Rs'),
                  title='Interactive Series Resistance Comparison')
fig.show()

data = {'R1': R1_vals.flatten(), 'R2': R2_vals.flatten(), 'Rs': Rs_vals.flatten()}
df = pd.DataFrame(data)
print(df.head())
