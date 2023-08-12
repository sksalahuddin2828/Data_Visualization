import numpy as np
import pandas as pd
import plotly.express as px

# Given symmetric matrix
symmetric_matrix = np.array([[1, 2, 3],
                             [2, 4, 5],
                             [3, 5, 6]])

# Convert the symmetric matrix to a DataFrame
df = pd.DataFrame(symmetric_matrix)

# Create a heatmap using plotly
fig = px.imshow(df, zmin=np.min(symmetric_matrix), zmax=np.max(symmetric_matrix), color_continuous_scale='Viridis')

# Update the layout for better display
fig.update_layout(
    title="Symmetric Matrix Heatmap",
    xaxis_title="Columns",
    yaxis_title="Rows",
    xaxis_nticks=len(df.columns),
    yaxis_nticks=len(df.index),
    xaxis_side="top",
    width=500,
    height=500,
    font=dict(size=10)
)

# Display the interactive heatmap
fig.show()
