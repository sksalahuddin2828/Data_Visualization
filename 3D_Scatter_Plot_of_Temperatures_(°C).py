import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate some temperature data for illustration
np.random.seed(42)
num_samples = 100
temperature_data = np.random.randint(-10, 40, num_samples)  # Random temperatures between -10°C and 40°C

# Create a DataFrame to store the temperature data
data_df = pd.DataFrame({"Temperature (°C)": temperature_data})

# Visualization: Histogram to show the distribution of temperatures
plt.figure(figsize=(8, 6))
plt.hist(data_df["Temperature (°C)"], bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Distribution of Temperatures (°C)")
plt.grid(True)
plt.show()

# Visualization: Scatter plot to show the equal intervals property
plt.figure(figsize=(8, 6))
plt.scatter(range(len(data_df)), data_df["Temperature (°C)"], color='orange')
plt.xlabel("Index")
plt.ylabel("Temperature (°C)")
plt.title("Scatter Plot of Temperatures (°C)")
plt.grid(True)
plt.show()
