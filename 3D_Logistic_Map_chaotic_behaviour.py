import pandas as pd
import plotly.express as px
import numpy as np

# Define the logistic map function
def logistic_map(x, r):
    return r * x * (1 - x)

# Generate logistic map data for different growth rates (r values)
growth_rates = [2.5, 3.5, 4.0]
logistic_data = pd.DataFrame()
logistic_data['Time (iterations)'] = range(100)
for r in growth_rates:
    logistic_data[f'r={r}'] = logistic_map(logistic_data.iloc[:, -1], r)

# Melt the DataFrame for plotting with Plotly
melted_logistic_data = pd.melt(logistic_data, id_vars=['Time (iterations)'],
                               var_name='Growth Rate (r)', value_name='Population')

# Plot the logistic map data
fig = px.line(melted_logistic_data, x='Time (iterations)', y='Population', color='Growth Rate (r)',
              title='Logistic Map - Chaotic Behavior',
              labels={'Population': 'Population (x)', 'Time (iterations)': 'Time'},
              template='plotly_dark')
fig.show()
