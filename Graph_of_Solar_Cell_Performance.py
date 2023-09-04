import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulated solar cell data
data = {
    'Incident_Solar_Radiation': np.arange(0, 1000, 100),  # Varying incident radiation
    'Voltage_Output': np.array([0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]),  # Sample voltage data
    'Current_Output': np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])  # Sample current data
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Data analysis
mean_voltage = df['Voltage_Output'].mean()
max_current = df['Current_Output'].max()

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(df['Incident_Solar_Radiation'], df['Voltage_Output'], label='Voltage Output')
plt.scatter(df['Incident_Solar_Radiation'], df['Current_Output'], label='Current Output')
plt.xlabel('Incident Solar Radiation')
plt.ylabel('Voltage / Current Output')
plt.title('Solar Cell Performance')
plt.legend()
plt.grid(True)

# Display analysis results
print(f"Mean Voltage Output: {mean_voltage}")
print(f"Max Current Output: {max_current}")

# Show the plot
plt.show()
