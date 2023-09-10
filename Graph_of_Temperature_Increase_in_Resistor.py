import matplotlib.pyplot as plt

V = 450  # Voltage in Volts
m = 2.50e-3  # Mass in kg
c = 1.67e3  # Specific heat capacity in J/(kg°C)

# Calculate the energy dissipated in the resistor
Q = 0.5 * C * V**2

delta_T = Q / (m * c)

# Create a bar chart
labels = ['Initial Temperature', 'Final Temperature']
temperatures = [25, 25 + delta_T]

plt.bar(labels, temperatures, color=['blue', 'red'])
plt.ylabel('Temperature (°C)')
plt.title('Temperature Increase in Resistor')
plt.show()
