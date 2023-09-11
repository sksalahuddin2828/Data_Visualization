import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbols for the variables
R, C, V, t = sp.symbols('R C V t')

# Define the RC time constant (τ) equation
tau = R * C

# Define the current equation (I) as a function of time
I = (V / R) * sp.exp(-t / tau)

# Create a function to calculate τ and I for given R and V values
def calculate_tau_and_current(R_value, V_value):
    tau_value = float(tau.subs({R: R_value, C: 1}))  # Convert to float
    I_values = [I.subs({R: R_value, V: V_value, C: 1, t: t_value}).evalf() for t_value in np.linspace(0, 5 * tau_value, 100)]
    return tau_value, I_values

# Example usage:
R_value = 10  # Initial resistance
V_value = 100  # Initial voltage

# Calculate τ and I for the initial values
tau_initial, I_initial = calculate_tau_and_current(R_value, V_value)

# Plot τ and I as functions of time
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.plot(np.linspace(0, 5 * tau_initial, 100), I_initial)
plt.xlabel('Time')
plt.ylabel('Current (I)')
plt.title('Current vs. Time')

plt.subplot(122)
plt.plot(R_value, tau_initial, 'ro')
plt.xlabel('Resistance (R)')
plt.ylabel('RC Time Constant (τ)')
plt.title('RC Time Constant vs. Resistance')

plt.tight_layout()
plt.show()
