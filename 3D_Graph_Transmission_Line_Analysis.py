import numpy as np
import pandas as pd
import plotly.express as px

# Given values
Pave = 100e6  # 100 MW in watts
Vrms = 200e3  # 200 kV in volts
R = 1.0       # Resistance in ohms

# Calculate current, power dissipation, and percentage loss
Irms = Pave / Vrms
P_dissipated = Irms**2 * R
percentage_loss = (P_dissipated / Pave) * 100

# Create a DataFrame for visualization
data = {'Parameter': ['Current (A)', 'Power Dissipated (W)', 'Percentage Loss (%)'],
        'Value': [Irms, P_dissipated, percentage_loss]}
df = pd.DataFrame(data)

# Visualize using a bar plot
fig = px.bar(df, x='Parameter', y='Value', text='Value', title='Transmission Line Analysis')
fig.update_traces(texttemplate='%{text:.2e}', textposition='outside')

# Show the plot
fig.show()
