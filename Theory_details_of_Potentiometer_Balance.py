import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy.interpolate import griddata
from IPython.display import display, Markdown, HTML, clear_output

# Given data
emf_standard = 3.0  # Standard EMF in volts
rs_values = np.linspace(10.0, 20.0, 50)  # Range of Rs values from 10.0 Ω to 20.0 Ω
emfx_values = np.linspace(0.0, 5.0, 50)  # Range of unknown EMF values from 0.0 V to 5.0 V

# Create a grid of Rs and EMFx values
rs_grid, emfx_grid = np.meshgrid(rs_values, emfx_values)

# Calculate corresponding Rx values using the potentiometer formula
rx_grid = emfx_grid * (rs_grid / emf_standard - 1)

# Create a Pandas DataFrame for the data
data = pd.DataFrame({'Rs': rs_grid.ravel(), 'EMFx': emfx_grid.ravel(), 'Rx': rx_grid.ravel()})

# Use Plotly to create an interactive 3D surface plot
fig = px.scatter_3d(data, x='Rs', y='EMFx', z='Rx', color='Rx',
                    title='3D Visualization of Potentiometer Balance',
                    labels={'Rx': 'Rx (Ω)'})

# Add labels and customize the appearance
fig.update_traces(marker=dict(size=2))
fig.update_layout(scene=dict(xaxis_title='Rs (Ω)', yaxis_title='EMFx (V)', zaxis_title='Rx (Ω)'))

# Define a function to update the Rx value based on user input
def update_rx(emfx, rs):
    target_rx = griddata((rs_grid.ravel(), emfx_grid.ravel()), rx_grid.ravel(), (rs, emfx), method='linear')
    return target_rx

# Create interactive sliders for EMFx and Rs
emfx_slider = go.FigureWidget(data=[go.Scatter(x=data['EMFx'], y=data['Rx'], mode='lines')],
                              layout=go.Layout(title='Rx vs. EMFx',
                                               xaxis=dict(title='EMFx (V)'),
                                               yaxis=dict(title='Rx (Ω)'),
                                               showlegend=False))
rs_slider = go.FigureWidget(data=[go.Scatter(x=data['Rs'], y=data['Rx'], mode='lines')],
                            layout=go.Layout(title='Rx vs. Rs',
                                             xaxis=dict(title='Rs (Ω)'),
                                             yaxis=dict(title='Rx (Ω)'),
                                             showlegend=False))

display(HTML("<h2>Interactive Rx Calculation</h2>"))
display(Markdown("Use the sliders below to calculate Rx for given EMFx and Rs values."))
display(Markdown("Choose EMFx (V):"))
display(emfx_slider)
display(Markdown("Choose Rs (Ω):"))
display(rs_slider)

# Define a function to update the slider plots
def update_slider_plots(change):
    with emfx_slider.batch_update(), rs_slider.batch_update():
        emfx = emfx_slider.data[0].x
        rs = rs_slider.data[0].x
        emfx_slider.data[0].y = [update_rx(emfx_val, rs[0]) for emfx_val in emfx]
        rs_slider.data[0].y = [update_rx(emfx[0], rs_val) for rs_val in rs]

# Link sliders to the update function
emfx_slider.data[0].x = emfx_values
rs_slider.data[0].x = rs_values
emfx_slider.data[0].y = [update_rx(emfx, rs_values[0]) for emfx in emfx_values]
rs_slider.data[0].y = [update_rx(emfx_values[0], rs) for rs in rs_values]
emfx_slider.observe(update_slider_plots, 'data')
rs_slider.observe(update_slider_plots, 'data')

# Display equations and explanations using MathJax
display(HTML("<h2>Mathematical Equations and Theory</h2>"))
display(Markdown("The formula for calculating Rx in a potentiometer is given by:"))
display(Markdown(r"$$Rx = \frac{{EMFx \cdot Rs}}{{E_{\text{standard}}} - EMFx}}$$"))
display(Markdown("Where:"))
display(Markdown("Rx = Unknown resistance (Ω)"))
display(Markdown("EMFx = EMF across the potentiometer (V)"))
display(Markdown("Rs = Known resistance (Ω)"))
display(Markdown(r"$E_{\text{standard}}$ = Standard EMF (V)"))
display(Markdown("This formula allows us to calculate Rx for given EMFx and Rs values."))

# Add animations or additional explanations here as desired

# Final display
display(HTML("<h2>Project Conclusion</h2>"))
display(Markdown("This project has demonstrated how a potentiometer can be used to calculate the unknown resistance (Rx) by balancing the EMF across it with a known resistance (Rs) and a standard EMF (E_standard). The interactive 3D visualization provides insights into how Rx varies with different EMFx and Rs values, and the sliders enable users to calculate Rx for specific conditions."))
