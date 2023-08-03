import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Sets A, B, and C
A = set([1, 2, 3, 4, 5])
B = set([4, 5, 6, 7, 8])
C = set([6, 7, 8, 9, 10])

# Calculate n(A), n(B), n(C)
n_A = len(A)
n_B = len(B)
n_C = len(C)

# Calculate n(A ∩ B), n(A ∩ C), n(B ∩ C), n(A ∩ B ∩ C)
n_A_int_B = len(A.intersection(B))
n_A_int_C = len(A.intersection(C))
n_B_int_C = len(B.intersection(C))
n_A_int_B_int_C = len(A.intersection(B).intersection(C))

# Calculate n(A ∪ B ∪ C) using inclusion-exclusion principle
n_A_union_B_union_C = n_A + n_B + n_C - n_A_int_B - n_A_int_C - n_B_int_C + n_A_int_B_int_C

# Create DataFrame to store the sets and intersection points
df = pd.DataFrame(columns=['x', 'y', 'z', 'label'])

# Populate DataFrame with points for each set
for x in A:
    df = df.append({'x': x, 'y': 0, 'z': 0, 'label': 'Set A'}, ignore_index=True)
for y in B:
    df = df.append({'x': 0, 'y': y, 'z': 0, 'label': 'Set B'}, ignore_index=True)
for z in C:
    df = df.append({'x': 0, 'y': 0, 'z': z, 'label': 'Set C'}, ignore_index=True)

# Calculate the intersection points
intersection_points = np.array([[x, y, z] for x in A.intersection(B).intersection(C)])

# Check if there are any intersection points before creating DataFrame
if len(intersection_points) > 0:
    intersection_df = pd.DataFrame(intersection_points, columns=['x', 'y', 'z'])
    intersection_df['label'] = 'Intersection'
    # Concatenate the DataFrames
    df = pd.concat([df, intersection_df], ignore_index=True)

# 3D Plotting with Plotly
fig = go.Figure()

# Scatter plot for each set and intersection points
for label in df['label'].unique():
    points = df[df['label'] == label]
    fig.add_trace(go.Scatter3d(x=points['x'], y=points['y'], z=points['z'],
                               mode='markers', marker=dict(size=6), name=label))

fig.update_layout(title='Inclusion-Exclusion Principle Visualization',
                  scene=dict(xaxis_title='X-axis', yaxis_title='Y-axis', zaxis_title='Z-axis'),
                  margin=dict(l=0, r=0, b=0, t=50))

fig.show()
