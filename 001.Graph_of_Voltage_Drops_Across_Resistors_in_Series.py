import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define the resistor values
R1 = 10  # Ohms
R2 = 20  # Ohms
R3 = 30  # Ohms

# Define the total resistance in series
Rs = R1 + R2 + R3

# Define the voltage source
V = 50  # Volts

# Calculate the current using Ohm's law (I = V / Rs)
I = V / Rs

# Calculate the voltage drops across each resistor
V1 = I * R1
V2 = I * R2
V3 = I * R3

# Create a pie chart to visualize voltage drops
labels = ['R1', 'R2', 'R3']
voltages = [V1, V2, V3]
colors = ['#ff9999', '#66b3ff', '#99ff99']
plt.figure(figsize=(8, 8))
plt.pie(voltages, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Voltage Drops Across Resistors in Series')
plt.show()

# Create a bar chart to visualize voltage drops
resistors = ['R1', 'R2', 'R3']
voltages = [V1, V2, V3]
plt.figure(figsize=(10, 6))
plt.bar(resistors, voltages, color=colors)
plt.xlabel('Resistor')
plt.ylabel('Voltage Drop (V)')
plt.title('Voltage Drops Across Resistors in Series')
plt.show()

# Symbolic representation of the equation V = V1 + V2 + V3
V, V1, V2, V3 = sp.symbols('V V1 V2 V3')
eq = sp.Eq(V, V1 + V2 + V3)
solution = sp.solve(eq, V)
print(f'Symbolic equation: {eq}')
print(f'Solution for V: {solution[0]}')
