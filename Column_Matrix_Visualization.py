import pandas as pd
import plotly.express as px

data = {'Row': [1, 2, 3, 4, 5],
        'Value': [5, 11, 4, 3, 7]}

df = pd.DataFrame(data)

fig = px.scatter(df, x='Row', y='Value', title='Column Matrix Visualization')
fig.update_layout(xaxis_title='Row', yaxis_title='Value')
fig.show()
