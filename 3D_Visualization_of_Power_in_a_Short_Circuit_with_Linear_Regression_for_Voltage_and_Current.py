import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
import plotly.express as px
import torch
from sklearn.linear_model import LinearRegression
from scipy.optimize import fsolve

# Given values
voltage = 240  # Volts
resistance = 0.250  # Ohms

# (a) Calculate power dissipation
current = voltage / resistance
power_dissipated = voltage * current

# (b) Calculate current
voltage_symbol, resistance_symbol, current_symbol = symbols('V R I')
ohms_law_eq = Eq(voltage_symbol, resistance_symbol * current_symbol)
current_solution = solve(ohms_law_eq.subs({voltage_symbol: voltage, resistance_symbol: resistance}), current_symbol)

# Convert current_solution to float
current_solution = float(current_solution[0])

# Create a Pandas DataFrame for presentation
data = {'Parameter': ['Voltage (V)', 'Resistance (Ω)', 'Current (A)', 'Power (W)'],
        'Value': [voltage, resistance, current_solution, power_dissipated]}
df = pd.DataFrame(data)

# Plot using Plotly
fig = px.bar(df, x='Parameter', y='Value',
             title='Short Circuit Analysis', labels={'Parameter': 'Parameters', 'Value': 'Values'},
             template='plotly_dark')
fig.show()

# Visualize with Matplotlib (3D visualization)
current_range = np.linspace(0, 10, 100)
voltage_range = resistance * current_range

fig_3d = plt.figure(figsize=(10, 6))
ax = fig_3d.add_subplot(111, projection='3d')
ax.plot(current_range, voltage_range, current_range**2, label='Power (W = I^2*R)')
ax.set_xlabel('Current (A)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Power (W)')
ax.legend()
plt.title('3D Visualization of Power in a Short Circuit')
plt.show()

# Mathematical Dance
time = np.linspace(0, 10, 100)
amplitude = np.sin(time)
plt.figure(figsize=(8, 4))
plt.plot(time, amplitude, label='sin(time)')
plt.title('Mathematical Dance: Sinusoidal Amplitude')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Linear Regression with PyTorch
x_train = torch.tensor(current_range, dtype=torch.float32).view(-1, 1)
y_train = torch.tensor(voltage_range, dtype=torch.float32).view(-1, 1)
model = torch.nn.Linear(1, 1)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(1000):
    optimizer.zero_grad()
    outputs = model(x_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

predicted_voltages = model(x_train).detach().numpy()

plt.figure(figsize=(8, 4))
plt.scatter(current_range, voltage_range, label='Actual Data')
plt.plot(current_range, predicted_voltages, label='Linear Regression', color='r')
plt.title('Linear Regression for Voltage and Current')
plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.show()

# Solve equation using SciPy
def equation_to_solve(x):
    return x**2 * resistance - power_dissipated

initial_guess = 1.0
solved_current = fsolve(equation_to_solve, initial_guess)[0]

print(f"Solved Current: {solved_current:.4f} A")

# Display the DataFrame
print(df)
