import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Problem 1
# (a) Calculate power in kW
power_kw = 230
# (b) Calculate current in A
current_a = 960

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define data
x = np.random.rand(10)
y = np.random.rand(10)
z = np.random.rand(10)

# Create scatter plot
ax.scatter(x, y, z, c='r', marker='o')

# Set labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('Creative 3D Visualization')

plt.show()
