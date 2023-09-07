import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define symbolic variables
I1, I2, I3 = sp.symbols('I1 I2 I3')

# Kirchhoff's first rule equation: I1 = I2 + I3
equation = sp.Eq(I1, I2 + I3)

# Solve the equation symbolically
solution = sp.solve(equation, I3)

# Create a function to calculate I3 for given values of I1 and I2
calculate_I3 = sp.lambdify((I1, I2), solution[0])

# Define some example current values
I1_val = 5.0  # Amperes
I2_val = 3.0  # Amperes

# Calculate I3 based on the example values
I3_val = calculate_I3(I1_val, I2_val)

# Print the result
print(f"I1 = {I1_val} A")
print(f"I2 = {I2_val} A")
print(f"I3 = {I3_val} A")

# Create a basic circuit visualization
fig, ax = plt.subplots()

# Draw current sources
ax.arrow(0.1, 0.5, 0.3, 0, head_width=0.05, head_length=0.05, fc='blue', ec='blue')
ax.arrow(0.1, 0.5, 0, -0.3, head_width=0.05, head_length=0.05, fc='red', ec='red')

# Draw resistor
ax.add_patch(plt.Rectangle((0.4, 0.45), 0.2, 0.1, fill=None))

# Add labels
ax.text(0.2, 0.7, f'I1 = {I1_val} A', color='blue')
ax.text(0.2, 0.2, f'I2 = {I2_val} A', color='red')
ax.text(0.5, 0.45, f'I3 = {I3_val} A', color='black')

# Set axis limits and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# Show the circuit
plt.show()
