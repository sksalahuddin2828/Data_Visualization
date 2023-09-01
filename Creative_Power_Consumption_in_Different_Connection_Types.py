import numpy as np
import pandas as pd
import plotly.express as px

# Constants
V = 12.0  # Voltage in volts
headlight_power = 30.0  # Headlight power in watts
starter_power = 2400.0  # Starter power in watts

# Resistance calculations
headlight_resistance = V**2 / headlight_power
starter_resistance = V**2 / starter_power

# Parallel Connection
total_parallel_resistance = 1 / ((1 / headlight_resistance) + (1 / starter_resistance))
parallel_current = V / total_parallel_resistance
parallel_headlight_power = parallel_current**2 * headlight_resistance
parallel_starter_power = parallel_current**2 * starter_resistance

# Series Connection
total_series_resistance = headlight_resistance + starter_resistance
series_current = V / total_series_resistance
series_headlight_power = series_current**2 * headlight_resistance
series_starter_power = series_current**2 * starter_resistance

# Create a Pandas DataFrame
data = {
    'Connection Type': ['Parallel', 'Series'],
    'Power Consumed (W)': [parallel_headlight_power + parallel_starter_power, series_headlight_power + series_starter_power]
}
df = pd.DataFrame(data)

# Create an interactive bar chart using Plotly
fig = px.bar(
    df,
    x='Connection Type',
    y='Power Consumed (W)',
    text='Power Consumed (W)',
    title='Power Consumption in Different Connection Types',
    color='Connection Type',
    labels={'Connection Type': 'Connection Type'},
    height=400
)

fig.update_traces(texttemplate='%{text:.2f} W', textposition='outside')

# Enhance the chart with customizations
fig.update_layout(
    xaxis=dict(type='category'),
    yaxis=dict(title='Power Consumed (W)'),
    uniformtext_minsize=10,
    uniformtext_mode='hide',
    bargap=0.2,
    showlegend=False,  # Hide legend
    template='plotly_dark',  # Dark theme
    hovermode='closest',  # Show closest data on hover
)

# Add annotations for more context
fig.add_annotation(
    text=f'Parallel: {parallel_headlight_power + parallel_starter_power:.2f} W',
    x=0,
    y=parallel_headlight_power + parallel_starter_power + 10,
    showarrow=False,
    font=dict(size=12, color='white')
)

fig.add_annotation(
    text=f'Series: {series_headlight_power + series_starter_power:.2f} W',
    x=1,
    y=series_headlight_power + series_starter_power + 10,
    showarrow=False,
    font=dict(size=12, color='white')
)

# Add a background image or texture (you can customize this part)
fig.update_layout(
    images=[
        dict(
            source="your_image_url.png",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            sizex=1,
            sizey=1,
            opacity=0.2,
            layer="below",
        )
    ]
)

# Customize axis and layout colors
fig.update_xaxes(showline=True, linewidth=1, linecolor='gray', gridcolor='gray')
fig.update_yaxes(showline=True, linewidth=1, linecolor='gray', gridcolor='gray')

# Add a 3D effect
fig.update_layout(scene=dict(zaxis=dict(showline=False)))
fig.update_layout(scene=dict(zaxis_title=''))

# Customize plot background color
fig.update_layout(plot_bgcolor='black')

# Add interactivity
fig.update_traces(marker=dict(line=dict(width=2, color='black')))

# Show the chart
fig.show()
