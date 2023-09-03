import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp
import torch
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
import plotly.express as px

V = 12.0  # Voltage
Rp = 0.8041  # Equivalent resistance

I = V / Rp  # Calculate the total current

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define voltage and resistance ranges
V_range = np.linspace(0.1, 20, 100)
Rp_range = np.linspace(0.1, 2, 100)
V, Rp = np.meshgrid(V_range, Rp_range)
I = V / Rp

# Plot the 3D surface
ax.plot_surface(V, Rp, I, cmap='viridis')

# Label axes
ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Resistance (Rp)')
ax.set_zlabel('Current (I)')

plt.title('3D Visualization of Ohm\'s Law')
plt.show()

# Generate some sample data
rng = np.random.default_rng(seed=42)
X = rng.uniform(0.1, 20, 100)
Y = X / 0.8041 + rng.normal(0, 0.5, 100)

# Fit a linear regression model
model = LinearRegression()
model.fit(X.reshape(-1, 1), Y)

# Visualize the linear regression line
plt.scatter(X, Y)
plt.plot(X, model.predict(X.reshape(-1, 1)), color='red')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (I)')
plt.title('Linear Regression of Ohm\'s Law')
plt.show()

# Define symbolic variables
V_symbol, Rp_symbol, I_symbol = sp.symbols('V Rp I')

# Define Ohm's Law equation
Ohms_law_eq = sp.Eq(V_symbol, Rp_symbol * I_symbol)

# Substitute single values for V and Rp
V_value = 12.0
Rp_value = 0.8041
current = sp.solve(Ohms_law_eq.subs({V_symbol: V_value, Rp_symbol: Rp_value}), I_symbol)

def ohms_law(V, Rp):
    return V / Rp

# Fit the curve to your data
params, covariance = curve_fit(ohms_law, X, Y)

# Extract the resistance value (Rp) from the fit
Rp_fit = params[0]

# Visualize the fit
plt.scatter(X, Y)
plt.plot(X, ohms_law(X, Rp_fit), color='red')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (I)')
plt.title('Curve Fit of Ohm\'s Law')
plt.show()

# Create a dataframe with voltage and current data
df = pd.DataFrame({'Voltage (V)': X, 'Current (I)': Y})

# Create an interactive scatter plot
fig = px.scatter(df, x='Voltage (V)', y='Current (I)', trendline='ols', title='Interactive Ohm\'s Law Plot')
fig.show()
