# pip install numpy matplotlib pandas plotly

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def twin_prime_conjecture(limit):
    multiples_of_6 = np.arange(6, limit+1, 6)
    twin_primes = []

    for n in multiples_of_6:
        if is_prime(n - 1) and is_prime(n + 1):
            twin_primes.append((n - 1, n + 1))

    return twin_primes

limit = 200  # Adjust the limit as per your requirement
twin_primes = twin_prime_conjecture(limit)

# Create a Pandas DataFrame for twin prime pairs
df = pd.DataFrame(twin_primes, columns=['n-1', 'n+1'])

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(df, x='n-1', y='n+1', z=np.zeros(len(df)), color=np.arange(len(df)),
                    opacity=0.7, size_max=7, hover_name=np.arange(len(df)))

# Add connecting lines between twin prime pairs
for pair in twin_primes:
    fig.add_trace(go.Scatter3d(x=[pair[0], pair[1]], y=[pair[1], pair[0]], z=[0, 0], mode='lines',
                               line=dict(color='blue', width=2)))

fig.update_layout(scene=dict(xaxis_title='n-1', yaxis_title='n+1', zaxis_title=''),
                  title=f'Twin Prime Conjecture (Limit: {limit})')

# Show the interactive plot
fig.show()
