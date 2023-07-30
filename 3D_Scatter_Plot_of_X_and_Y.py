import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate random data for two variables
np.random.seed(42)
num_samples = 100
X = np.random.rand(num_samples) * 10
Y = 2 * X + np.random.randn(num_samples) * 2

# Perform statistical analysis
mean_X = np.mean(X)
mean_Y = np.mean(Y)
correlation = np.corrcoef(X, Y)[0, 1]

# Create a DataFrame to store the data
data_df = pd.DataFrame({"X": X, "Y": Y})

# Create 3D visualization
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(data_df["X"], data_df["Y"], c='b', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('3D Scatter Plot of X and Y')
plt.show()

# Print statistical results
print("Mean of X:", mean_X)
print("Mean of Y:", mean_Y)
print("Correlation between X and Y:", correlation)
