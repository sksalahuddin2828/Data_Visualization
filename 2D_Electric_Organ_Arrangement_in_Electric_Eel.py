import pandas as pd
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a dataframe for animal information
animal_data = pd.DataFrame({
    'Animal': ['Electric Eel', 'Platypus', 'Shark'],
    'Voltage (V)': [0.15, 0.03, 0.1],
    'Emf (V)': [600, 30, None],  # None for sharks since it varies
    'Current (A)': [1, None, None]  # None for Platypus and Sharks
})

# Create a dataframe for electric organ information in Electric Eel
electric_organ_data = pd.DataFrame({
    'Number of Rows': [140],
    'Electroplaques per Row': [5000]
})

# Define symbols
voltage_per_cell = 0.15  # V
rows = 140
electroplaques_per_row = 5000

# Calculate total emf
total_emf = voltage_per_cell * rows * electroplaques_per_row

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate 3D data points for electroplaques using numpy meshgrid
x = np.arange(rows)
y = np.arange(electroplaques_per_row)
x, y = np.meshgrid(x, y)
z = np.zeros_like(x)

# Plot the electroplaques
ax.scatter(x, y, z)

# Add labels and titles
ax.set_xlabel('Rows')
ax.set_ylabel('Electroplaques per Row')
ax.set_zlabel('Electroplaques')

plt.title('Electric Organ Arrangement in Electric Eel')
plt.show()
