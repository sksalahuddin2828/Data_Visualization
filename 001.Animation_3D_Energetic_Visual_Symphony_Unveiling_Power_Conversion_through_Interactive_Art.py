import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Given values
watts_data = np.random.uniform(20, 100, 50)
kilowatts_data = np.random.uniform(1, 5, 50)

# Create a DataFrame
data = pd.DataFrame({'Watts': watts_data, 'Kilowatts': kilowatts_data})

fig = px.scatter_3d(data, x='Watts', y='Kilowatts', z='Watts', color='Kilowatts',
                    title='Watts vs Kilowatts Conversion')

fig.update_layout(scene=dict(
    xaxis_title='Watts',
    yaxis_title='Kilowatts',
    zaxis_title='Watts'
))

fig.show()

conversion_eq_str = 'Watts = Kilowatts * 1000'

fig.add_annotation(
    text=conversion_eq_str,
    xref="paper", yref="paper",
    x=0.5, y=0.95,
    showarrow=False,
    font=dict(size=12)
)

fig.show()

frames = []
for i in range(1, len(data) + 1):
    frame = go.Frame(
        data=[go.Scatter3d(x=data['Watts'][:i], y=data['Kilowatts'][:i], z=data['Watts'][:i],
                           mode='markers', marker=dict(size=8, opacity=0.5),
                           name='Conversion')],
        name=f'frame{i}'
    )
    frames.append(frame)

fig.frames = frames
animation_settings = go.layout.Updatemenu(type='buttons', showactive=False, buttons=[{
    'label': 'Play',
    'method': 'animate',
    'args': [None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}]
}])

fig.update_layout(updatemenus=[animation_settings])
fig.show()
