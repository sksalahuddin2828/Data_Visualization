import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate probable error
def probable_error(r, N):
    return 0.674 * (1 - r**2) / np.sqrt(N)

# Generate sample data using Pandas
np.random.seed(42)
num_samples = 100
data = pd.DataFrame({
    'Sample': range(1, num_samples + 1),
    'Correlation Coefficient': np.random.uniform(-1, 1, num_samples),
    'Sample Size': np.random.randint(2, 101, num_samples)
})

# Calculate Probable Error using the provided formula
data['Probable Error'] = probable_error(data['Correlation Coefficient'], data['Sample Size'])

# Visualization - 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot the data points
ax.scatter(data['Correlation Coefficient'], data['Sample Size'], data['Probable Error'], c='b', marker='o')

# Add labels and title
ax.set_xlabel('Correlation Coefficient (r)')
ax.set_ylabel('Sample Size (N)')
ax.set_zlabel('Probable Error')
ax.set_title('Probable Error for Correlation Coefficient')

# Show the plot
plt.show()
