import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Constants
R_g = 25.0  # Galvanometer resistance in ohms
I_g = 50e-6  # Galvanometer sensitivity in A

# Calculate shunt resistance as a function of I_full and I_g
def calculate_shunt_resistance(I_full, I_g):
    return R_g / (I_full / I_g - 1)

# Create a Pandas DataFrame for data visualization
I_full_values = np.linspace(0.01, 20, 100)  # Full-scale current values
I_g_values = np.linspace(1e-6, 200e-6, 100)  # Galvanometer sensitivity values

data = {'Full-scale Current (I_full) [A]': [], 'Galvanometer Sensitivity (I_g) [A]': [], 'Shunt Resistance (R_s) [Ω]': []}
for I_full_val in I_full_values:
    for I_g_val in I_g_values:
        R_s_calculated = calculate_shunt_resistance(I_full_val, I_g_val)
        data['Full-scale Current (I_full) [A]'].append(I_full_val)
        data['Galvanometer Sensitivity (I_g) [A]'].append(I_g_val)
        data['Shunt Resistance (R_s) [Ω]'].append(R_s_calculated)

df = pd.DataFrame(data)

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(df, x='Full-scale Current (I_full) [A]', y='Galvanometer Sensitivity (I_g) [A]',
                    z='Shunt Resistance (R_s) [Ω]', color='Shunt Resistance (R_s) [Ω]',
                    labels={'Full-scale Current (I_full) [A]': 'Full-scale Current (I_full) [A]',
                            'Galvanometer Sensitivity (I_g) [A]': 'Galvanometer Sensitivity (I_g) [A]',
                            'Shunt Resistance (R_s) [Ω]': 'Shunt Resistance (R_s) [Ω]'},
                    title='Interactive 3D Plot: Shunt Resistance as a Function of I_full and I_g')

# Add a theoretical curve representing the ideal shunt resistance
I_full_theoretical = np.linspace(0.01, 20, 100)
R_s_theoretical = R_g / (I_full_theoretical / I_g - 1)
fig.add_trace(go.Scatter3d(x=I_full_theoretical, y=np.full(100, I_g), z=R_s_theoretical,
                           mode='lines', name='Theoretical Curve', line=dict(color='red')))

# Add animation
animation_frames = []
frame_step = len(df) // 10  # Adjust the step size for animation
for i in range(0, len(df), frame_step):
    frame = go.Frame(
        data=[go.Scatter3d(x=df['Full-scale Current (I_full) [A]'][i:i+frame_step],
                            y=df['Galvanometer Sensitivity (I_g) [A]'][i:i+frame_step],
                            z=df['Shunt Resistance (R_s) [Ω]'][i:i+frame_step],
                            marker=dict(size=3),
                            name=f'Frame {i}')],
    )
    animation_frames.append(frame)

fig.update(frames=animation_frames)

# Customize the layout
fig.update_layout(scene=dict(aspectmode='cube'),
                  scene_camera_eye=dict(x=1.2, y=1.2, z=0.8))

# Show the interactive plot
fig.show()
