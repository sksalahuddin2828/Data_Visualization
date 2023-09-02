import numpy as np
import pandas as pd
import plotly.express as px

# Create a DataFrame with V1 and R2 values
V1_values = np.linspace(0, 5, 100)
R2_values = np.linspace(1, 10, 100)
V1_values, R2_values = np.meshgrid(V1_values, R2_values)
I2_values = (V - V1_values) / R2_values

df = pd.DataFrame({
    'V1': V1_values.flatten(),
    'R2': R2_values.flatten(),
    'I2': I2_values.flatten()
})

# Create an interactive 3D surface plot
fig = px.scatter_3d(df, x='V1', y='R2', z='I2',
                     labels={'I2': 'Current (A)'},
                     title='Current through R2 vs. V1 and R2')

fig.update_traces(marker=dict(size=5),
                  selector=dict(mode='markers+text'),
                  textfont_size=12,
                  textposition='top right')

fig.show()
