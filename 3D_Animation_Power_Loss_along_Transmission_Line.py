import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display, clear_output
import time

# Sample data for demonstration
voltage = 25000.0  # Example voltage in volts
resistance = 1.00  # Example resistance in ohms

# Calculate current and power loss
current = voltage / resistance
power_loss = resistance * (current ** 2)

# Create a DataFrame for power loss values along the transmission line
distance = np.linspace(0, 1, 100)
loss_values = resistance * (current ** 2) * distance
df = pd.DataFrame({"Distance": distance, "Power Loss": loss_values})

# Display calculations
display(f"Voltage: {voltage} V")
display(f"Resistance: {resistance} Ω")
display(f"Current: {current:.2f} A")
display(f"Power Loss: {power_loss:.2f} W")

# Plotly interactive line plot with equation annotation
fig_line = px.line(df, x="Distance", y="Power Loss", title="Power Loss along Transmission Line")
fig_line.update_xaxes(title="Distance")
fig_line.update_yaxes(title="Power Loss (W)")

# Add equation annotation
equation = f"Power Loss = {resistance:.2f} Ω * (Current^2) * Distance"
fig_line.add_annotation(text=equation,
                        xref="paper", yref="paper",
                        x=0.5, y=-0.15,
                        showarrow=False)

# Display the Plotly line plot
fig_line.show()

# Animate power loss calculation along the transmission line
animation_fig = go.Figure()

for i in range(len(distance)):
    animation_fig.add_trace(
        go.Scatter(x=[distance[i]], y=[loss_values[i]],
                   mode="markers",
                   marker=dict(size=10, color="blue"))
    )

    animation_fig.add_annotation(
        text=f"Distance: {distance[i]:.2f}<br>Power Loss: {loss_values[i]:.2f} W",
        x=distance[i], y=loss_values[i],
        arrowhead=2, showarrow=True
    )

    with animation_fig.batch_update():
        animation_fig.update_layout(
            title="Animating Power Loss Calculation",
            xaxis_title="Distance",
            yaxis_title="Power Loss (W)"
        )
        time.sleep(0.5)
        clear_output(wait=True)
        display(animation_fig)

# Display the final animation
animation_fig.show()
