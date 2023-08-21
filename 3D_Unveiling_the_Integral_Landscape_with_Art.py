import numpy as np
import pandas as pd
import sympy as sp
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Define the symbolic variable
x, a = sp.symbols('x a')

# Define the integrand
integral_expr = sp.sqrt(a**2 + x**2)

# Solve the integral symbolically
integral_result = sp.integrate(integral_expr, x)

# Create a function from the symbolic expression
integral_func = sp.lambdify((x, a), integral_result, 'numpy')

# Generate x values for plotting
x_vals = np.linspace(-10, 10, 400)

# Generate a values for plotting
a_vals = np.linspace(0.1, 5, 100)

# Create a meshgrid for 3D plotting
X, A = np.meshgrid(x_vals, a_vals)

# Calculate the integral values using the function
integral_vals = integral_func(X, A)

# Reshape the integral values for DataFrame
integral_vals_flat = integral_vals.flatten()

# Create a DataFrame for the plotly line plot
integral_df = pd.DataFrame({'x': np.tile(x_vals, len(a_vals)),
                            'a': np.repeat(a_vals, len(x_vals)),
                            'Integral': integral_vals_flat})

# Create an interactive line plot using Plotly
fig = px.line(integral_df, x='x', y='Integral', title='Integral Plot',
              labels={'x': 'x', 'Integral': 'Integral Value'})
fig.update_layout(xaxis_title="x", yaxis_title="Integral Value")
fig.update_traces(line=dict(color='blue'))
fig.update_layout(title_text="Dancing Through Integration",
                  title_font_size=24, title_x=0.5)
fig.show()

# Mathematical dance and narration
narrative = """
As the sun sets, mathematical elegance awakens. The dance of integration unfolds, where
each step follows the beat of the square root of the sum of 'a' squared and 'x' squared.
Behold, the integral expression reveals its secrets, painting the canvas of numbers with
the hues of understanding and wonder. The journey through this landscape transcends
the ordinary, guiding us through the pathways of mathematical harmony.

Imagine the intersection of theoretical brilliance and artistic expression. In the realm
of calculus, the integral symbolizes the accumulation of infinitesimal contributions,
forming a bridge between geometry and algebra. As 'a' and 'x' converge, the dance of
integration imparts a profound message - that in the union of disparate elements, beauty
and knowledge intertwine.

Let's animate this mathematical journey! Watch as the integral curve evolves, illustrating
how the integration process builds the elegant curve before your eyes. With each frame,
witness the harmony of numbers and their transformation into the visual masterpiece.

Behold the Integral Landscape: a world where 'a' and 'x' intertwine to create a stunning
topography of integral values. As you explore the peaks and valleys of this landscape, let
your mind wander through the tapestry of mathematical possibilities. The axis of 'a' leads
you through different levels of abstraction, while the 'x' axis reveals the symphony of
integrated values that emerge from the dance of mathematics.

In this realm, numbers transcend their numeric essence, taking on the role of both form and
function. The 3D surface plot, a masterpiece of modern visualization, presents this union
in its full glory. Every point on the surface represents a unique perspective into the
mathematical universe, a universe waiting to be explored.

Witness the convergence of art and mathematics as you gaze upon this creation. The colors,
lines, and contours tell a story of equations, relationships, and connections. A story that
speaks not only to the mind but also to the soul. A story of a journey through integration,
where the dance of numbers transforms into a symphony of understanding.
"""

print(narrative)

# Create a 3D surface plot using Plotly Graph Objects
fig_3d = go.Figure(data=[go.Surface(z=integral_vals, x=x_vals, y=a_vals)])
fig_3d.update_layout(scene=dict(zaxis_title='Integral Value'),
                     title_text="Unveiling the Integral Landscape",
                     title_font_size=24, title_x=0.5)
fig_3d.show()

# Display the 3D Matplotlib plot for a dynamic visual experience
fig_3d_matplotlib = plt.figure()
ax = fig_3d_matplotlib.add_subplot(111, projection='3d')
ax.plot_surface(X, A, integral_vals, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('a')
ax.set_zlabel('Integral')
ax.set_title('Elevating Integration to Art')
plt.show()
