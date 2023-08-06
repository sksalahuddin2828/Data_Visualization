import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create 3D plot for the proposition p(x)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['x'], df['p(x)'], zs=0, s=50, c='b', marker='o')
ax.set_xlabel('x')
ax.set_ylabel('p(x)')
ax.set_zlabel('Truth Value')
plt.show()
