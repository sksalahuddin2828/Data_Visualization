import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.integrate import odeint

# Constants
B = 0.100  # Magnetic field strength in Tesla
E = 1500  # Electric field strength in N/C
d = 0.01  # Separation between plates in meters
v0 = 4.00e6  # Initial speed in m/s
q = 1.6e-19  # Charge of the particle in Coulombs
m = 9.11e-31  # Mass of the particle in kg

# Time values
t = np.linspace(0, 0.002, 1000)  # Adjust time as needed

# Equations of motion for a charged particle
def motion_equations(w, t, q, m, E, B):
    x, y, z, vx, vy, vz = w
    Fx = q * (E + vy * B)
    Fy = q * (vx * B)
    Fz = q * (-vx * E)
    dxdt = vx
    dydt = vy
    dzdt = vz
    dvxdt = Fx / m
    dvydt = Fy / m
    dvzdt = Fz / m
    return [dxdt, dydt, dzdt, dvxdt, dvydt, dvzdt]

# Solve the equations of motion
initial_conditions = [0, 0, 0, 0, 0, v0]
solution = odeint(motion_equations, initial_conditions, t, args=(q, m, E, B))

# Extract position data
x, y, z = solution[:, 0], solution[:, 1], solution[:, 2]

# Create interactive 3D visualization
fig = go.Figure()

fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(width=3)))

fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    title='Charged Particle Motion in Magnetic and Electric Fields',
)

# Show the interactive visualization
fig.show()

# Static 3D visualization (optional)
plt.figure()
ax = plt.axes(projection='3d')
ax.plot(x, y, z, linewidth=3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Charged Particle Motion in Magnetic and Electric Fields (Static)')
plt.show()
