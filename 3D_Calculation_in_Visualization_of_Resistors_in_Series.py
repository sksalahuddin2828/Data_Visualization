import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import interactive
from IPython.display import display

total_resistance = 0.500e6
first_resistance = 900e3
second_resistance = total_resistance - first_resistance
print("Second Resistance:", second_resistance, "Ω")

# Define symbolic variables
R1, R2 = sp.symbols('R1 R2')
total_resistance_expr = R1 + R2

# Interactive expression display
def display_expression(R1_val, R2_val):
    total = total_resistance_expr.subs({R1: R1_val, R2: R2_val})
    sp.init_printing(use_unicode=True)
    display(sp.Eq(total_resistance_expr, total))

interactive(display_expression, R1_val=(0, 1e6, 10000), R2_val=(0, 1e6, 10000))

# Generate data
resistor_values = np.linspace(0, 1e6, 100)
second_resistor_values = total_resistance - resistor_values
data = {'First Resistor': resistor_values, 'Second Resistor': second_resistor_values, 'Total Resistance': total_resistance}
df = pd.DataFrame(data)

# Create dynamic animation
fig = px.scatter(df, x='First Resistor', y='Second Resistor', animation_frame='Total Resistance',
                 title='Dynamic Animation of Resistors in Series')
fig.update_layout(sliders=[dict(steps=[dict(method='animate', args=([None], {'frame': {'duration': 200, 'redraw': True}, 'mode': 'immediate'}), label=str(round(total, 2))) for total in df['Total Resistance']])])

fig.show()

# Example of a simplified animation, actual implementation may vary
# def mathematical_dance_animation():
#     # Define animation frames and steps
#     frames = 50
#     for i in range(frames):
#         plt.cla()
#         # Generate animation frames here
#         plt.plot([0, 1], [0, 1])  # Placeholder for animation content
#         plt.title("Mathematical Dance Animation")
#         plt.xlabel("X-axis")
#         plt.ylabel("Y-axis")
#         plt.xlim(0, 1)
#         plt.ylim(0, 1)
#         plt.pause(0.1)  # Adjust pause duration for animation speed

# mathematical_dance_animation()
