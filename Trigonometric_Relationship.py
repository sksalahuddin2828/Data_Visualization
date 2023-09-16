import numpy as np
import sympy as sp

# Given value
sin_theta = 1/3

# Calculate sec θ
sec_theta = 1 / sp.sqrt(1 - sin_theta**2)

sec_theta_val = sec_theta.evalf()  # Evaluate the result

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a range of values for sin θ
sin_theta_values = np.linspace(0, 1, 100)
cos_theta_values = np.sqrt(1 - sin_theta_values**2)
sec_theta_values = 1 / np.sqrt(1 - sin_theta_values**2)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sin_theta_values, cos_theta_values, sec_theta_values)

ax.set_xlabel('sin θ')
ax.set_ylabel('cos θ')
ax.set_zlabel('sec θ')

plt.show()
