import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Define the symbolic variables
x, a = sp.symbols('x a')

# Define the integrand
integral_expr = a**2 - x**2

# Solve the integral symbolically
integral_result_positive = sp.integrate(sp.sqrt(integral_expr), x)
integral_result_negative = -sp.integrate(sp.sqrt(integral_expr), x)

# Convert the symbolic expressions to lambdified functions
integral_func_positive = sp.lambdify((x, a), integral_result_positive, 'numpy')
integral_func_negative = sp.lambdify((x, a), integral_result_negative, 'numpy')

# Generate x and a values for plotting
x_vals = np.linspace(-10, 10, 400)
a_vals = np.linspace(0.1, 5, 100)

# Create meshgrids for 3D plotting
X, A = np.meshgrid(x_vals, a_vals)

# Calculate integral values using the lambdified functions
integral_vals_positive = integral_func_positive(X, A)
integral_vals_negative = integral_func_negative(X, A)

# Extract real and imaginary components for plotting
integral_vals_positive_real = np.real(integral_vals_positive)
integral_vals_positive_imag = np.imag(integral_vals_positive)
integral_vals_negative_real = np.real(integral_vals_negative)
integral_vals_negative_imag = np.imag(integral_vals_negative)

# Create DataFrames for the real and imaginary components of the positive branch
integral_df_positive_real = pd.DataFrame({'x': np.tile(x_vals, len(a_vals)),
                                          'a': np.repeat(a_vals, len(x_vals)),
                                          'Integral Real': integral_vals_positive_real.flatten()})

integral_df_positive_imag = pd.DataFrame({'x': np.tile(x_vals, len(a_vals)),
                                          'a': np.repeat(a_vals, len(x_vals)),
                                          'Integral Imaginary': integral_vals_positive_imag.flatten()})


# Create 3D surface plots using Plotly Graph Objects for real and imaginary components
fig_3d_positive_real = go.Figure(data=[go.Surface(z=integral_vals_positive_real, x=x_vals, y=a_vals)])
fig_3d_positive_real.update_layout(scene=dict(zaxis_title='Real Integral Value'),
                                   title_text="Positive Branch: Unveiling the Real Integral Landscape",
                                   title_font_size=24, title_x=0.5)
fig_3d_positive_real.show()

fig_3d_positive_imag = go.Figure(data=[go.Surface(z=integral_vals_positive_imag, x=x_vals, y=a_vals)])
fig_3d_positive_imag.update_layout(scene=dict(zaxis_title='Imaginary Integral Value'),
                                   title_text="Positive Branch: Unveiling the Imaginary Integral Landscape",
                                   title_font_size=24, title_x=0.5)
fig_3d_positive_imag.show()

# Complex Numbers Dance and Narration
narrative_complex = """
Now, let's embark on a journey into the realm of complex numbers. The integral expression ∫(a^2 - x^2)^(1/2) dx
transforms once more, embracing the dance of imaginary and real parts. Complex numbers weave a fascinating story,
where reality and imagination collide.

The integration process, guided by the power of complex numbers, breathes life into a new visual representation.
Imagine 'a' and 'x' as the architects of a multidimensional dance floor, and the complex integral expression as
the guiding melody. As the dance unfolds, watch as the real and imaginary components merge to create a harmonious
and vibrant rhythm.

The Plotly line plots and 3D surface plots presented below encapsulate the essence of this dance. Observe how
complex numbers paint a rich tapestry of colors and patterns, each representing a unique combination of 'a' and 'x'.
The intricate designs tell a tale of mathematical elegance, where imagination transcends the boundaries of reality.

As we explore the beauty of complex integration, remember that these numbers aren't just mathematical entities.
They are the conduits through which we interpret the universe's hidden patterns, a bridge between the tangible
and the abstract. Immerse yourself in the realm of complex numbers, and experience the harmony that emerges from
the interplay between real and imaginary worlds.
"""

print(narrative_complex)
