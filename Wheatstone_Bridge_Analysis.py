import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbolic variables
Rx = sp.symbols('Rx')

# Known values
R1 = 100.0
R2 = 220.0
V_source = 5.0
I_measured = 0.0  # To be determined

# Equation based on Wheatstone bridge principle
equation = sp.Eq(I_measured * R1, (V_source / (R2 + Rx)) * Rx)

# Solve for Rx symbolically
solution = sp.solve(equation, Rx)

# Convert symbolic solution to a numeric value
Rx_value = solution[0]

# Simulate a range of measured currents
I_measured_values = np.linspace(0, 2, 100)  # Example current values

# Calculate corresponding Rx values
Rx_values = []
for I_measured in I_measured_values:
    solution = sp.solve(equation.subs({I_measured: I_measured}), Rx)
    Rx_values.append(float(solution[0]))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter([R1], [R2], [Rx_value], c='r', marker='o', label='Balanced Point (Rx)')
ax.plot(I_measured_values, np.full_like(I_measured_values, R2), Rx_values, label='Rx for Different I_measured', linestyle='--')

ax.set_xlabel('I_measured')
ax.set_ylabel('R2')
ax.set_zlabel('Rx')
ax.legend()

plt.title('Wheatstone Bridge Analysis')
plt.show()
