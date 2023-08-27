import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Assuming you have calculated 'power_loss' earlier
power_loss = 2500.0  # Example value, replace with actual calculated power loss

# Matplotlib 2D plot
plt.figure(figsize=(10, 6))
plt.plot([0, 1], [0, power_loss], label="Power Loss")
plt.xlabel("Distance")
plt.ylabel("Power Loss (W)")
plt.title("Power Loss along Transmission Line")
plt.legend()
plt.show()

# Plotly interactive 3D plot
distance = np.linspace(0, 1, 100)
loss_values = line_resistance * (current_loss ** 2) * distance
fig = go.Figure(data=[go.Surface(z=loss_values.reshape(10, 10))])
fig.update_layout(title="Power Loss Distribution along Transmission Line",
                  scene=dict(xaxis_title="Distance", yaxis_title="Iteration", zaxis_title="Power Loss (W)"))
fig.show()
