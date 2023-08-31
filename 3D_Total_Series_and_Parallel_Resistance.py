import numpy as np
import pandas as pd
import plotly.express as px

# Generate data
R1_values = np.linspace(1, 1000, 50)
R2_values = np.linspace(1, 100, 50)

R1, R2 = np.meshgrid(R1_values, R2_values)
series_resistances = R1 + R2
parallel_resistances = 1 / (1 / R1 + 1 / R2)

# Create DataFrame for Series Resistance
df_series = pd.DataFrame({'R1': R1.flatten(), 'R2': R2.flatten(), 'Series Resistance': series_resistances.flatten()})

# Create DataFrame for Parallel Resistance
df_parallel = pd.DataFrame({'R1': R1.flatten(), 'R2': R2.flatten(), 'Parallel Resistance': parallel_resistances.flatten()})

# Interactive scatter plots
fig_series = px.scatter(df_series, x='R1', y='R2', size='Series Resistance',
                        color='Series Resistance', hover_name='Series Resistance',
                        labels={'Series Resistance': 'Series Resistance'},
                        title='Series Resistance Visualization')
fig_series.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGrey')))

fig_parallel = px.scatter(df_parallel, x='R1', y='R2', size='Parallel Resistance',
                          color='Parallel Resistance', hover_name='Parallel Resistance',
                          labels={'Parallel Resistance': 'Parallel Resistance'},
                          title='Parallel Resistance Visualization')
fig_parallel.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGrey')))

# Display plots
fig_series.show()
fig_parallel.show()

# Create DataFrame for Unreasonable Results
df_unreasonable = pd.DataFrame({'First Resistance': np.full(50, first_resistance),
                                'Second Resistance': R2_values,
                                'Total Resistance': total_resistance})

# Line plot for Unreasonable Results
fig_unreasonable = px.line(df_unreasonable, x='Second Resistance', y='Total Resistance',
                           labels={'Second Resistance': 'Second Resistance', 'Total Resistance': 'Total Resistance'},
                           title='Unreasonable Results: Total Resistance vs. Second Resistance')
fig_unreasonable.add_hline(y=first_resistance, line_dash="dash", line_color="red",
                           annotation_text=f'First Resistance ({first_resistance} Ω)',
                           annotation_position="bottom right")

# Display plot
fig_unreasonable.show()
