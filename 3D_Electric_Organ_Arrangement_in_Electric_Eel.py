import pandas as pd
import numpy as np
import plotly.express as px

# Create a dataframe for electric organ information in Electric Eel
electric_organ_data = pd.DataFrame({
    'Row': np.arange(1, 141),  # Row numbers
    'Electroplaques': np.repeat(5000, 140)  # Electroplaques per row
})

# Create a 3D scatter plot using Plotly
fig = px.scatter_3d(electric_organ_data,
                     x='Row',
                     y='Electroplaques',
                     z=np.zeros(140),  # All points at z=0 for visualization
                     text='Electroplaques',
                     title='Electric Organ Arrangement in Electric Eel')

# Customize the appearance of the plot
fig.update_traces(marker=dict(size=5, color='blue', opacity=0.8))

# Add labels to axes
fig.update_layout(scene=dict(xaxis_title='Rows',
                             yaxis_title='Electroplaques per Row',
                             zaxis_title='Electroplaques'))

# Show the interactive plot
fig.show()
