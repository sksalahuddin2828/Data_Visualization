import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Given tan(x)
tan_x = 5/12

# Calculate sec(x)
sec_x = np.sqrt(1 + tan_x**2)

# Visualization
x = np.linspace(0, 2*np.pi, 100)
y = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

plt.title('3D Visualization')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()

print(f"The value of sec(x) is: {sec_x}")


#--------------------------------------------------------------------------------------------------------------


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Given tan(x)
tan_x = 5/12

# Calculate sec(x)
sec_x = np.sqrt(1 + tan_x**2)

# Create a DataFrame for visualization
x_values = np.linspace(0, 2*np.pi, 100)
y_values = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(x_values, y_values)
Z = np.sin(X) * np.cos(Y)

df = pd.DataFrame({'X': X.flatten(), 'Y': Y.flatten(), 'Z': Z.flatten()})

# Create an interactive 3D surface plot using Plotly
fig = px.scatter_3d(df, x='X', y='Y', z='Z', color='Z', opacity=0.7)
fig.update_layout(scene=dict(zaxis_title='Z-axis', xaxis_title='X-axis', yaxis_title='Y-axis'))

# Create a table to display sec(x) value
sec_df = pd.DataFrame({'sec(x)': [sec_x]})

fig_sec = go.Figure(data=[go.Table(header=dict(values=["sec(x)"]), cells=dict(values=[sec_df['sec(x)']]))])

# Display the interactive visualizations
fig.show()
fig_sec.show()

print(f"The value of sec(x) is: {sec_x}")
