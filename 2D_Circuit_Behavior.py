import pandas as pd

data = {'Resistor': ['R1', 'R2'],
        'Resistance (Ω)': [2750, 27.5],
        'Current (A)': [0, 0],
        'Voltage (V)': [0, 0]}

df = pd.DataFrame(data)

import plotly.express as px

fig = px.scatter(df, x='Resistance (Ω)', y='Current (A)', size='Voltage (V)', color='Voltage (V)',
                 text='Resistor', title='Circuit Behavior')
fig.update_traces(textposition='top center')
fig.update_layout(xaxis_title='Resistance (Ω)', yaxis_title='Current (A)')
fig.show()
