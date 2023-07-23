from mpl_toolkits.mplot3d import Axes3D

# Create a figure and axis for the plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the correlation coefficient 'r' and probable error
ax.scatter([r], [prob_error], [N], c='red', s=100)

# Plot the probable limits as vertical dashed lines
ax.axhline(prob_error, color='green', linestyle='dashed', label='Lower Limit')
ax.axhline(-prob_error, color='green', linestyle='dashed', label='Upper Limit')

# Customize the plot aesthetics
ax.set_xlabel('Correlation Coefficient (r)')
ax.set_ylabel('Probable Error (P.E.)')
ax.set_zlabel('Sample Size (N)')
ax.set_title('Probable Error and Limits for Correlation Coefficient and Sample Size')

# Add artistic elements like annotations and mathematical dance
ax.text(0.75, 0.045, 64, r"P.E. = 0.674 \times \frac{{(1 - r^2)}}{{\sqrt{N}}}", color='white', fontsize=12)
ax.text(0.65, 0.055, 64, f"Probable Limit: ({lower_limit:.3f}, {upper_limit:.3f})", color='white', fontsize=12)

# Customize the legend
ax.legend(loc='upper right')

# Show the plot
plt.show()
