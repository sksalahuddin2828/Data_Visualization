import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D

# Define a range of values for sin θ
sin_theta_values = np.linspace(0, 1, 100)
cos_theta_values = np.sqrt(1 - sin_theta_values**2)
sec_theta_values = 1 / np.sqrt(1 - sin_theta_values**2)

# Given value
sin_theta = 1/3

# Calculate sec θ
sec_theta = 1 / sp.sqrt(1 - sin_theta**2)

sec_theta_val = sec_theta.evalf()  # Evaluate the result

# Create a DataFrame for visualization
data = {'sin_theta': sin_theta_values, 'cos_theta': cos_theta_values, 'sec_theta': sec_theta_values}
df = pd.DataFrame(data)

# Create an interactive scatter plot
scatter_plot = px.scatter_3d(df, x='sin_theta', y='cos_theta', z='sec_theta',
                             title="Trigonometric Relationship",
                             labels={'sin_theta': 'sin θ', 'cos_theta': 'cos θ', 'sec_theta': 'sec θ'})

scatter_plot.update_traces(marker=dict(size=5))  # Adjust marker size
scatter_plot.show()
