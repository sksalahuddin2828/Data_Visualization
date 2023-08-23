import plotly.express as px
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3D Angular Acceleration Plot
time_values = np.linspace(0, t, 100)
alpha_values = 20.0 * (2 * np.pi) - 0.1 * time_values

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(time_values, alpha_values, zs=0, zdir='y', label='Angular Acceleration')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Acceleration (rad/s^2)')
ax.set_zlabel('Value')
ax.legend()
plt.show()
