import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

# Matplotlib Visualization
x_vals = np.linspace(-2*np.pi, 2*np.pi, 400)
y_vals = np.log(np.abs(1/np.cos(x_vals)))

plt.plot(x_vals, y_vals, label='ln|sec(x)|')
plt.xlabel('x')
plt.ylabel('ln|sec(x)|')
plt.title('Plot of ln|sec(x)|')
plt.legend()
plt.show()

# Plotly Visualization
fig = px.line(x=x_vals, y=y_vals, title="Plot of ln|sec(x)|")
fig.show()
