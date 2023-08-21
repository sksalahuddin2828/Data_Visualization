import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
import torch
import scipy.integrate as spi

x, a = sp.symbols('x a')
integral_expr = a**2 - x**2
integral_result_positive = sp.integrate(sp.sqrt(integral_expr), x)
integral_result_negative = -sp.integrate(sp.sqrt(integral_expr), x)

x_vals = np.linspace(-10, 10, 400)
integral_vals_positive = np.array([integral_result_positive.subs(x, val).evalf() for val in x_vals])
integral_vals_negative = np.array([integral_result_negative.subs(x, val).evalf() for val in x_vals])

integral_df = pd.DataFrame({'x': x_vals,
                            'Integral (Positive)': integral_vals_positive,
                            'Integral (Negative)': integral_vals_negative})

fig = px.line(integral_df, x='x', title='Symbolic Integral Visualization')
fig.update_layout(xaxis_title="x", yaxis_title="Integral Value")
fig.update_traces(line=dict(width=2))
fig.update_layout(title_text="Dancing with Integrals",
                  title_font_size=24, title_x=0.5)
fig.show()

narrative = """
Welcome to the waltz of integration! Imagine a dance where numbers come alive, swirling and twirling
with elegance. The integral ∫(a^2 - x^2)^(1/2) dx sweeps across the stage, revealing a mesmerizing
choreography of both positive and negative square roots.

As we take each step, the symphony of mathematics unfolds. The stage is set with 'a' and 'x' as the
lead dancers. The integral expression embodies their dance, capturing the essence of the interplay
between algebra and geometry.

Positive and negative branches intertwine, showcasing the full spectrum of possibilities. Like a
dual-sided mirror, the integral expression reflects both sides of the story, where 'a' takes center
stage, and 'x' gracefully follows. This dance transcends mere numbers; it speaks the language of
equations and evokes a sense of wonder in the heart of the observer.

The plot below is a canvas of motion, capturing the graceful journey of the integral. As you explore,
remember that every curve, every peak, and every dip tells a story of integration. It's a story of
mathematical beauty that comes to life in every step of the dance.
"""

print(narrative)
