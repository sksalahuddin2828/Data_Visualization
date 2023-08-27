import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import sympy as sp

# Given peak voltage
peak_voltage = 679

# Calculate the RMS voltage using numpy
rms_voltage = peak_voltage / np.sqrt(2)

# Display the RMS voltage
print(f"RMS Voltage: {rms_voltage:.2f} V")

# Create symbolic variable for visualization
t = sp.symbols('t')

# Create a sinusoidal equation for visualization
equation = peak_voltage * sp.sin(t)

# Convert sympy expression to numpy function
equation_numpy = sp.lambdify(t, equation, "numpy")

# Generate data points for visualization
t_vals = np.linspace(0, 2 * np.pi, 100)
voltage_vals = equation_numpy(t_vals)

# Create a 3D visualization using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(t_vals, voltage_vals, t_vals, label='Voltage = 679 * sin(t)')
ax.set_xlabel('Time')
ax.set_ylabel('Voltage')
ax.set_zlabel('Time')
ax.legend()

# Show the 3D plot
plt.show()

# Create interactive visualization using Plotly
fig = go.Figure(data=[go.Scatter3d(x=t_vals, y=voltage_vals, z=t_vals, mode='lines')])
fig.update_layout(scene=dict(
                    xaxis_title='Time',
                    yaxis_title='Voltage',
                    zaxis_title='Time'),
                  title='Mathematical Dance of Voltage')
fig.show()
