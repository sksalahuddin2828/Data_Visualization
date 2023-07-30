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

# Calculate the average temperature on the centigrade scale
avg_temperature = np.mean(temperature_data)

# Create a dynamic histogram with animated bars to show the distribution of temperatures
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Temperatures (°C)")

def update_hist(num, data):
    ax.clear()
    bins = np.arange(-15, 45, 5)
    ax.hist(data["Temperature (°C)"][:num], bins=bins, color='skyblue', edgecolor='black')
    ax.axvline(x=avg_temperature, color='red', linestyle='--', label='Average Temperature')
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Temperatures (°C)")
    ax.legend()
    ax.grid(True)

ani = animation.FuncAnimation(fig, update_hist, fargs=(data_df,), frames=num_samples, interval=100, repeat=False)
plt.close()

# Create an interactive scatter plot with tooltips to show the equal intervals property
fig = go.Figure()
fig.add_trace(go.Scatter(x=list(range(len(data_df))), y=data_df["Temperature (°C)"], mode='markers', marker=dict(color='orange')))
fig.update_layout(title="Scatter Plot of Temperatures (°C)", xaxis_title="Index", yaxis_title="Temperature (°C)")

# Add tooltips to the scatter plot
fig.update_traces(hoverinfo="text", text=list(data_df["Temperature (°C)"].values))

# Create an interactive line chart to explore the temperature data over time
fig.add_trace(go.Scatter(x=list(range(len(data_df))), y=data_df["Temperature (°C)"], mode='lines', line=dict(color='blue'), visible=False))

# Set the length of the `visible` list to the maximum value needed for both traces
visible_list_length = len(data_df) + 2

steps = []
for i in range(len(data_df)):
    step = dict(
        method="update",
        args=[{"visible": [False] * visible_list_length},
              {"title": f"Temperature at Index {i}: {data_df['Temperature (°C)'][i]}°C"}],
    )
    step["args"][0]["visible"][1] = True
    step["args"][0]["visible"][i + 2] = True
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Index: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(sliders=sliders)

# Show the interactive plot using plotly
fig.show()

# Add a mathematical dance explanation to the project presentation
print("Imagine the temperature data dancing across the centigrade scale!")
print("The histogram showcases the distribution of temperatures, gracefully forming a bell curve.")
print(f"The average temperature on the centigrade scale is {avg_temperature:.2f}°C, marked by a red dashed line.")
print("The interactive scatter plot allows you to explore the temperature data at different indices.")
print("Select an index from the slider below the chart to visualize the temperature over time.")
print("In the world of mathematics, these properties and visualizations make the centigrade scale a mesmerizing dance of data!")
