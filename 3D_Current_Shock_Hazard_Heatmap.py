import numpy as np
import pandas as pd
import plotly.express as px

# Create example data
current_data = np.linspace(0.001, 1, 100)
duration_data = np.linspace(0.1, 5, 100)
shock_hazard_data = current_data[:, np.newaxis] * duration_data

# Create a DataFrame
df = pd.DataFrame(shock_hazard_data, columns=duration_data, index=current_data)

# Create a heatmap
fig = px.imshow(df, x=duration_data, y=current_data,
                title='Shock Hazard Heatmap',
                labels={'x': 'Duration (s)', 'y': 'Current (A)', 'color': 'Shock Hazard'},
                color_continuous_scale='Viridis')

fig.show()
