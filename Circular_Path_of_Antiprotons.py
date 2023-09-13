import numpy as np
import matplotlib.pyplot as plt

# Given parameters
velocity = 5.00e7  # m/s
radius = 2.00  # m

# Mass and charge of antiprotons
mass_antiproton = 1.6726219e-27  # kg (same as proton)
charge_antiproton = -1.60217662e-19  # C (opposite of proton)

# Calculate the magnetic field strength using the centripetal force equation
centripetal_force = mass_antiproton * velocity**2 / radius
magnetic_field_strength = centripetal_force / abs(charge_antiproton)

print(f"The required magnetic field strength is {magnetic_field_strength:.2e} Tesla")

# Visualize the circular path
theta = np.linspace(0, 2 * np.pi, 100)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

plt.figure(figsize=(8, 8))
plt.plot(x, y)
plt.title("Circular Path of Antiprotons")
plt.xlabel("X-coordinate (m)")
plt.ylabel("Y-coordinate (m)")
plt.grid()
plt.axis('equal')
plt.show()


#--------------------------------------------------------------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt

# Given parameters
velocity = 5.00e7  # m/s
radius = 2.00  # m

# Mass and charge of antiprotons
mass_antiproton = 1.6726219e-27  # kg (same as proton)
charge_antiproton = -1.60217662e-19  # C (opposite of proton)

# Calculate the magnetic field strength using the centripetal force equation
centripetal_force = mass_antiproton * velocity**2 / radius
magnetic_field_strength = centripetal_force / abs(charge_antiproton)

print(f"The required magnetic field strength is {magnetic_field_strength:.2e} Tesla")

# Visualize the circular path
theta = np.linspace(0, 2 * np.pi, 100)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

plt.figure(figsize=(8, 8))
plt.plot(x, y)
plt.title("Circular Path of Antiprotons")
plt.xlabel("X-coordinate (m)")
plt.ylabel("Y-coordinate (m)")
plt.grid()
plt.axis('equal')

# Adding annotations for better visualization
plt.text(0, 0, 'Starship Enterprise', ha='center', va='center', fontsize=12, color='blue')
plt.text(radius, 0, 'Antiproton Path', ha='center', va='center', fontsize=12, color='red')

plt.show()
