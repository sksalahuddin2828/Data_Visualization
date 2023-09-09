import pandas as pd
import numpy as np
import plotly.express as px

# Generate synthetic data
np.random.seed(42)  # For reproducibility

num_samples = 100
data = {
    'emfx': np.random.uniform(0.5, 1.0, num_samples),
    'emfs': np.random.uniform(1.0, 1.5, num_samples),
    'Rx': np.random.uniform(2.0, 3.0, num_samples),
    'Rs': np.random.uniform(1.0, 2.0, num_samples)
}

df = pd.DataFrame(data)

# Calculate emfx using the formula
df['calculated_emfx'] = df['emfs'] * (df['Rx'] / df['Rs'])

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(
    df,
    x='emfx',
    y='emfs',
    z='Rx',
    color='Rs',
    size='calculated_emfx',
    hover_data=['calculated_emfx']
)

# Customize the plot
fig.update_layout(
    scene=dict(
        xaxis_title='emfx',
        yaxis_title='emfs',
        zaxis_title='Rx',
    ),
    title='Interactive 3D Scatter Plot of emfx, emfs, Rx, and Rs',
)

# Show the plot
fig.show()
