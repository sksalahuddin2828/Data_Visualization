import numpy as np
import pandas as pd
import plotly.express as px
from sympy import Symbol, Eq, solve

# Define the given values and range for EMF and load resistance
emf_values = np.linspace(5.0, 15.0, 100)
load_resistance_values = np.linspace(0.1, 2.0, 100)

# Initialize empty lists to store data for animation
frames = []

# Function to calculate current and power for a given EMF and load resistance
def calculate_emf_load(emf, load_resistance):
    I = emf / load_resistance
    P_load = I**2 * load_resistance
    return I, P_load

# Perform calculations and store data for each frame
for emf in emf_values:
    for load_resistance in load_resistance_values:
        I, P_load = calculate_emf_load(emf, load_resistance)
        frames.append({'EMF (Volts)': emf, 'Load Resistance (Ohms)': load_resistance,
                       'Current (A)': I, 'Power (Watts)': P_load})

# Create a DataFrame to store the data
df = pd.DataFrame(frames)

# Create a scatter plot for battery characteristics
fig_battery = px.scatter(df, x='Load Resistance (Ohms)', y='Current (A)', animation_frame='EMF (Volts)',
                         title='Battery Characteristics', labels={'Load Resistance (Ohms)': 'Load Resistance'},
                         range_x=[0.1, 2.0], range_y=[0, 15])

# Create a 3D surface plot for power dissipation
fig_power = px.scatter_3d(df, x='EMF (Volts)', y='Load Resistance (Ohms)', z='Power (Watts)',
                          color='Current (A)', labels={'Load Resistance (Ohms)': 'Load Resistance'},
                          title='Power Dissipation in Battery Circuit',
                          color_continuous_scale='Viridis')

# Mathematical expression and equation solving using SymPy
V, I, R = Symbol('V'), Symbol('I'), Symbol('R')
equation = Eq(V, I * R)
current_equation = equation.subs({V: 10.0, R: 0.5})
current_solution = solve(current_equation, I)[0]

print(f'Current (I) = {current_solution:.2f} A')
print(f'Power Dissipation (P) = {current_solution**2 * 0.5:.2f} W')

# Show the Plotly plots
fig_battery.show()
fig_power.show()
