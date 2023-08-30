import numpy as np
import pandas as pd
import plotly.express as px

# Create example data
current_data = np.linspace(0, 1500, 100)
power_data = current_data ** 2 / 1000

# Create a DataFrame
df = pd.DataFrame({'Current (A)': current_data, 'Power (kW)': power_data})

# Create an interactive scatter plot
fig = px.scatter(df, x='Current (A)', y='Power (kW)', title='Current vs Power',
                 labels={'Current (A)': 'Current (A)', 'Power (kW)': 'Power (kW)'},
                 hover_data=['Current (A)', 'Power (kW)'])

fig.show()
