import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import sympy as sp
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

# Simulated data for R1, R2, R3, and Rx
np.random.seed(42)
num_samples = 100
R1 = np.random.uniform(1, 10, num_samples)
R2 = np.random.uniform(1, 10, num_samples)
R3 = np.random.uniform(1, 10, num_samples)

# Function to calculate Rx using the Wheatstone bridge equation
def calculate_rx(r1, r2, r3):
    return (r3 * r2) / r1

Rx = [calculate_rx(r1, r2, r3) for r1, r2, r3 in zip(R1, R2, R3)]

# Create a Pandas DataFrame to manage the data
data = pd.DataFrame({'R1': R1, 'R2': R2, 'R3': R3, 'Rx': Rx})

# Create a dynamic animation showing how Rx changes with different R3 values
fig_anim, ax = plt.subplots(figsize=(10, 8))
ax.set_xlabel('R1')
ax.set_ylabel('Rx')
sc = ax.scatter(R1, Rx, c=R3, cmap='viridis')

def update(frame):
    ax.clear()
    ax.set_xlabel('R1')
    ax.set_ylabel('Rx')
    Rx = calculate_rx(R1, R2, frame)
    sc = ax.scatter(R1, Rx, c=R3, cmap='viridis')
    return sc,

ani = FuncAnimation(fig_anim, update, frames=np.linspace(1, 10, 100), repeat=False)

# Display the animation (for Jupyter Notebook)
HTML(ani.to_jshtml())
