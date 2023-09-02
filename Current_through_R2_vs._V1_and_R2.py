import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Define symbolic variables for the calculations
V, V1, R2, I2 = sp.symbols('V V1 R2 I2')

# Calculate voltage applied to R2 (Vp) symbolically
Vp = V - V1

# Calculate current through R2 (I2) symbolically using Ohm's law
I2_expression = Vp / R2

# Convert the symbolic expression to LaTeX
math_expression_latex = sp.latex(I2_expression)

# Create a DataFrame with V1 and R2 values
V1_values = np.linspace(0, 5, 100)
R2_values = np.linspace(1, 10, 100)
V1_values, R2_values = np.meshgrid(V1_values, R2_values)

# Calculate I2 using the Python function
calculate_I2 = sp.lambdify((V, V1, R2), I2_expression, 'numpy')
I2_values = calculate_I2(V, V1_values, R2_values)

df = pd.DataFrame({
    'V1': V1_values.flatten(),
    'R2': R2_values.flatten(),
    'I2': I2_values.flatten()
})

# Create an interactive 3D surface plot
fig = px.scatter_3d(df, x='V1', y='R2', z='I2',
                     labels={'I2': 'Current (A)'},
                     title='Current through R2 vs. V1 and R2')

fig.update_traces(marker=dict(size=5),
                  selector=dict(mode='markers+text'),
                  textfont_size=12,
                  textposition='top right')

# Save the LaTeX expression as an image file
fig, ax = plt.subplots(figsize=(2, 1))
ax.text(0.5, 0.5, math_expression_latex, size=12)
ax.axis('off')
fig.savefig('math_expression.png', dpi=300, bbox_inches='tight')

# Embed the image in the Plotly figure
with open('math_expression.png', 'rb') as img_file:
    image_data = base64.b64encode(img_file.read()).decode()
    
fig_with_image = go.Figure()

fig_with_image.add_trace(go.Scatter(x=[2], y=[8], text=['<img src="data:image/png;base64,{}">'.format(image_data)], mode='text'))

# Show the plot
fig_with_image.show()
