import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# MRI acquisition parameters
# Data at 7 years
b_value_7 = 3000  # s/mm^2
gradient_directions_7 = 45
b0_images_7 = 6
voxel_size_7 = 2.3  # mm^3

# Data at 13 years
b_value_13 = 2800  # s/mm^2
gradient_directions_13 = 60
b0_images_13 = 4
voxel_size_13 = 2.4  # mm^3

# Simulate data for the corpus callosum at 7 years and 13 years
# Assuming the data for each age consists of 3D arrays of size (104, 104, 45) and (110, 110, 60) respectively
data_7 = np.random.rand(104, 104, 45)
data_13 = np.random.rand(110, 110, 60)

# Visualization of corpus callosum at 7 years
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x, y, z = np.meshgrid(np.arange(0, 104), np.arange(0, 104), np.arange(0, 45))
ax.scatter(x, y, z, c=data_7.flatten(), cmap='viridis', marker='o', s=50, alpha=0.6)

ax.set_title("Corpus Callosum at 7 Years")
ax.set_xlabel("X-axis (mm)")
ax.set_ylabel("Y-axis (mm)")
ax.set_zlabel("Z-axis (mm)")

plt.show()

# Visualization of corpus callosum at 13 years
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x, y, z = np.meshgrid(np.arange(0, 110), np.arange(0, 110), np.arange(0, 60))
ax.scatter(x, y, z, c=data_13.flatten(), cmap='plasma', marker='o', s=50, alpha=0.6)

ax.set_title("Corpus Callosum at 13 Years")
ax.set_xlabel("X-axis (mm)")
ax.set_ylabel("Y-axis (mm)")
ax.set_zlabel("Z-axis (mm)")

plt.show()

# Equations for corpus callosum analysis
def calculate_correlation(data):
    # Calculate the correlation between voxel intensities along different gradient directions
    correlations = np.corrcoef(data.reshape(-1, data.shape[-1]).T)
    return correlations

# Perform correlation analysis for the corpus callosum at 7 and 13 years
correlations_7 = calculate_correlation(data_7)
correlations_13 = calculate_correlation(data_13)

# Mathematical dance explanation
print("Mathematical Dance:")
print("The corpus callosum is a fascinating structure that connects the left and right hemispheres of the brain.")
print("Imagine each voxel in the corpus callosum as a tiny dancer, expressing itself in different directions.")
print("Our dancers at 7 years and 13 years move gracefully along various paths, represented by gradient directions.")
print("Let's analyze their correlations to understand their harmonious interactions.")
print("\nEquations:")
print("The correlation matrix for the corpus callosum at 7 years:")
print(correlations_7)
print("\nThe correlation matrix for the corpus callosum at 13 years:")
print(correlations_13)

# Logical Explanation
print("\nLogical Explanation:")
print("A high positive correlation between two voxels indicates that their intensities change together.")
print("On the other hand, a high negative correlation means that their intensities change in opposite directions.")
print("By analyzing the correlation matrices, we can observe the dynamic relationships between our voxel dancers.")
print("Now, let's present this dynamic relationship using a heatmap visualization.")

# Dynamic Heatmap Visualization
def visualize_correlation_heatmap(correlations, title):
    plt.figure(figsize=(8, 6))
    plt.imshow(correlations, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
    plt.colorbar(label="Correlation")
    plt.title(title)
    plt.xlabel("Voxel Index")
    plt.ylabel("Voxel Index")
    plt.show()

# Visualize correlation heatmap for the corpus callosum at 7 years
visualize_correlation_heatmap(correlations_7, "Correlation Heatmap at 7 Years")

# Visualize correlation heatmap for the corpus callosum at 13 years
visualize_correlation_heatmap(correlations_13, "Correlation Heatmap at 13 Years")
