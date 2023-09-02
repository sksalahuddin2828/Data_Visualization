import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Create a DataFrame to store resistance values for different R2 and R3 combinations
R2_values = np.linspace(1, 10, 100)
R3_values = np.linspace(1, 20, 100)
data = []

for R2 in R2_values:
    for R3 in R3_values:
        Rp = 1 / (1/R2 + 1/R3)
        Rtot = R1 + Rp
        data.append([R2, R3, Rp, Rtot])

df = pd.DataFrame(data, columns=['R2 (Ω)', 'R3 (Ω)', 'Rp (Ω)', 'Rtot (Ω)'])

# Scatter plot of R2 and R3 vs. Rtot
fig = px.scatter_3d(df, x='R2 (Ω)', y='R3 (Ω)', z='Rtot (Ω)', color='Rp (Ω)', 
                     title='Total Resistance vs. R2 and R3',
                     labels={'R2 (Ω)': 'R2 (Ω)', 'R3 (Ω)': 'R3 (Ω)', 'Rtot (Ω)': 'Rtot (Ω)', 'Rp (Ω)': 'Rp (Ω)'})

# Customize the plot layout
fig.update_layout(scene=dict(xaxis_title='R2 (Ω)', yaxis_title='R3 (Ω)', zaxis_title='Rtot (Ω)'))
fig.show()
