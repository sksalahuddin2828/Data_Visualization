import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# Function to calculate the probable error for 'r'
def probable_error(r, N):
    return 0.674 * (1 - r**2) / np.sqrt(N)

# Generate data points for correlation coefficient (r) and sample size (N)
r_values = np.linspace(-1, 1, 100)
N_values = np.arange(10, 201, 10)

# Create a meshgrid from the data points
R, N = np.meshgrid(r_values, N_values)

# Calculate the probable error for each combination of 'r' and 'N'
pe_values = probable_error(R, N)

# Create the figure and axis for the plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D surface with the probable error values
surf = ax.plot_surface(R, N, pe_values, cmap='cool', rstride=1, cstride=1, linewidth=0, antialiased=True)

# Customize the plot aesthetics
ax.set_xlabel('Correlation Coefficient (r)')
ax.set_ylabel('Sample Size (N)')
ax.set_zlabel('Probable Error (P.E.)')
ax.set_title('Probable Error for Correlation Coefficient and Sample Size')

# Add artistic elements and annotations
ax.text(0.7, 200, 0.04, r"$P.E. = 0.674 \times \frac{{(1 - r^2)}}{{\sqrt{N}}}$", color='white', fontsize=16)
ax.text(0.7, 220, 0.04, "Slide the values of 'r' and 'N'", color='white', fontsize=14)

# Customize the colorbar
cbar = plt.colorbar(surf, shrink=0.5, aspect=10)
cbar.set_label('Probable Error (P.E.)', rotation=270, labelpad=15)

# Add interactive sliders for 'r' and 'N'
ax_r = plt.axes([0.2, 0.03, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_N = plt.axes([0.2, 0.08, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_r = Slider(ax_r, 'Correlation (r)', -1, 1, valinit=0.7)
slider_N = Slider(ax_N, 'Sample Size (N)', 10, 200, valinit=64)

def update(val):
    r = slider_r.val
    N = slider_N.val
    pe_values = probable_error(R, N)
    surf.remove()
    surf = ax.plot_surface(R, N, pe_values, cmap='cool', rstride=1, cstride=1, linewidth=0, antialiased=True)
    ax.set_title(f'Probable Error for Correlation Coefficient (r={r}) and Sample Size (N={N})')
    fig.canvas.draw_idle()

slider_r.on_changed(update)
slider_N.on_changed(update)

# Show the plot
plt.show()
