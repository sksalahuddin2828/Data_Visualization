import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import display, Markdown
import sympy as sp
import plotly.express as px
import plotly.graph_objects as go
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
fig_3d = px.scatter_3d(df, x='Time', y='Voltage', z='Voltage', color='Voltage', title='Interactive 3D Voltage Visualization')
fig_3d.update_layout(scene=dict(xaxis_title='Time (s)', yaxis_title='Voltage (V)', zaxis_title='Voltage (V)'))
fig_3d.show()

# Step 5: Pandas Data Analysis and Visualization
np.random.seed(42)
noise = np.random.normal(0, 1, len(df))
df['Noisy_Voltage'] = df['Voltage'] + noise

fig_noise, axs_noise = plt.subplots(2, 1, figsize=(10, 8))
df.plot(x='Time', y=['Voltage', 'Noisy_Voltage'], ax=axs_noise[0], title='Voltage vs. Noisy Voltage')
df['Difference'] = df['Voltage'] - df['Noisy_Voltage']
df.plot(x='Time', y='Difference', ax=axs_noise[1], title='Difference between Voltage and Noisy Voltage')
plt.tight_layout()
plt.show()

# Step 6: Advanced Animation and Mathematical Expressions
fig_advanced_anim, ax_advanced_anim = plt.subplots(figsize=(8, 6))

def advanced_animate(i):
    ax_advanced_anim.clear()
    ax_advanced_anim.plot(df['Time'][:i], df['Voltage'][:i], color='b', label='Voltage')
    ax_advanced_anim.plot(df['Time'][:i], df['Noisy_Voltage'][:i], color='r', linestyle='dashed', label='Noisy Voltage')
    ax_advanced_anim.set_title('AC Voltage and Noisy Voltage Over Time')
    ax_advanced_anim.set_xlabel('Time (s)')
    ax_advanced_anim.set_ylabel('Voltage (V)')
    ax_advanced_anim.legend()
    ax_advanced_anim.grid(True)

ani_advanced = FuncAnimation(fig_advanced_anim, advanced_animate, frames=len(df['Time']), interval=50)
display(ani_advanced)

# Step 7: Interactive Animation with Plotly
fig_interactive_anim = go.Figure()

for i in range(len(df)):
    fig_interactive_anim.add_trace(go.Scatter(x=df['Time'][:i], y=df['Voltage'][:i], name='Voltage',
                                              mode='lines', line=dict(color='blue')))

    fig_interactive_anim.add_trace(go.Scatter(x=df['Time'][:i], y=df['Noisy_Voltage'][:i], name='Noisy Voltage',
                                              mode='lines', line=dict(color='red', dash='dash')))

    fig_interactive_anim.update_layout(title='Interactive AC Voltage and Noisy Voltage Animation',
                                       xaxis_title='Time (s)', yaxis_title='Voltage (V)',
                                       legend=dict(x=0, y=1))
    fig_interactive_anim.update_traces(showlegend=True)

frames = []

for i in range(len(df)):
    frame = go.Frame(data=[
        go.Scatter(x=df['Time'][:i+1], y=df['Voltage'][:i+1], mode='lines', name='Voltage'),
        go.Scatter(x=df['Time'][:i+1], y=df['Noisy_Voltage'][:i+1], mode='lines', name='Noisy Voltage')
    ])
    frame.name = f'frame_{i+1}'
    frames.append(frame)

fig_interactive_anim.frames = frames

fig_interactive_anim.show()
