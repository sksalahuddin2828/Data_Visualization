import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
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

# Creative Presentation with Plotly and Pandas
# Create a DataFrame to organize the data
data = {'Time (s)': time_values, 'Angular Velocity (rad/s)': initial_angular_velocity, 'Kinetic Energy (J)': kinetic_energy_values}
df = pd.DataFrame(data)

# Create interactive visualizations using Plotly
fig1 = px.line(df, x='Time (s)', y='Angular Velocity (rad/s)', title='Change in Angular Velocity')
fig2 = px.line(df, x='Time (s)', y='Kinetic Energy (J)', title='Change in Kinetic Energy')

# Create a subplot with both Plotly visualizations
fig = make_subplots(rows=1, cols=2, subplot_titles=('Change in Angular Velocity', 'Change in Kinetic Energy'))
fig.add_trace(fig1.data[0], row=1, col=1)
fig.add_trace(fig2.data[0], row=1, col=2)

# Update subplot layout
fig.update_layout(showlegend=False)

# Display the Plotly subplot visualization
fig.show()
