# Import the necessary libraries
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define circuit parameters
V_battery = 12.0  # Battery voltage in volts
R1 = 1.00  # Resistance of R1 in ohms
R2 = 6.00  # Resistance of R2 in ohms
R3 = 13.00  # Resistance of R3 in ohms

# (a) Calculate total resistance
# Create symbolic variables
I_total, I2 = sp.symbols('I_total I2')
# Define equations for current through R1, R2, and R3
eq1 = sp.Eq(I_total, V_battery / (R1 + R2 + R3))
eq2 = sp.Eq(I2, V_battery / (R2 + R3))
# Solve for I_total and I2
solution = sp.solve([eq1, eq2], (I_total, I2))
total_resistance = V_battery / solution[I_total]

# (b) Calculate IR drop in R1
IR_drop_R1 = solution[I_total] * R1

# (c) Find current I2 through R2
current_I2 = solution[I2]

# (d) Calculate power dissipated by R2
power_R2 = current_I2 ** 2 * R2

# Create a 3D visualization of the circuit
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define resistor dimensions
resistor_width = 0.5
resistor_height = 0.1

# Create rectangles representing R1, R2, and R3
ax.add_collection3d(Poly3DCollection([[(0, 0, 0), (R1, 0, 0), (R1, resistor_width, 0), (0, resistor_width, 0)]], color='r', alpha=0.6, label='R1'))
ax.add_collection3d(Poly3DCollection([[(R1, 0, 0), (R1 + R2, 0, 0), (R1 + R2, resistor_width, 0), (R1, resistor_width, 0)]], color='g', alpha=0.6, label='R2'))
ax.add_collection3d(Poly3DCollection([[(R1 + R2, 0, 0), (R1 + R2 + R3, 0, 0), (R1 + R2 + R3, resistor_width, 0), (R1 + R2, resistor_width, 0)]], color='b', alpha=0.6, label='R3'))

# Customize the plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Circuit Visualization')

# Manually add the legend
legend_elements = [
    plt.Line2D([0], [0], color='r', lw=4, label='R1'),
    plt.Line2D([0], [0], color='g', lw=4, label='R2'),
    plt.Line2D([0], [0], color='b', lw=4, label='R3')
]
ax.legend(handles=legend_elements)

# Display the 3D plot
plt.show()

# Display results in a table
import pandas as pd

results = pd.DataFrame({
    'Total Resistance (Ohms)': [total_resistance],
    'IR Drop in R1 (Volts)': [IR_drop_R1],
    'Current I2 (Amps)': [current_I2],
    'Power Dissipated by R2 (Watts)': [power_R2]
})

print(results)
