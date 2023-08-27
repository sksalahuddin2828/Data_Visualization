import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# (b) Power loss in a 1.00-Ω transmission line
line_resistance = 1.00  # Ω

# Sample data for demonstration
power_loss = 2500.0  # Example value, replace with actual calculated power loss

# Create a DataFrame for power loss values along the transmission line
distance = np.linspace(0, 1, 100)
loss_values = line_resistance * (current_loss ** 2) * distance
df = pd.DataFrame({"Distance": distance, "Power Loss": loss_values})

# Plotly interactive 3D plot
fig_3d = go.Figure(data=[go.Surface(z=loss_values.reshape(10, 10))])
fig_3d.update_layout(title="Power Loss Distribution along Transmission Line",
                     scene=dict(xaxis_title="Distance", yaxis_title="Iteration", zaxis_title="Power Loss (W)"))

# Plotly interactive line plot
fig_line = px.line(df, x="Distance", y="Power Loss", title="Power Loss along Transmission Line")
fig_line.update_xaxes(title="Distance")
fig_line.update_yaxes(title="Power Loss (W)")

# Show the Plotly plots
fig_3d.show()
fig_line.show()
