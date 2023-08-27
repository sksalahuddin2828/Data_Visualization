import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp

# Calculate peak current
rms_current = 15.0
peak_current = rms_current * np.sqrt(2)

# Create data
rms_values = np.linspace(0, 20, 100)
peak_values = rms_values * np.sqrt(2)
data = pd.DataFrame({'RMS Current (A)': rms_values, 'Peak Current (A)': peak_values})

# Create an interactive scatter plot using Plotly
fig = px.scatter(data, x='RMS Current (A)', y='Peak Current (A)', title='RMS vs. Peak Current',
                 labels={'RMS Current (A)': 'RMS Current (A)', 'Peak Current (A)': 'Peak Current (A)'})

# Add a trendline
fig.update_traces(mode='lines+markers')
trendline_eq = f'Peak Current = RMS Current × √2'
fig.add_annotation(text=trendline_eq, x=10, y=15)

# Display the interactive plot
fig.show()

# Create a summary table using Pandas
summary_table = data[data['RMS Current (A)'].isin([5, 10, 15, 20])]

print("Summary Table:")
print(summary_table)
