import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.graph_objects as go

# Generate some temperature data for illustration
np.random.seed(42)
num_samples = 100
temperature_data = np.random.randint(-10, 40, num_samples)  # Random temperatures between -10°C and 40°C

# Create a DataFrame to store the temperature data
data_df = pd.DataFrame({"Temperature (°C)": temperature_data})

# Create a dynamic histogram with animated bars to show the distribution of temperatures
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Temperatures (°C)")

def update_hist(num, data):
    ax.clear()
    bins = np.arange(-15, 45, 5)
    ax.hist(data["Temperature (°C)"][:num], bins=bins, color='skyblue', edgecolor='black')
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Temperatures (°C)")
    ax.grid(True)

ani = animation.FuncAnimation(fig, update_hist, fargs=(data_df,), frames=num_samples, interval=100, repeat=False)
plt.close()

# Create an interactive scatter plot with tooltips to show the equal intervals property
fig = go.Figure()
fig.add_trace(go.Scatter(x=list(range(len(data_df))), y=data_df["Temperature (°C)"], mode='markers', marker=dict(color='orange')))
fig.update_layout(title="Scatter Plot of Temperatures (°C)", xaxis_title="Index", yaxis_title="Temperature (°C)")

# Add tooltips to the scatter plot
fig.update_traces(hoverinfo="text", text=list(data_df["Temperature (°C)"].values))

# Show the interactive plot using plotly
fig.show()

# Add a mathematical dance explanation to the project presentation
print("Imagine the temperature data dancing across the centigrade scale!")
print("The histogram showcases the distribution of temperatures, gracefully forming a bell curve.")
print("Meanwhile, the scatter plot dances with equal intervals, elegantly aligning each temperature point.")
print("In the world of mathematics, these properties make the centigrade scale a mesmerizing dance of data!")
