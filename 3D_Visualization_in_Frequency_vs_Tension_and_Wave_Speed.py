import numpy as np
import pandas as pd
import plotly.express as px
from sympy import symbols, sqrt, Eq, solve

# Constants and variables
mu = 0.03
length = 2.0
tension_values = np.linspace(10, 40, 100)

# Mathematical expressions
tension, wave_speed, frequency = symbols('tension wave_speed frequency')
wave_speed_eq = Eq(wave_speed, sqrt(tension / mu))
frequency_eq = Eq(frequency, wave_speed / length)

# Data generation and DataFrame
wave_speeds = [float(solve(wave_speed_eq.subs(tension, t))[0]) for t in tension_values]
frequencies = [float(solve(frequency_eq.subs(wave_speed, ws))[0]) for ws in wave_speeds]
results_df = pd.DataFrame({'Tension (N)': tension_values, 'Wave Speed (m/s)': wave_speeds, 'Frequency (Hz)': frequencies})

# Interactive 3D Visualization using Plotly
fig = px.scatter_3d(results_df, x='Tension (N)', y='Wave Speed (m/s)', z='Frequency (Hz)',
                    title='Frequency vs. Tension and Wave Speed',
                    labels={'Tension (N)': 'Tension (N)', 'Wave Speed (m/s)': 'Wave Speed (m/s)', 'Frequency (Hz)': 'Frequency (Hz)'},
                    hover_name='Tension (N)')

# Show interactive 3D Visualization
fig.show()
