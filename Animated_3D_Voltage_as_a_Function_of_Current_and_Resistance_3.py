import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import IPython.display as display
import time

# Given values
current = 20.0e-6  # Amps
resistance = 300   # Ohms

# Calculate voltage using Ohm's law: V = I * R
voltage = current * resistance * 1e6  # Convert to μV

print("The smallest voltage that poses danger:", voltage, "μV")

# Create a dataframe for visualization
current_vals = np.linspace(0, 30e-6, 100)
resistance_vals = np.linspace(0, 500, 100)
data = []

for curr in current_vals:
    for res in resistance_vals:
        data.append({'Current (A)': curr, 'Resistance (Ω)': res, 'Voltage (μV)': curr * res * 1e6})

df = pd.DataFrame(data)

# Create interactive 3D scatter plot using Plotly
scatter_plot = px.scatter_3d(df, x='Current (A)', y='Resistance (Ω)', z='Voltage (μV)',
                              title='Voltage as a Function of Current and Resistance',
                              labels={'Current (A)': 'Current (A)', 'Resistance (Ω)': 'Resistance (Ω)', 'Voltage (μV)': 'Voltage (μV)'})

#------------------------------------------------------------------------------------------------------------------------------------------------

# Matplotlib wireframe plot
# fig_wireframe = plt.figure()
# ax = fig_wireframe.add_subplot(111, projection='3d')
# X, Y = np.meshgrid(current_vals, resistance_vals)
# Z = X * Y * 1e6
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
# ax.set_xlabel('Current (A)')
# ax.set_ylabel('Resistance (Ω)')
# ax.set_zlabel('Voltage (μV)')
# ax.set_title('Voltage as a Function of Current and Resistance')

#------------------------------------------------------------------------------------------------------------------------------------------------

# Create animated plot with changing resistance values
animation_frames = []
for res in resistance_vals:
    animation_frames.append(go.Scatter(x=current_vals, y=res * current_vals * 1e6, mode='lines', name=f'Resistance = {res} Ω'))

animation_plot = go.Figure(animation_frames, layout=go.Layout(xaxis_title='Current (A)',
                                                              yaxis_title='Voltage (μV)'))

animation_plot.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                                                                                 method='animate',
                                                                                                 args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True, transition=dict(duration=0))]),
                                                                                          dict(label='Pause',
                                                                                               method='animate',
                                                                                               args=[[None], dict(frame=dict(duration=0, redraw=False), mode='immediate')])])],
                            sliders=[dict(currentvalue={'prefix': 'Resistance: '},
                                          steps=[dict(label=f'Resistance = {res} Ω',
                                                      method='animate',
                                                      args=[[f'Resistance = {res} Ω'], dict(mode='immediate')]) for res in resistance_vals])])

# Arrange plots side by side using subplots
fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'scene'}, {'type': 'scene'}, {'type': 'xy'}]])
fig.add_trace(scatter_plot.data[0], row=1, col=1)
fig.add_trace(scatter_plot.data[0], row=1, col=2)
fig.add_trace(animation_frames[0], row=1, col=3)

# Update layout
fig.update_layout(scene=dict(aspectmode="manual", aspectratio=dict(x=1, y=1, z=0.5)),
                  scene2=dict(aspectmode="manual", aspectratio=dict(x=1, y=1, z=0.5)),
                  showlegend=False)

# Display the plots and animation

# display.display(fig_wireframe)

display.display(animation_plot)
display.display(fig)
time.sleep(5)
display.clear_output(wait=True)
