import plotly.graph_objects as go

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

# Prove using mathematical induction
def prove_sum_of_squares(n):
    for i in range(1, n+1):
        if sum_of_squares(i) != i*(i+1)*(2*i+1)//6:
            return False
    return True

# Generate data for visualization
n_values = list(range(1, 11))
sum_squares_values = [sum_of_squares(n) for n in n_values]
expected_values = [n*(n+1)*(2*n+1)//6 for n in n_values]

# Create a 3D scatter plot
fig = go.Figure(data=[
    go.Scatter3d(x=n_values, y=sum_squares_values, z=expected_values, mode='markers', marker=dict(size=8, color='blue'), name='Sum of Squares')
])

# Add a line plot to connect the points for visualization
fig.add_trace(go.Scatter3d(x=n_values, y=sum_squares_values, z=expected_values, mode='lines', line=dict(color='red'), name='n*(n+1)*(2n+1)//6'))

# Set axis labels and title
fig.update_layout(scene=dict(xaxis_title='n', yaxis_title='Sum of Squares', zaxis_title='n*(n+1)*(2n+1)//6'),
                  title='Sum of Squares using Mathematical Induction',
                  showlegend=True)

# Show the plot
fig.show()

# Prove for n=10
n = 10
if prove_sum_of_squares(n):
    print(f"Sum of squares is true for n = {n}")
else:
    print(f"Sum of squares is not true for n = {n}")
