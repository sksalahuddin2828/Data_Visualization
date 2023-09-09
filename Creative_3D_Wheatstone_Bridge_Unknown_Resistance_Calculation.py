import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D

# Simulated data for R1, R2, R3, and Rx
np.random.seed(42)  # Set a seed for reproducibility
num_samples = 100
R1 = np.random.uniform(1, 10, num_samples)
R2 = np.random.uniform(1, 10, num_samples)
R3 = np.random.uniform(1, 10, num_samples)
Rx = (R3 * R2) / R1  # Calculate Rx using the Wheatstone bridge equation

# Create a Pandas DataFrame to manage the data
data = pd.DataFrame({'R1': R1, 'R2': R2, 'R3': R3, 'Rx': Rx})

# Create a 3D scatter plot using Matplotlib (for reference)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(R1, R2, Rx, c=Rx, cmap='viridis', label='Unknown Resistance (Rx)')
ax.set_xlabel('R1')
ax.set_ylabel('R2')
ax.set_zlabel('Rx')
ax.set_title('Wheatstone Bridge - Unknown Resistance Calculation')
cbar = fig.colorbar(ax.scatter(R1, R2, Rx, c=Rx, cmap='viridis'), ax=ax)
cbar.set_label('Rx Value')
plt.legend()

# Create an interactive 3D scatter plot using Plotly
fig_plotly = px.scatter_3d(data, x='R1', y='R2', z='Rx', color='Rx', title='Wheatstone Bridge - Unknown Resistance Calculation', labels={'Rx': 'Unknown Resistance (Rx)'})
fig_plotly.update_layout(scene=dict(xaxis_title='R1', yaxis_title='R2', zaxis_title='Rx'))
fig_plotly.show()
