import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Example 2: Visualize p → q and its contrapositive ~q → ~p in 3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot p → q
ax.scatter(df['p'], df['q'], df['p → q'], color='b', label='p → q')

# Plot ~q → ~p
ax.scatter(df['p'], df['q'], df['~q → ~p'], color='r', label='~q → ~p')

# Set labels and title
ax.set_xlabel('p')
ax.set_ylabel('q')
ax.set_zlabel('Result')
ax.set_title('Conditional and Contrapositive Visualization')
ax.legend()

plt.show()
