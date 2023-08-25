import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import display, Markdown
import sympy as sp
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D

# Step 2: Define the AC Voltage Function and Dynamic Visualization
def ac_voltage(V0, f, t):
    return V0 * np.sin(2 * np.pi * f * t)

t_values = np.linspace(0, 1, 1000)
V0 = 10
f = 50
voltage_values = ac_voltage(V0, f, t_values)
data = {'Time': t_values, 'Voltage': voltage_values}
df = pd.DataFrame(data)

# Step 3: Mathematical Dance and Equation Presentation
equation = r"$V = V_0 \sin(2\pi ft)$"
display(Markdown(equation))

# Step 4: Interactive 3D Visualization with Plotly
fig = px.scatter_3d(df, x='Time', y='Voltage', z='Voltage', color='Voltage', title='Interactive 3D Voltage Visualization')
fig.update_layout(scene=dict(xaxis_title='Time (s)', yaxis_title='Voltage (V)', zaxis_title='Voltage (V)'))
fig.show()

# Step 5: Pandas Data Analysis and Visualization
# Let's add some noise to the voltage data for variety
np.random.seed(42)
noise = np.random.normal(0, 1, len(df))
df['Noisy_Voltage'] = df['Voltage'] + noise

# Analyze and visualize noisy data
fig, axs = plt.subplots(2, 1, figsize=(10, 8))
df.plot(x='Time', y=['Voltage', 'Noisy_Voltage'], ax=axs[0], title='Voltage vs. Noisy Voltage')
df['Difference'] = df['Voltage'] - df['Noisy_Voltage']
df.plot(x='Time', y='Difference', ax=axs[1], title='Difference between Voltage and Noisy Voltage')
plt.tight_layout()
plt.show()
