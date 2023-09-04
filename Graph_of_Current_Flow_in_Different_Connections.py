import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbolic variables
emf1, emf2, r1, r2, R_load, I = sp.symbols('emf1 emf2 r1 r2 R_load I')

# Define equations for current calculations
current_opposition = (emf1 - emf2) / (r1 + r2)
current_same_sense = (emf1 + emf2) / (r1 + r2 + R_load)

# Define values for variables
values = {
    emf1: 1.5,  # Replace with your values
    emf2: 1.0,  # Replace with your values
    r1: 0.2,    # Replace with your values
    r2: 0.3,    # Replace with your values
    R_load: 5.0  # Replace with your values
}

# Calculate current in both cases
current_opposition_value = current_opposition.subs(values)
current_same_sense_value = current_same_sense.subs(values)

# Print the results
print(f"Current in opposition: {current_opposition_value} A")
print(f"Current in same sense: {current_same_sense_value} A")

# Create a bar chart to visualize the currents
currents = [current_opposition_value, current_same_sense_value]
labels = ['Opposition', 'Same Sense']

plt.bar(labels, currents)
plt.xlabel('Connection Type')
plt.ylabel('Current (A)')
plt.title('Current Flow in Different Connections')
plt.show()
