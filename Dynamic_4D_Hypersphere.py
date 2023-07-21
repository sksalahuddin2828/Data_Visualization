import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import ipywidgets as widgets
from IPython.display import display, clear_output

# Define the number of points on the hypersphere
num_points = 5000

# Generate random 4D points with coordinates between -1 and 1
points = np.random.uniform(-1, 1, (num_points, 4))

# Normalize the points to lie on the hypersphere surface
points /= np.linalg.norm(points, axis=1)[:, None]

# Create a figure and 3D axes for the initial view
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Function to set dynamic axis limits
def set_dynamic_axis_limits(points):
    max_range = np.max(np.abs(points))
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_zlim(-max_range, max_range)

# Set dynamic axis limits for the initial points
set_dynamic_axis_limits(points)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Function to update the plot during animation
def update_plot(frame):
    # Clear the previous plot
    ax.clear()
    
    # Apply complex mathematical transformations to the points
    t = frame / 100.0 * speed_slider.value
    transformed_points = np.empty_like(points)
    for j, point in enumerate(points):
        x, y, z, w = point
        transformed_points[j] = [
            np.cos(3 * x + 2 * np.sin(4 * w * t)),           # X coordinate transformation
            y * np.sin(5 * y * t) + z * np.cos(3 * z * t),  # Y coordinate transformation
            np.sin(x * w * t) * np.cos(y * w * t),          # Z coordinate transformation
            np.sin(w * t) * np.cos(3 * x * t)               # W coordinate transformation
        ]

    # Normalize the transformed points to lie on the hypersphere surface
    transformed_points /= np.linalg.norm(transformed_points, axis=1)[:, None]

    # Get colors based on the custom color palette
    colors = np.array([get_custom_color(w) for w in transformed_points[:, 3]])

    # Plot the 3D hypersphere with colored points
    ax.scatter(transformed_points[:, 0], transformed_points[:, 1], transformed_points[:, 2], s=2, c=colors, alpha=0.7)

    # Set dynamic axis limits for the transformed points
    set_dynamic_axis_limits(transformed_points)

# Function to update interactive parameters
def update_params(change):
    global num_frames, ani
    num_frames = frames_slider.value
    ani = FuncAnimation(fig, update_plot, frames=np.arange(num_frames), interval=50)
    plt.close()  # Close the existing plot to prevent duplicate display

# Create interactive controls using ipywidgets
speed_slider = widgets.FloatSlider(min=0.1, max=3, step=0.1, value=1.0, description='Speed Factor')
frames_slider = widgets.IntSlider(min=50, max=200, step=10, value=100, description='Number of Frames')
frames_slider.observe(update_params, names='value')
display(speed_slider, frames_slider)

# Function to generate custom colors based on the W coordinate
def get_custom_color(w):
    r = np.abs(np.sin(2 * np.pi * w))
    g = np.abs(np.cos(2 * np.pi * w))
    b = 0.7
    return (r, g, b)

# Set the initial number of frames and show the plot
num_frames = frames_slider.value
ani = FuncAnimation(fig, update_plot, frames=np.arange(num_frames), interval=50)
display(fig)  # Explicitly display the plot using IPython.display

# Close the initial plot to prevent duplicate display
plt.close(fig)
