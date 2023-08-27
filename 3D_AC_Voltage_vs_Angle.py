import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt

# Calculate the time for one complete cycle of 400-Hz AC power
frequency = 400  # in Hertz
time_period = 1 / frequency  # in seconds

# Display the result
print("Time for one complete cycle:", time_period, "seconds")

# Create a symbolic variable for the angle in radians
angle = sp.symbols('angle', real=True)

# Create a function for the AC voltage over time
voltage_function = sp.sin(angle)

# Create a numpy function from the symbolic function
voltage_np = sp.lambdify(angle, voltage_function, 'numpy')

# Generate time values
angles = np.linspace(0, 2*np.pi, 100)
voltages = voltage_np(angles)

# Create a DataFrame using pandas
data = pd.DataFrame({'Angle': angles, 'Voltage': voltages})

# Interactive 3D plot using Plotly
fig = px.line_3d(data, x='Angle', y='Voltage', z=np.zeros_like(data['Angle']))
fig.update_layout(scene=dict(xaxis_title='Angle (radians)', yaxis_title='Voltage', zaxis_title='Time'))
fig.show()

# Scatter plot using Plotly
fig_scatter = px.scatter(data, x='Angle', y='Voltage', title='AC Voltage vs. Angle')
fig_scatter.update_xaxes(title_text='Angle (radians)')
fig_scatter.update_yaxes(title_text='Voltage')
fig_scatter.show()

# Polar plot using Plotly
fig_polar = go.Figure(go.Scatterpolar(r=data['Voltage'], theta=data['Angle'], mode='markers'))
fig_polar.update_layout(title='Polar Plot of AC Voltage')
fig_polar.show()

# Time-domain plot using Matplotlib
plt.plot(data['Angle'], data['Voltage'])
plt.xlabel('Angle (radians)')
plt.ylabel('Voltage')
plt.title('AC Voltage vs. Angle')
plt.grid(True)
plt.show()
