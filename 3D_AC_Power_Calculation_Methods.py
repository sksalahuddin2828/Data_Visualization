import numpy as np
import pandas as pd
import plotly.express as px

# Create a DataFrame for power calculation methods
methods = ['Irms * Vrms', 'Vrms^2 / R', 'Irms^2 * R']
powers = [Pave_formula1, Pave_formula2, Pave_formula3]
data = {'Method': methods, 'Average Power': powers}
df = pd.DataFrame(data)

# Create an interactive bar chart
fig = px.bar(df, x='Method', y='Average Power', text='Average Power', title='AC Power Calculation Methods')
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.show()
