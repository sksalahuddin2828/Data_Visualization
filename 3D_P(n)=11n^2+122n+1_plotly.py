import plotly.graph_objects as go

def P(n):
    return 11*n**2 + 122*n + 1

def prove_divisibility_by_133(n):
    for i in range(1, n+1):
        if P(i) % 133 != 0:
            return False
    return True

# Generate data for visualization
n_values = list(range(1, 21))
P_values = [P(n) for n in n_values]

# Create a 3D scatter plot
fig = go.Figure(data=[
    go.Scatter3d(x=n_values, y=P_values, z=[133]*len(n_values), mode='markers', marker=dict(size=8, color='blue'), name='P(n)'),
    go.Scatter3d(x=n_values, y=[133]*len(n_values), z=P_values, mode='lines', line=dict(color='red'), name='y = 133')
])

# Set axis labels and title
fig.update_layout(scene=dict(xaxis_title='n', yaxis_title='P(n)', zaxis_title='133'),
                  title='P(n) = 11n^2 + 122n + 1',
                  showlegend=True)

# Show the plot
fig.show()

# Prove for n=20
n = 20
if prove_divisibility_by_133(n):
    print(f"P(n) is divisible by 133 for n = {n}")
else:
    print(f"P(n) is not divisible by 133 for n = {n}")
