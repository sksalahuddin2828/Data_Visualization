import numpy as np
import pandas as pd
import plotly.express as px

# Constants
mu_0 = 4 * np.pi * 1e-7  # Magnetic constant (permeability of free space)

# Define the magnetic field vector (B) and current vector (I) for each case
data = {
    'Case': ['a', 'b', 'c', 'd', 'e', 'f'],
    'B_x': [0, 1, 0, 1, 0, -1],
    'B_y': [0, 0, 1, 0, -1, 0],
    'B_z': [-1, 0, 0, 0, 0, 0],
    'I_x': [0, 0, 1, -1, 0, 0],
    'I_y': [0, -1, 0, 0, 0, 0],
    'I_z': [-1, 0, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

# Calculate the magnetic force vector (F) for each case
df['F_x'] = df['I_y'] * df['B_z'] - df['I_z'] * df['B_y']
df['F_y'] = df['I_z'] * df['B_x'] - df['I_x'] * df['B_z']
df['F_z'] = df['I_x'] * df['B_y'] - df['I_y'] * df['B_x']

# Calculate the magnitude of the magnetic force
df['F_mag'] = np.sqrt(df['F_x'] ** 2 + df['F_y'] ** 2 + df['F_z'] ** 2)

# Calculate the theoretical magnitude of the magnetic force using the formula F = I * B
df['F_theoretical'] = np.sqrt(df['I_x'] ** 2 + df['I_y'] ** 2 + df['I_z'] ** 2) * np.sqrt(df['B_x'] ** 2 + df['B_y'] ** 2 + df['B_z'] ** 2) * mu_0

# Create an interactive 3D scatter plot
fig = px.scatter_3d(df, x='F_x', y='F_y', z='F_z', color='Case',
                     labels={'F_x': 'F_x', 'F_y': 'F_y', 'F_z': 'F_z'},
                     title='Magnetic Force on Current (Figure 5 Cases)')

# Customize the layout
fig.update_layout(scene=dict(aspectmode="cube"))
fig.update_traces(marker=dict(size=5))

# Show the interactive plot
fig.show()

# Explanation and Theory
print("Explanation and Theory:")
for index, row in df.iterrows():
    case = row['Case']
    F_mag = row['F_mag']
    F_theoretical = row['F_theoretical']
    
    print(f"Case {case}:")
    print(f"   Magnitude of Magnetic Force (Calculated): {F_mag:.4e} N")
    print(f"   Magnitude of Magnetic Force (Theoretical): {F_theoretical:.4e} N")
    print()
