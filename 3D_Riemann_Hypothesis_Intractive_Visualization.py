import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import sympy as sp

def zeta(s):
    return np.sum(1 / np.power(np.arange(1, 10000), s))

def zeta_critical_line(t):
    s = 0.5 + 1j * t
    return zeta(s).real

t_values = np.linspace(0, 81702130.19, 500)
zeta_values = [zeta_critical_line(t) for t in t_values]

plt.figure(figsize=(12, 6))
plt.plot(t_values, zeta_values, label='Riemann Zeta Function on Critical Line', color='blue')
plt.xlabel('t')
plt.ylabel('zeta(1/2 + it)')
plt.title('Riemann Zeta Function on the Critical Line')
plt.axhline(0, color='black', linewidth=0.5)  # Add a horizontal line at y=0 for better visualization
plt.legend()
plt.grid(True)
plt.show()

def zeta_modulus(t):
    s = 0.5 + 1j * t
    return abs(zeta(s))

modulus_values = [zeta_modulus(t) for t in t_values]

plt.figure(figsize=(12, 6))
plt.plot(t_values, modulus_values, label='Modulus of Riemann Zeta Function on Critical Line', color='purple')
plt.xlabel('t')
plt.ylabel('|zeta(1/2 + it)|')
plt.title('Modulus of the Riemann Zeta Function on the Critical Line')
plt.legend()
plt.grid(True)
plt.show()

# Step 8: Define the Riemann Xi Function
def xi(s):
    return 0.5 * s * (s - 1) * np.pi ** (-s / 2) * sp.gamma(s / 2) * zeta(s)

# Step 9: Define the Riemann Xi Function on the Critical Line
def xi_critical_line(t):
    s = 0.5 + 1j * t
    return np.abs(xi(s))  # Use np.abs to compute the modulus (absolute value)

# Step 10: Visualize the Riemann Xi Function on the Critical Line
xi_values = [xi_critical_line(t) for t in t_values]

plt.figure(figsize=(12, 6))
plt.plot(t_values, xi_values, label='Riemann Xi Function on Critical Line', color='green')
plt.xlabel('t')
plt.ylabel('|xi(1/2 + it)|')
plt.title('Riemann Xi Function on the Critical Line')
plt.axhline(0, color='black', linewidth=0.5)  # Add a horizontal line at y=0 for better visualization
plt.legend()
plt.grid(True)
plt.show()

def xi_modulus(t):
    s = 0.5 + 1j * t
    return abs(xi(s))

xi_modulus_values = [xi_modulus(t) for t in t_values]

plt.figure(figsize=(12, 6))
plt.plot(t_values, xi_modulus_values, label='Modulus of Riemann Xi Function on Critical Line', color='orange')
plt.xlabel('t')
plt.ylabel('|xi(1/2 + it)|')
plt.title('Modulus of the Riemann Xi Function on the Critical Line')
plt.legend()
plt.grid(True)
plt.show()

# Step 11: Visualize the Phase of the Riemann Zeta Function on the Critical Line
zeta_phase_values = [np.angle(complex(zeta_critical_line(t))) for t in t_values]  # Convert to complex numbers

plt.figure(figsize=(12, 6))
plt.plot(t_values, zeta_phase_values, label='Phase of Riemann Zeta Function on Critical Line', color='yellow')
plt.xlabel('t')
plt.ylabel('arg(zeta(1/2 + it))')
plt.title('Phase of the Riemann Zeta Function on the Critical Line')
plt.legend()
plt.grid(True)
plt.show()

# Step 12: Visualize the Phase of the Riemann Xi Function on the Critical Line
xi_phase_values = [np.angle(complex(xi_critical_line(t))) for t in t_values]  # Convert to complex numbers

plt.figure(figsize=(12, 6))
plt.plot(t_values, xi_phase_values, label='Phase of Riemann Xi Function on Critical Line', color='cyan')
plt.xlabel('t')
plt.ylabel('arg(xi(1/2 + it))')
plt.title('Phase of the Riemann Xi Function on the Critical Line')
plt.legend()
plt.grid(True)
plt.show()

fig = go.Figure()

# Convert the data to standard Python lists
t_values_list = t_values.tolist()
zeta_values_list = [float(val) for val in zeta_values]
modulus_values_list = [float(val) for val in modulus_values]
xi_values_list = [float(val) for val in xi_values]
xi_modulus_values_list = [float(val) for val in xi_modulus_values]
zeta_phase_values_list = [float(val) for val in zeta_phase_values]
xi_phase_values_list = [float(val) for val in xi_phase_values]

fig = go.Figure()

# Add the Riemann zeta function on the critical line
fig.add_trace(go.Scatter(x=t_values_list, y=zeta_values_list, mode='lines', name='Riemann Zeta Function on Critical Line (Real)',
                         line=dict(color='blue', width=2)))

# Add the modulus of the Riemann zeta function on the critical line
fig.add_trace(go.Scatter(x=t_values_list, y=modulus_values_list, mode='lines', name='Modulus of Riemann Zeta Function (Real)',
                         line=dict(color='purple', width=2)))

# Add the Riemann Xi function on the critical line
fig.add_trace(go.Scatter(x=t_values_list, y=xi_values_list, mode='lines', name='Riemann Xi Function on Critical Line (Real)',
                         line=dict(color='green', width=2)))

# Add the modulus of the Riemann Xi function on the critical line
fig.add_trace(go.Scatter(x=t_values_list, y=xi_modulus_values_list, mode='lines', name='Modulus of Riemann Xi Function (Real)',
                         line=dict(color='orange', width=2)))

# Add the phase of the Riemann Zeta function on the critical line
fig.add_trace(go.Scatter(x=t_values_list, y=zeta_phase_values_list, mode='lines', name='Phase of Riemann Zeta Function',
                         line=dict(color='yellow', width=2)))

# Add the phase of the Riemann Xi function on the critical line
fig.add_trace(go.Scatter(x=t_values_list, y=xi_phase_values_list, mode='lines', name='Phase of Riemann Xi Function',
                         line=dict(color='cyan', width=2)))

fig.update_layout(title='Riemann Hypothesis - Interactive Visualization',
                  xaxis_title='t',
                  legend=dict(x=0.8, y=0.1),
                  showlegend=True,
                  template='plotly_dark',  # Use a dark theme for an attractive look
                  width=1000, height=600,  # Adjust size for better display
                  margin=dict(l=50, r=50, t=80, b=50),  # Add margins for better spacing
                  hovermode='closest')  # Enable closest data point hover for better interactivity

fig.show()
