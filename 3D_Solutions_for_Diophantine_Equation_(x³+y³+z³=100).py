import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def find_diophantine_solution(k):
    for x in range(-k, k+1):
        for y in range(-k, k+1):
            for z in range(-k, k+1):
                if x**3 + y**3 + z**3 == k:
                    return x, y, z
    return None, None, None

def update_plot(frame):
    ax.cla()  # Clear the previous frame
    k = frame + 1
    x, y, z = find_diophantine_solution(k)

    if x is not None:
        ax.scatter(x, y, z, c=[k], marker='o', s=100, cmap='viridis')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title(f'Solutions for Diophantine Equation x³ + y³ + z³ = {k}')

k_values = list(range(1, 101))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create the animation
animation = FuncAnimation(fig, update_plot, frames=len(k_values), interval=500, repeat=False)

# Save the animation as a gif (optional)
animation.save('diophantine_animation.gif', writer='imagemagick', fps=2)

plt.show()
