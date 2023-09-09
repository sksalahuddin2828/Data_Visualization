import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given values
galvanometer_resistance = 40.0  # Ω
galvanometer_sensitivity = 25.0e-6  # A
desired_full_scale_current = 10.0e-6  # A

# Calculate the equivalent resistance in parallel
R_eq = (galvanometer_resistance * desired_full_scale_current) / (galvanometer_sensitivity - desired_full_scale_current)

# Create a DataFrame to store the results
data = {'Parameters': ['Galvanometer Resistance (Ω)', 'Galvanometer Sensitivity (A)',
                       'Desired Full-Scale Current (A)', 'Equivalent Resistance (Ω)'],
        'Value': [galvanometer_resistance, galvanometer_sensitivity,
                  desired_full_scale_current, R_eq]}
result_df = pd.DataFrame(data)

# Create a bar chart to visualize the result
fig = px.bar(result_df, x='Parameters', y='Value',
             labels={'Value': 'Value'},
             title='Equivalent Resistance for Ammeter Conversion')
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
fig.update_layout(yaxis_type='log', yaxis_title='Value (log scale)')

# Show the bar chart
fig.show()

# Print the result
print(f"The required parallel resistance is {R_eq:.2f} Ω")
