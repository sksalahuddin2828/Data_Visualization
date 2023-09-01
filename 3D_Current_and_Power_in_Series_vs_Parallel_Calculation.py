import numpy as np
import pandas as pd

# Constants
voltage = 48.0  # V
resistances_series = np.array([24.0, 96.0])  # Ω
resistances_parallel = 1 / (1 / 24.0 + 1 / 96.0)  # Ω

# Calculate current in series
current_series = voltage / np.sum(resistances_series)

# Calculate current in parallel
current_parallel = voltage / resistances_parallel

# Calculate power in series
power_series = current_series**2 * resistances_series

# Calculate power in parallel
power_parallel = current_parallel**2 * resistances_parallel

# Create a pandas DataFrame for results
results_df = pd.DataFrame({
    'Configuration': ['Series', 'Parallel'],
    'Current (A)': [current_series, current_parallel],
    'Power (W)': [power_series, power_parallel]
})

print(results_df)

import numpy as np
import pandas as pd
import plotly.express as px

# Constants
voltage = 48.0  # V
resistances_series = np.array([24.0, 96.0])  # Ω
resistances_parallel = 1 / (1 / 24.0 + 1 / 96.0)  # Ω

# Calculate current in series
current_series = voltage / np.sum(resistances_series)

# Calculate current in parallel
current_parallel = voltage / resistances_parallel

# Calculate power in series
power_series = current_series**2 * resistances_series

# Calculate power in parallel
power_parallel = current_parallel**2 * resistances_parallel

# Create a pandas DataFrame for results
results_df = pd.DataFrame({
    'Configuration': ['Series', 'Parallel'],
    'Current (A)': [current_series, current_parallel],
    'Power (W)': [power_series, power_parallel]
})

# Melt the DataFrame into long format
results_melted = results_df.melt(id_vars='Configuration', var_name='Measurement', value_name='Value')

# Create an interactive bar chart
fig = px.bar(results_melted, x='Configuration', y='Value', color='Measurement',
             title='Current and Power in Series vs. Parallel',
             labels={'Value': 'Value'},
             height=400)

# Show the Plotly figure
fig.show()
