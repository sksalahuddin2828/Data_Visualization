import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from mpl_toolkits.mplot3d import Axes3D

# Step 2: Calculate Initial and Final Parameters
I = 800.0  # moment of inertia in kg-m^2
initial_angular_velocity = 4.0 * 2 * np.pi  # initial angular velocity in rad/s
final_kinetic_energy = 2.03e5  # final kinetic energy in J

# Calculate new angular velocity
final_angular_velocity = np.sqrt(final_kinetic_energy * 2 / I)

# Step 3: Create Data Visualization with Matplotlib (Simplified)
time_values = np.linspace(0, 5, num=100)
kinetic_energy_values = 0.5 * I * initial_angular_velocity**2 * np.exp(-time_values)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(time_values, [initial_angular_velocity] * len(time_values), kinetic_energy_values)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Velocity (rad/s)')
ax.set_zlabel('Kinetic Energy (J)')
ax.set_title('Change in Kinetic Energy and Angular Velocity')
ax.text(2, initial_angular_velocity, 200000, r'$KE = \frac{1}{2} I \omega^2 e^{-t}$', fontsize=12, color='red')
plt.show()

# Step 6: Creative Presentation with Plotly and Pandas
# Create a DataFrame to organize the data
data = {'Time (s)': time_values, 'Angular Velocity (rad/s)': initial_angular_velocity, 'Kinetic Energy (J)': kinetic_energy_values}
df = pd.DataFrame(data)

# Create animated visualizations using Plotly
fig1 = px.line(df, x='Time (s)', y='Angular Velocity (rad/s)', title='Change in Angular Velocity')
fig1.update_traces(line=dict(dash='dot'), selector=dict(type='scatter'))

fig2 = px.line(df, x='Time (s)', y='Kinetic Energy (J)', title='Change in Kinetic Energy')
fig2.update_traces(line=dict(dash='dot'), selector=dict(type='scatter'))

# Create a subplot with both animated Plotly visualizations
fig = make_subplots(rows=1, cols=2, subplot_titles=('Change in Angular Velocity', 'Change in Kinetic Energy'))
fig.add_trace(fig1.data[0], row=1, col=1)
fig.add_trace(fig2.data[0], row=1, col=2)

# Update subplot layout
fig.update_layout(showlegend=False)

# Add animation buttons
buttons = [dict(method='animate', label='Play', args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True, 'transition': {'duration': 0}}]),
           dict(method='animate', label='Pause', args=[[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'after', 'transition': {'duration': 0}}])]
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=buttons)])

# Create frames for animations
angular_velocity_frames = tuple([go.Frame(data=[go.Scatter(x=df['Time (s)'][:i+1], y=df['Angular Velocity (rad/s)'][:i+1], mode='lines')]) for i in range(len(df))])
kinetic_energy_frames = tuple([go.Frame(data=[go.Scatter(x=df['Time (s)'][:i+1], y=df['Kinetic Energy (J)'][:i+1], mode='lines')]) for i in range(len(df))])

# Attach frames to animated figures
fig.frames += angular_velocity_frames
fig.frames += kinetic_energy_frames

# Display the animated subplot visualization
fig.show()
