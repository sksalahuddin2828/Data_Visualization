import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sympy as sp

# Given values
Pave = 100e6  # 100 MW in watts
Vrms_values = np.linspace(100e3, 1000e3, 10)  # Voltage values from 100 kV to 1 MV
R = 1.0       # Resistance in ohms

# Calculate current, power dissipation, and percentage loss
Irms_values = Pave / Vrms_values
P_dissipated_values = Irms_values**2 * R
percentage_loss_values = (P_dissipated_values / Pave) * 100

# Create a DataFrame for visualization
df = pd.DataFrame({'Voltage (kV)': Vrms_values / 1e3,  # Convert to kV
                   'Current (A)': Irms_values,
                   'Power Dissipated (kW)': P_dissipated_values / 1e3,  # Convert to kW
                   'Percentage Loss (%)': percentage_loss_values})

# Create animated 3D surface plot
fig = make_subplots(rows=1, cols=2,
                    specs=[[{'type': 'surface'}, {'type': 'surface'}]])

# Create data points for the plot
current_values = np.linspace(100, 1000, 10)
voltage_values = np.linspace(100, 1000, 10)
current_values, voltage_values = np.meshgrid(current_values, voltage_values)
power_loss = (current_values**2 * R) / (current_values * voltage_values)

# Create 3D surface plot for Power Loss
fig.add_trace(go.Surface(z=power_loss, x=current_values, y=voltage_values),
              row=1, col=1)
fig.update_layout(scene=dict(xaxis_title='Current (A)', yaxis_title='Voltage (V)', zaxis_title='Power Loss (W)'),
                  title='Power Loss in Transmission Lines')

# Create a mathematical expression
I, V = sp.symbols('I V')
expression = sp.Eq(I * V, Pave)
expression_text = f'{sp.latex(expression.lhs)} = {sp.latex(expression.rhs)}'

# Create 3D surface plot for Power Dissipation Percentage
fig.add_trace(go.Surface(z=percentage_loss_values.reshape((-1, 1)), x=current_values, y=Vrms_values / 1e3),
              row=1, col=2)
fig.update_layout(scene=dict(xaxis_title='Current (A)', yaxis_title='Voltage (kV)', zaxis_title='% Power Loss'),
                  title='Percentage Power Loss in Transmission Lines')

# Add annotation with mathematical expression
fig.add_annotation(text=expression_text, xref='paper', yref='paper',
                   x=0.9, y=0.15, showarrow=False)

# Create frames for animation
frames = [go.Frame(data=[go.Surface(z=(c**2 * R) / (c * voltage_values))],
                   name=f'Power Loss at Current = {c} A')
          for c in current_values[0]]

# Update animation frames
fig.frames = frames

# Set layout for animation
fig.update_layout(updatemenus=[dict(type='buttons',
                                    showactive=False,
                                    buttons=[dict(label='Play',
                                                  method='animate',
                                                  args=[None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True, transition=dict(duration=0))]),
                                             dict(label='Pause',
                                                  method='animate',
                                                  args=[[None], dict(frame=dict(duration=0, redraw=False), mode='immediate', transition=dict(duration=0))])])])

# Show the plot
fig.show()
