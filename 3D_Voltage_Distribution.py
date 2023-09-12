import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff

# Define parameters
initial_voltage = 1000.0  # Initial voltage across the capacitor (V)
bleeder_resistor = 1000.0  # Bleeder resistor resistance (ohms)
capacitance = 0.001  # Capacitance (farads)
simulation_time = 5 * bleeder_resistor * capacitance  # Total simulation time

# Time values
time = np.linspace(0, simulation_time, 1000)

# Calculate voltage across the capacitor over time
voltage = initial_voltage * np.exp(-time / (bleeder_resistor * capacitance))

# Create a Pandas DataFrame for the data
data_df = pd.DataFrame({'Time (s)': time, 'Voltage (V)': voltage})

# Create an interactive line plot using Plotly
fig = px.line(data_df, x='Time (s)', y='Voltage (V)', title='Capacitor Discharge Curve')
fig.update_xaxes(title_text='Time (s)')
fig.update_yaxes(title_text='Voltage (V)')
fig.update_traces(line=dict(width=2))

# Create an interactive 3D surface plot using Plotly
# fig_3d = go.Figure(data=[go.Surface(z=[voltage], colorscale='Viridis')])
# fig_3d.update_layout(scene=dict(zaxis_title='Voltage (V)'), title='3D Visualization of Capacitor Discharge')

# Create a histogram using Plotly Figure Factory
hist_data = [voltage]
group_labels = ['Voltage Distribution']
hist_fig = ff.create_distplot(hist_data, group_labels)

# Display the interactive visualizations
fig.show()
# fig_3d.show()
hist_fig.show()

# import numpy as np
# import plotly.graph_objs as go

# Define parameters
initial_voltages = np.linspace(100, 1000, 10)  # Vary initial voltage from 100 to 1000 V
capacitances = np.linspace(0.001, 0.01, 10)  # Vary capacitance from 0.001 to 0.01 F
time_constant = 1000.0  # Fixed time constant (for demonstration)

# Create a grid of values for initial voltage and capacitance
initial_voltages, capacitances = np.meshgrid(initial_voltages, capacitances)

# Calculate voltage across the capacitor for different combinations
voltage = initial_voltages * np.exp(-time_constant / (capacitances * initial_voltages))

# Create a 3D surface plot
surface = go.Surface(x=initial_voltages, y=capacitances, z=voltage, colorscale='Viridis')
layout = go.Layout(scene=dict(xaxis_title='Initial Voltage (V)', yaxis_title='Capacitance (F)', zaxis_title='Voltage (V)'),
                   title='3D Visualization of Capacitor Discharge')
fig = go.Figure(data=[surface], layout=layout)

# Show the 3D visualization
fig.show()
