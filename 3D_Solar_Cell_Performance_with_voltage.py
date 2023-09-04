import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Simulated solar cell data
incident_radiation = np.linspace(0, 1000, 20)
voltage_data = np.linspace(0.2, 2.0, 20)
current_data = np.linspace(0.1, 1.0, 20)

# Create a pandas DataFrame
df = pd.DataFrame({'Incident_Radiation': incident_radiation, 'Voltage': voltage_data, 'Current': current_data})

# Data analysis
mean_voltage = df['Voltage'].mean()
max_current = df['Current'].max()

# Create a 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=df['Incident_Radiation'],
    y=df['Voltage'],
    z=df['Current'],
    mode='markers',
    marker=dict(size=8, color=df['Incident_Radiation'], opacity=0.8),
    text='Radiation Level'
)])

fig.update_layout(scene=dict(xaxis_title='Incident Radiation',
                             yaxis_title='Voltage (V)',
                             zaxis_title='Current (A)'),
                  title='Solar Cell Performance',
                  margin=dict(l=0, r=0, b=0, t=40))

# Create a 2D scatter plot with hover text
fig2 = px.scatter(df, x='Incident_Radiation', y='Voltage', size='Current', hover_name='Incident_Radiation',
                  labels={'Incident_Radiation': 'Radiation Level'})
fig2.update_traces(marker=dict(size=8, opacity=0.8))

# Display analysis results
print(f"Mean Voltage Output: {mean_voltage}")
print(f"Max Current Output: {max_current}")

# Show the interactive 3D plot
fig.show()

# Show the 2D scatter plot
fig2.show()
