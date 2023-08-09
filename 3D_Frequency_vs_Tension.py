import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
import pandas as pd

# Define constants
mu = 0.03  # Linear density in kg/m
tension_values = [10, 20, 30, 40]  # Tension values in N
length = 2.0  # Length of the string in meters

# Calculate wave speed for different tension values
wave_speeds = [np.sqrt(tension / mu) for tension in tension_values]

# Calculate frequencies based on wave speed
frequencies = [wave_speed / length for wave_speed in wave_speeds]

# Create a Pandas DataFrame for results
results_df = pd.DataFrame({'Tension (N)': tension_values, 'Wave Speed (m/s)': wave_speeds, 'Frequency (Hz)': frequencies})

# Display results
print(results_df)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(tension_values, frequencies, marker='o')
plt.xlabel('Tension (N)')
plt.ylabel('Frequency (Hz)')
plt.title('Frequency vs. Tension')
plt.grid(True)
plt.show()
