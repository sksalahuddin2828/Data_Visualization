import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate Data for Visualization
a_vals = np.linspace(0.1, 2*np.pi, 100)  # Avoid a=0 for division
results = [a_val**2 - np.sin(2*a_val)**2 / (4*a_val) for a_val in a_vals]

# Create DataFrame
df = pd.DataFrame({'a': a_vals, 'result': results})

# Matplotlib 3D Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(df['a'], df['result'], df['a'])
ax.set_xlabel('a')
ax.set_ylabel('Expected Result')
ax.set_zlabel('Integral Result')

plt.show()
