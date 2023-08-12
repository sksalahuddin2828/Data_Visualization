import numpy as np
import pandas as pd
import plotly.express as px

# Matrix A
A = np.array([[4, 3], [2, 1]])

# Convert matrix to pandas DataFrame
df_A = pd.DataFrame(A, columns=['Column 1', 'Column 2'])

# Create heatmap using plotly
fig = px.imshow(df_A, labels=dict(color="Matrix A"), title="Heatmap of Matrix A")
fig.show()

# Matrix C
C = np.array([[4, 8], [2, 2]])

# Convert matrix to pandas DataFrame
df_C = pd.DataFrame(C, columns=['Column 1', 'Column 2'])

# Create heatmap using plotly
fig = px.imshow(df_C, labels=dict(color="Matrix C"), title="Heatmap of Matrix C")
fig.show()

# Matrix A
A = np.array([[1, -9, -3], [4, -6, -2], [3, 5, -2]])

# Convert matrix to pandas DataFrame
df_A = pd.DataFrame(A, columns=['Column 1', 'Column 2', 'Column 3'])

# Create heatmap using plotly
fig = px.imshow(df_A, labels=dict(color="Matrix A"), title="Heatmap of Matrix A")
fig.show()

# Matrix B after the row transformation
B = np.array([[1, 1, 1], [2, 3, 4], [0, 1, 2]])

# Convert matrix to pandas DataFrame
df_B = pd.DataFrame(B, columns=['Column 1', 'Column 2', 'Column 3'])

# Create heatmap using plotly
fig = px.imshow(df_B, labels=dict(color="Matrix B"), title="Heatmap of Matrix B")
fig.show()
