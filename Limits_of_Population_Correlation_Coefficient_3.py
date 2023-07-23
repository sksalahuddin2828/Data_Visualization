import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to calculate the probable error (P.E.) for 'r'
def probable_error(r, N):
    return 0.674 * (1 - r**2) / np.sqrt(N)

# Function to calculate the standard error (SE) for 'r'
def standard_error(r, N):
    return np.sqrt((1 - r**2) / N)

# Given correlation coefficient (r) and sample size (N)
r = 0.7
N = 64

# Calculate the probable error and standard error
prob_error = probable_error(r, N)
standard_err = standard_error(r, N)

# Calculate the lower and upper limits for the population correlation coefficient
lower_limit = r - prob_error
upper_limit = r + prob_error

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Animation function to update the plot
def update(frame):
    ax.clear()
    
    # Plot correlation coefficient 'r' as a colored circle
    ax.scatter([r], [0], c=[r], cmap='cool', s=200, vmin=-1, vmax=1, edgecolors='k', zorder=2)
    
    # Plot the lower and upper limits as vertical dashed lines
    ax.axvline(lower_limit, color='green', linestyle='dashed', label='Lower Limit')
    ax.axvline(upper_limit, color='blue', linestyle='dashed', label='Upper Limit')
    
    # Set plot limits and labels
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-0.1, 0.1)
    ax.set_xlabel('Correlation Coefficient')
    ax.set_title('Limits of Population Correlation Coefficient')
    
    # Add artistic elements like colors and title
    ax.set_facecolor('#f0f0f0')
    ax.text(0, 0.06, f"P.E. = {prob_error:.3f}\nS.E. = {standard_err:.3f}", ha='center', va='center', fontsize=12)
    
    # Add legend
    ax.legend(loc='upper right')

# Create an animation
animation = FuncAnimation(fig, update, frames=range(100), interval=50)

# Save the animation as a gif (you can also display it with plt.show() instead of saving)
animation.save('correlation_coefficient.gif', writer='imagemagick')

# Display the static plot for the final frame
update(99)
plt.show()
