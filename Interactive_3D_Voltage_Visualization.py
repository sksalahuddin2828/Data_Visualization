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

fig, ax = plt.subplots(figsize=(8, 6))

def animate(i):
    ax.clear()
    ax.plot(df['Time'][:i], df['Voltage'][:i], color='b')
    ax.set_title('AC Voltage Over Time')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Voltage (V)')
    ax.grid(True)

ani = FuncAnimation(fig, animate, frames=len(df['Time']), interval=50)
display(ani)

# Step 3: Mathematical Dance and Equation Presentation
equation = r"$V = V_0 \sin(2\pi ft)$"
display(Markdown(equation))

# Step 4: Interactive 3D Visualization
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['Time'], df['Voltage'], df['Voltage'], c=df['Voltage'], cmap='viridis')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Voltage (V)')
ax.set_title('Interactive 3D Voltage Visualization')
plt.show()
