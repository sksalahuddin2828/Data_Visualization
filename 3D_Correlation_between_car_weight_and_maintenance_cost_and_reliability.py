# pip install numpy pandas matplotlib seaborn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data (you can replace this with your actual data)
car_data = pd.DataFrame({
    'car_weight': [1500, 1800, 2000, 2200, 2400],
    'reliability': [0.9, 0.8, 0.7, 0.6, 0.5],
    'maintenance_cost': [1000, 1200, 1500, 1800, 2000]
})

# Calculate correlation coefficients
correlation_reliability = np.corrcoef(car_data['car_weight'], car_data['reliability'])[0, 1]
correlation_maintenance_cost = np.corrcoef(car_data['car_weight'], car_data['maintenance_cost'])[0, 1]

# Print correlation coefficients
print("Correlation between car weight and reliability:", correlation_reliability)
print("Correlation between car weight and maintenance cost:", correlation_maintenance_cost)

# Visualize the data and correlations
sns.set(style='whitegrid', font_scale=1.2)

# Scatter plot for car weight and reliability
plt.figure(figsize=(8, 6))
sns.scatterplot(data=car_data, x='car_weight', y='reliability', s=100, color='blue')
plt.xlabel('Car Weight')
plt.ylabel('Reliability')
plt.title('Scatter plot of Car Weight vs. Reliability')
plt.show()

# Scatter plot for car weight and maintenance cost
plt.figure(figsize=(8, 6))
sns.scatterplot(data=car_data, x='car_weight', y='maintenance_cost', s=100, color='green')
plt.xlabel('Car Weight')
plt.ylabel('Maintenance Cost')
plt.title('Scatter plot of Car Weight vs. Maintenance Cost')
plt.show()
