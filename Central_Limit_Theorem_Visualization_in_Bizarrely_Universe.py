import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def bizarrely_universe(num_galaxies, num_dimensions):
    return np.random.randn(num_galaxies, num_dimensions)

def central_limit_theorem(num_galaxies, num_dimensions, num_samples, sample_size):
    sample_means = []
    for _ in range(num_samples):
        galaxies = bizarrely_universe(num_galaxies, num_dimensions)
        mean = np.mean(galaxies[:sample_size])
        sample_means.append(mean)
    return sample_means

def plot_bizarrely_universe(galaxies):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(galaxies[:, 0], galaxies[:, 1], galaxies[:, 2], c='b', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def plot_clt(sample_means):
    fig, ax = plt.subplots()
    ax.hist(sample_means, bins=30, density=True, alpha=0.6, color='b')
    ax.set_xlabel('Sample Means')
    ax.set_ylabel('Frequency')
    ax.set_title('Central Limit Theorem Visualization')

   # Add the labels for 'Frequency' and 'Sample Means' to the plot
    ax.text(0.95, 0.9, 'Frequency', transform=ax.transAxes, ha='right', va='top')
    ax.text(0.05, 0.9, 'Sample Means', transform=ax.transAxes, ha='left', va='top')

    plt.show()

def animate_clt(num_samples, sample_size):
    fig, ax = plt.subplots()
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Sample Means')
    ax.set_ylabel('Frequency')
    ax.set_title('Central Limit Theorem Animation')

    def update_hist(num):
        ax.clear()
        means = central_limit_theorem(num_galaxies, num_dimensions, num, sample_size)
        ax.hist(means, bins=30, density=True, alpha=0.6, color='b')
        ax.set_xlim(-5, 5)
        ax.set_ylim(0, 1)
        ax.set_xlabel('Sample Means')
        ax.set_ylabel('Frequency')
        ax.set_title('Central Limit Theorem Animation (Sample {})'.format(num))

    ani = FuncAnimation(fig, update_hist, frames=num_samples, interval=500, repeat=True)

    # Save the animation to an HTML file
    ani.save('clt_animation.html', writer='html')

# Constants
num_galaxies = 1000
num_dimensions = 3
num_samples = 100
sample_size = 10

# Step 5: Explanation
print("Welcome to the CLT Bizarrely Universe!")
print("In this universe, galaxies are randomly scattered in a 3D space.")
print("Let's visualize the Bizarrely Universe:")

galaxies = bizarrely_universe(num_galaxies, num_dimensions)
plot_bizarrely_universe(galaxies)

print("\nNow, let's apply the Central Limit Theorem.")
print("We'll take {} samples of size {} and observe how their means converge to a Gaussian distribution.".format(num_samples, sample_size))
print("Creating the animation...")

animate_clt(num_samples, sample_size)
