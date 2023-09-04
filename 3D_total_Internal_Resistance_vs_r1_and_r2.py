import pandas as pd
import plotly.express as px
import numpy as np

# Generate multiple values for E, r1, and r2
num_samples = 50  # Number of data points
E_values = np.random.uniform(10.0, 15.0, num_samples)  # Random emf values between 10 and 15 V
r1_values = np.random.uniform(0.05, 0.3, num_samples)  # Random r1 values between 0.05 and 0.3 Ohms
r2_values = np.random.uniform(0.05, 0.3, num_samples)  # Random r2 values between 0.05 and 0.3 Ohms

# Create a DataFrame
data = {
    'E': E_values,
    'r1': r1_values,
    'r2': r2_values
}

df = pd.DataFrame(data)
df['rtot'] = 1 / (1 / df['r1'] + 1 / df['r2'])
df['R_load'] = 2.0
df['I'] = df['E'] / (df['rtot'] + df['R_load'])

# Visualization with Plotly
fig = px.scatter_3d(df, x='r1', y='r2', z='rtot', color='rtot',
                     title='Total Internal Resistance vs. r1 and r2',
                     labels={'r1': 'r1 (Ohms)', 'r2': 'r2 (Ohms)', 'rtot': 'Total Internal Resistance (Ohms)'},
                     color_continuous_scale='viridis')
fig.update_coloraxes(colorbar_title='rtot (Ohms)')

fig.show()
