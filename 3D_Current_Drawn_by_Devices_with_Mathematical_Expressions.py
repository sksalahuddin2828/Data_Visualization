import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
from sympy.utilities.lambdify import lambdify

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

# Check if the fuse will blow
fuse_blown = total_current > fuse_current

# Create a DataFrame for visualization
device_data = {
    'Device': ['Toaster', 'Frying Pan', 'Lamp'],
    'Power (Watts)': [toaster_power, frying_pan_power, lamp_power],
    'Current (Amperes)': [toaster_current, frying_pan_current, lamp_current]
}

data = pd.DataFrame(device_data)

# Create a bar chart to visualize currents
fig = px.bar(data, x='Device', y='Current (Amperes)',
             text='Current (Amperes)',
             title='Current Drawn by Devices',
             labels={'Current (Amperes)': 'Current (A)'})

# Add a line for the fuse current
fig.add_hline(y=fuse_current, line_dash="dash", line_color="red",
              annotation_text="Fuse Current", annotation_position="top left")

# Display the chart
fig.show()

# Mathematical Expressions and Explanations
x = sp.symbols('x')
power_eq = x * voltage  # General power equation (P = VI)
current_eq = power_eq / voltage  # Ohm's Law (I = P / V)
fuse_eq = fuse_current - total_current  # Fuse current remaining

# Lambdify the fuse equation for numerical evaluation
fuse_eq_numeric = lambdify(x, fuse_eq, "numpy")

# Evaluate the equation for an array of x values
x_vals = np.linspace(0, 20, 100)
power_vals = np.array([power_eq.subs(x, val).evalf() for val in x_vals])
current_vals = np.array([current_eq.subs(x, val).evalf() for val in x_vals])
fuse_vals = np.array([fuse_eq_numeric(val) for val in x_vals])  # Corrected evaluation

plt.figure(figsize=(10, 6))
plt.plot(x_vals, power_vals, label='Power (Watts)')
plt.plot(x_vals, current_vals, label='Current (Amperes)')
plt.plot(x_vals, fuse_vals, label='Remaining Fuse Current (Amperes)', linestyle='--', color='red')
plt.xlabel('Variable x')
plt.ylabel('Value')
plt.legend()
plt.title('Mathematical Expressions')

plt.show()

# Display results and explanations
print(data)
if fuse_blown:
    print("The combination will blow the 15-A fuse.")
else:
    print("The combination will not blow the 15-A fuse.")
