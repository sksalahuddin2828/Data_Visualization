import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Create a meshgrid for X and Y values
x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.sin(np.sqrt(X**2 + Y**2))  # Trigonometric function

# Matplotlib 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.title('3D Surface Plot of sin(sqrt(X^2 + Y^2))')
plt.show()

# Plotly 3D surface plot
fig = go.Figure(data=[go.Surface(z=Z, x=x_vals, y=y_vals)])
fig.update_layout(scene=dict(xaxis_title='X Label', yaxis_title='Y Label', zaxis_title='Z Label'),
                  title='3D Surface Plot of sin(sqrt(X^2 + Y^2))')
fig.show()
