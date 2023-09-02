import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp

# Define circuit parameters
V_battery = 12.0  # Volts
R1 = 1.00  # Ohms
R2 = 6.00  # Ohms
R3 = 13.00  # Ohms

# Calculate total resistance (a)
R_parallel = 1 / (1/R2 + 1/R3)
R_total = R1 + R_parallel

# Calculate current through the circuit
I_total = V_battery / R_total

# Calculate IR drop in R1 (b)
IR_drop_R1 = I_total * R1

# Calculate current through R2 (c)
I_R2 = V_battery / (R1 + R_parallel)

# Calculate power dissipated by R2 (d)
P_R2 = I_R2 ** 2 * R2

# Create a DataFrame to store and display the results
results = pd.DataFrame({
    'Total Resistance (a)': [R_total],
    'IR Drop in R1 (b)': [IR_drop_R1],
    'Current I2 (c)': [I_R2],
    'Power Dissipated by R2 (d)': [P_R2]
})

# Create a basic 3D visualization (not a detailed circuit)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Represent resistors as 3D boxes
ax.bar3d(0, 0, 0, 1, 1, R1, shade=True, color='r', alpha=0.5, label='R1')
ax.bar3d(0, 0, R1, 1, 1, R_parallel, shade=True, color='g', alpha=0.5, label='R2+R3')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Circuit Visualization')
# ax.legend()

# Display the results
print(results)

# Show the 3D visualization
plt.show()
