import numpy as np
import pandas as pd
import plotly.graph_objects as go

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

def generate_random_data():
    data = {
        'X': np.random.randint(1, 100, 100),
        'Y': np.random.randint(1, 100, 100),
        'Z': np.random.randint(1, 100, 100),
        'Value': 200 + np.random.randn(100)
    }
    return pd.DataFrame(data)

def visualize_3d_scatter(df):
    fig = go.Figure(data=[go.Scatter3d(
        x=df['X'],
        y=df['Y'],
        z=df['Z'],
        mode='markers',
        marker=dict(
            size=6,
            color=df['Value'],
            colorscale='Viridis',
            opacity=0.8
        )
    )])

    fig.update_layout(
        title='Creative 3D Scatter Plot',
        scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
        width=800, height=800,
        showlegend=False
    )

    fig.show()

def main():
    data_df = generate_random_data()
    visualize_3d_scatter(data_df)

if __name__ == "__main__":
    main()
