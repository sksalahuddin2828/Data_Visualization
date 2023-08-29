import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

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

# Interactive 3D scatter plot using Plotly
fig = px.scatter_3d(df, x='Current (A)', y='Resistance (Ω)', z='Voltage (μV)',
                    title='Voltage as a Function of Current and Resistance',
                    labels={'Current (A)': 'Current (A)', 'Resistance (Ω)': 'Resistance (Ω)', 'Voltage (μV)': 'Voltage (μV)'})

fig.show()

# Matplotlib wireframe plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(current_vals, resistance_vals)
Z = X * Y * 1e6
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
ax.set_xlabel('Current (A)')
ax.set_ylabel('Resistance (Ω)')
ax.set_zlabel('Voltage (μV)')
ax.set_title('Voltage as a Function of Current and Resistance')

plt.show()
