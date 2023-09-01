import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Constants
voltage = 120  # Volts
fuse_current = 15  # Amperes

# Power ratings of devices
toaster_power = 1800  # Watts
frying_pan_power = 1400  # Watts
lamp_power = 75  # Watts

# Calculate currents
toaster_current = toaster_power / voltage
frying_pan_current = frying_pan_power / voltage
lamp_current = lamp_power / voltage

# Total current
total_current = toaster_current + frying_pan_current + lamp_current

# Create a DataFrame for visualization
device_data = {
    'Device': ['Toaster', 'Frying Pan', 'Lamp'],
    'Power (Watts)': [toaster_power, frying_pan_power, lamp_power],
    'Current (Amperes)': [toaster_current, frying_pan_current, lamp_current]
}

# Mathematical Expressions
x = sp.symbols('x')
power_eq = x * voltage  # General power equation (P = VI)
current_eq = power_eq / voltage  # Ohm's Law (I = P / V)
fuse_eq = fuse_current - total_current  # Fuse current remaining

# Lambdify the fuse equation for numerical evaluation
fuse_eq_numeric = lambdify(x, fuse_eq, "numpy")

# Create a range of resistance values
resistance_values = np.linspace(0.1, 20, 200)

# Function to update the plot in each animation frame
def update(frame):
    plt.cla()
    resistance = resistance_values[frame]
    current = voltage / (toaster_power / resistance + frying_pan_power / resistance + lamp_power / resistance)
    remaining_fuse_current = fuse_eq_numeric(resistance)
    
    # Plot current vs. resistance
    plt.plot(resistance_values[:frame], currents[:frame], label='Current (Amperes)')
    plt.xlabel('Resistance (Ohms)')
    plt.ylabel('Value')
    plt.title('Current vs. Resistance')
    plt.legend(loc='upper right')
    
    # Plot remaining fuse current vs. resistance
    plt.plot(resistance_values[:frame], fuse_currents[:frame], linestyle='--', color='red', label='Remaining Fuse Current (Amperes)')
    plt.legend(loc='upper right')

# Initialize arrays to store current and fuse current values
currents = []
fuse_currents = []

# Calculate current and fuse current for each resistance value
for resistance in resistance_values:
    current_val = voltage / (toaster_power / resistance + frying_pan_power / resistance + lamp_power / resistance)
    remaining_fuse_current_val = fuse_eq_numeric(resistance)
    currents.append(current_val)
    fuse_currents.append(remaining_fuse_current_val)

# Create an animation
fig, ax = plt.subplots(figsize=(10, 6))
ani = FuncAnimation(fig, update, frames=len(resistance_values), repeat=False)

# Display the animation as HTML
html_output = HTML(ani.to_jshtml())

# Save the animation as an HTML file (optional)
# html_output.save('circuit_animation.html')

# Display results and explanations
print(device_data)
plt.show()
html_output
