import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

# Matplotlib Visualization
x_vals = np.linspace(0, 2*np.pi, 100)
y_vals = np.sin(x_vals)
plt.plot(x_vals, y_vals, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Plot of sin(x)')
plt.legend()
plt.show()

# Plotly Visualization
fig = px.line(x=x_vals, y=y_vals, title="Plot of sin(x)")
fig.show()
