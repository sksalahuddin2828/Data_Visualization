import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import torch
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import fsolve

# Define constants
emf_nicad = 1.25  # Nicad cell emf (V)
emf_alkaline = 1.58  # Alkaline cell emf (V)
resistance_radio = 3.20  # Radio resistance (Ω)
internal_resistance_nicad = 0.0400  # Internal resistance of Nicad cell (Ω)
internal_resistance_alkaline = 0.200  # Internal resistance of Alkaline cell (Ω)

# Define a function to calculate power delivered to the radio
def power_delivered(emf, internal_resistance, load_resistance):
    current = emf / (internal_resistance + load_resistance)
    power = current ** 2 * load_resistance
    return power

# (a) Draw a circuit diagram of the radio and its batteries (use a drawing library or tool)

# (b) Calculate power delivered using Nicad cells
load_resistance = resistance_radio  # Effective resistance of the radio
power_nicad = power_delivered(emf_nicad, internal_resistance_nicad, load_resistance)

# (c) Calculate power delivered using Alkaline cells
power_alkaline = power_delivered(emf_alkaline, internal_resistance_alkaline, load_resistance)

# (d) Compare the powers and plot the results
print(f"Power delivered with Nicad cells: {power_nicad} Watts")
print(f"Power delivered with Alkaline cells: {power_alkaline} Watts")

# Visualization using matplotlib
# Create a 3D bar chart to show the power comparison
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = ['Nicad', 'Alkaline']
y = [power_nicad, power_alkaline]
z = [0, 1]

ax.bar(x, y, z, zdir='y', color=['blue', 'green'])
ax.set_xlabel('Battery Type')
ax.set_ylabel('Power (Watts)')
ax.set_zlabel('')

plt.title('Power Delivered by Battery Type')
plt.show()
