import numpy as np
import pandas as pd
import plotly.express as px

# Create a DataFrame with voltage, current, and power data
voltage_range = np.linspace(0, 240, 100)
current_range = np.linspace(0, 20, 100)
V, I = np.meshgrid(voltage_range, current_range)
P = V * I

data = pd.DataFrame({'Voltage': V.ravel(), 'Current': I.ravel(), 'Power': P.ravel()})

# Create an interactive scatter plot using Plotly
fig = px.scatter(data, x='Voltage', y='Current', size='Power', color='Power',
                 labels={'Voltage': 'Voltage (V)', 'Current': 'Current (A)', 'Power': 'Power (W)'},
                 title='Microwave Oven Power Consumption')

# Add a slider to control the marker size (power)
fig.update_layout(sliders=[{
    'currentvalue': {'prefix': 'Power: '},
    'steps': [{'args': [['marker.size'], [i]],
               'label': str(i),
               'method': 'restyle'} for i in range(10, 101, 10)]
}])

# Show the interactive plot
fig.show()
