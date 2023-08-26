import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# Create a meshgrid for X and Y values
x_vals = np.linspace(0, 10, 100)
y_vals = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = X * Y  # Replace with your function

# Matplotlib 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

# Plotly 3D surface plot
fig = go.Figure(data=[go.Surface(z=Z, x=x_vals, y=y_vals)])
fig.update_layout(scene=dict(xaxis_title='X Label', yaxis_title='Y Label', zaxis_title='Z Label'))
fig.show()
