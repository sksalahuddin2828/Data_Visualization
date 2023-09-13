import numpy as np
import matplotlib.pyplot as plt

# Problem 1: Direction of Magnetic Force for Positive Charge
directions = ["Left (West)", "Into the page", "Up (North)", "No force", "Right (East)", "Down (South)"]
angles = np.arange(0, 360, 60)

# Create a polar plot to represent directions
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, polar=True)

ax.set_xticks(np.radians(angles))
ax.set_xticklabels(directions)
ax.set_yticklabels([])

# Plot arrows representing directions
for angle in np.radians(angles):
    ax.annotate("", xy=(angle, 1), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", lw=2))

ax.set_title("Direction of Magnetic Force for Positive Charge")
plt.show()

# Problem 3: Direction of Velocity for Negative Charge
directions = ["East (right)", "Into the page", "South (down)"]
angles = np.arange(0, 360, 120)

# Create a polar plot to represent directions
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, polar=True)

ax.set_xticks(np.radians(angles))
ax.set_xticklabels(directions)
ax.set_yticklabels([])

# Plot arrows representing directions
for angle in np.radians(angles):
    ax.annotate("", xy=(angle, 1), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", lw=2))

ax.set_title("Direction of Velocity for Negative Charge")
plt.show()

# Problem 5: Direction of Magnetic Field
directions = ["Into page", "West (left)", "Out of page"]
angles = np.arange(0, 360, 120)

# Create a polar plot to represent directions
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, polar=True)

ax.set_xticks(np.radians(angles))
ax.set_xticklabels(directions)
ax.set_yticklabels([])

# Plot arrows representing directions
for angle in np.radians(angles):
    ax.annotate("", xy=(angle, 1), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", lw=2))

ax.set_title("Direction of Magnetic Field")
plt.show()

# Problem 7: Magnetic Force Calculation
q = 0.100e-6  # Charge in Coulombs
v = 5.00  # Speed in m/s
B = 1.50  # Magnetic field in Tesla

F = q * v * B
print("Maximum force on the aluminum rod:", F, "N, perpendicular to both the magnetic field lines and the velocity")

# Problem 9: Magnetic Field Strength Calculation
F = 7.50e-7  # Force in N
v = 5.00  # Speed in m/s

B = F / (q * v)
print("Magnetic field strength:", B, "T")

# Problem 10: Magnetic Field Calculation
F = 6.67e-10  # Force in N
v = 660  # Speed in m/s

B = F / (q * v)
print("Magnetic field strength:", B, "T")
