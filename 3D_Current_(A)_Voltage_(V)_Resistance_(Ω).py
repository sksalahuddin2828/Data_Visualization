import pandas as pd
import numpy as np
import sympy as sp

# Given data
resistance = 4000  # Ω

# Create a DataFrame with voltage values
voltages = np.linspace(0, 120, 100)  # Example voltage range

# Calculate current for each voltage using SymPy
voltage_sym = sp.Symbol('voltage')
current_sym = voltage_sym / resistance
current_values = [current_sym.subs(voltage_sym, v) for v in voltages]

# Create a DataFrame
data = {'Voltage': voltages, 'Current': current_values}
df = pd.DataFrame(data)

import plotly.graph_objects as go

# Create a meshgrid for voltage and resistance
voltages_3d = np.linspace(0, 120, 50)
resistances_3d = np.linspace(1000, 8000, 50)
V, R = np.meshgrid(voltages_3d, resistances_3d)

# Calculate current for the meshgrid using NumPy
I = V / R

# Create a 3D surface plot
fig_3d = go.Figure(data=[go.Surface(z=I, x=V, y=R)])
fig_3d.update_layout(title='Current (A) vs Voltage (V) and Resistance (Ω)',
                     scene=dict(xaxis_title='Voltage (V)', yaxis_title='Resistance (Ω)', zaxis_title='Current (A)'))

# Show the 3D plot
fig_3d.show()
