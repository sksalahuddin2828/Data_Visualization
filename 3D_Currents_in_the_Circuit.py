import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define symbolic variables
I1, I2, I3 = sp.symbols('I1 I2 I3')

# Define circuit parameters
emf1 = 18  # emf1 value
emf2 = 45  # emf2 value
R1 = 6     # R1 value
R2 = 3     # R2 value
R3 = 2     # R3 value
r1 = 6     # r1 value
r2 = 2     # r2 value

# Define equations from Kirchhoff's rules
eq1 = sp.Eq(I1, I2 + I3)
eq2 = sp.Eq(-I2 * (R2 + r1) + emf1 - I1 * R1, 0)
eq3 = sp.Eq(I1 * R1 + I3 * (R3 + r2) - emf2, 0)

# Solve the system of equations
solution = sp.solve((eq1, eq2, eq3), (I1, I2, I3))

# Extract numerical values
I1_val = solution[I1]
I2_val = solution[I2]
I3_val = solution[I3]

# Create a 3D plot for visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for I1 and I3
I1_vals = np.linspace(0, 10, 100)
I3_vals = np.linspace(0, 10, 100)
I1_mesh, I3_mesh = np.meshgrid(I1_vals, I3_vals)

# Calculate I2 using the equation I2 = 6 - 2I1 - I3
I2_mesh = 6 - 2 * I1_mesh - I3_mesh

# Plot the 3D surface
ax.plot_surface(I1_mesh, I3_mesh, I2_mesh, cmap='viridis')

# Add labels and title
ax.set_xlabel('I1 (A)')
ax.set_ylabel('I3 (A)')
ax.set_zlabel('I2 (A)')
plt.title('Currents in the Circuit')

# Show the plot
plt.show()

# Display the numerical results
print(f"I1 = {I1_val:.2f} A")
print(f"I2 = {I2_val:.2f} A")
print(f"I3 = {I3_val:.2f} A")
