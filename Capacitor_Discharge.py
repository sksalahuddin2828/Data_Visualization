import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define symbols
t, V0, R, C = sp.symbols('t V0 R C')

# Define the equation
equation = sp.Eq(V0 * sp.exp(-t / (R * C)), 0)

# Calculate the discharge time numerically
from scipy.optimize import fsolve

# Define a function to find the root of the equation
def find_discharge_time(t):
    return V0_val * np.exp(-t / (R_val * C_val))

# Initial guess for the root
initial_guess = 0.1  # You may need to adjust this based on your specific case

# Find the root (time to reach zero voltage)
time_to_zero = fsolve(find_discharge_time, initial_guess)

print(f"Time to reach zero voltage: {time_to_zero[0]} seconds")

# Create a 3D visualization
t_vals = np.linspace(0, float(time_to_zero[0]), 100)
V_vals = [V0_val * np.exp(-t / (R_val * C_val)) for t in t_vals]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(t_vals, V_vals, t_vals)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Voltage (V)')
ax.set_title('Capacitor Discharge')

plt.show()
