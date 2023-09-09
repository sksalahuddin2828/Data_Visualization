import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.gridspec as gridspec
from ipywidgets import interact
from IPython.display import display

# Define Wheatstone Bridge Equations
R3 = sp.Symbol('R3')
Rx = 100
R1 = 50.0
R2 = 175

eq = sp.Eq(R1 * R3, R2 * Rx)
solution = sp.solve(eq, R3)

# Create a function to visualize the Wheatstone Bridge
def plot_bridge_balance(R3_value):
    # Calculate the voltage across the bridge
    voltage = (R2 * Rx) / (R1 + R2 + R3_value)

    # Create the plot
    fig = plt.figure(figsize=(10, 6))
    gs = gridspec.GridSpec(2, 2, width_ratios=[2, 1])
    ax1 = plt.subplot(gs[:, 0])
    ax2 = plt.subplot(gs[0, 1])
    ax3 = plt.subplot(gs[1, 1])

    # Plot the Wheatstone Bridge
    R_values = [R1, R2, R3_value, Rx]
    labels = ['R1', 'R2', 'R3', 'Rx']
    colors = ['gold', 'lightcoral', 'lightblue', 'lightgreen']

    ax1.pie(R_values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    ax1.set_aspect('equal')
    ax1.set_title('Wheatstone Bridge')

    # Plot the voltage bar chart
    ax2.barh(['Voltage'], voltage, color='royalblue')
    ax2.set_xlim(0, 150)
    ax2.set_xlabel('Voltage (V)')
    ax2.set_title('Voltage across Bridge')

    # Display the equation
    equation_text = f'Equation: {R1}*R3 = {R2}*{Rx}\nR3 = {R3_value:.2f} Ω\nVoltage = {voltage:.2f} V'
    ax3.text(0.5, 0.5, equation_text, fontsize=12, ha='center', va='center', transform=ax3.transAxes)
    ax3.axis('off')

    plt.tight_layout()
    plt.show()

# Interactive widget to adjust R3
interact(plot_bridge_balance, R3_value=(0, 200, 1))

# Display the solution
print("Balancing the Wheatstone Bridge:")
print(f"R3 must be adjusted to {solution[0]:.2f} Ω for balance.")
