import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import sympy as sp

# Step 2: Define the Riemann Zeta Function
def zeta(s):
    return np.sum(1 / np.power(np.arange(1, 10000), s))

# Step 3: Define the Riemann Zeta Function on the Critical Line
def zeta_critical_line(t):
    s = 0.5 + 1j * t
    return zeta(s).real

# Step 4: Visualize the Riemann Zeta Function on the Critical Line
t_values = np.linspace(0, 81702130.19, 500)
zeta_values = [zeta_critical_line(t) for t in t_values]

plt.figure(figsize=(12, 6))
plt.plot(t_values, zeta_values, label='Riemann Zeta Function on Critical Line', color='blue')
plt.xlabel('t')
plt.ylabel('zeta(1/2 + it)')
plt.title('Riemann Zeta Function on the Critical Line')
plt.legend()
plt.grid(True)
plt.show()

# Step 5: Visualize the Zeros of the Riemann Zeta Function on the Critical Line
def find_zeros(t_range):
    zeros = []
    for t in t_range:
        s = 0.5 + 1j * t
        z = zeta(s)
        if abs(z) < 1e-8:
            zeros.append(t)
    return zeros

t_values = np.linspace(0, 81702130.19, 2000)
zeros = find_zeros(t_values)

plt.figure(figsize=(12, 6))
plt.plot(t_values, np.zeros(len(t_values)), label='Critical Line', color='black')
plt.scatter(zeros, np.zeros(len(zeros)), color='red', marker='o', label='Zeros on Critical Line')
plt.xlabel('t')
plt.title('Zeros of the Riemann Zeta Function on the Critical Line')
plt.legend()
plt.grid(True)
plt.show()

# Step 6: Interactive Visualization - Symmetry of Zeros
t_values_positive = np.linspace(0, 4000000000, 1000)
t_values_negative = -t_values_positive
zeros_positive = find_zeros(t_values_positive)
zeros_negative = find_zeros(t_values_negative)

fig = go.Figure()

# Add the zeros of the Riemann zeta function on the critical line
fig.add_trace(go.Scatter(x=zeros_positive, y=[0] * len(zeros_positive), mode='markers', marker=dict(color='red', size=5),
                         name='Zeros on Critical Line (Positive t)'))
fig.add_trace(go.Scatter(x=zeros_negative, y=[0] * len(zeros_negative), mode='markers', marker=dict(color='blue', size=5),
                         name='Zeros on Critical Line (Negative t)'))

fig.update_layout(title='Symmetry of Zeros on the Critical Line',
                  xaxis_title='t',
                  yaxis_title='zeta(1/2 + it)',
                  legend=dict(x=0.8, y=0.1),
                  showlegend=True)

fig.show()

# Step 7: Interactive Visualization - Equivalent Statements of the Riemann Hypothesis
x_values = np.linspace(1, 1000, 100)
li_x = np.log(x_values)
pi_x = np.cumsum([sp.isprime(int(x)) for x in x_values])  # Use sympy.isprime

c = 0.1  # You can adjust this constant for scaling purposes
upper_bound = c * np.sqrt(x_values) * np.log(x_values)
lower_bound = -upper_bound

fig = go.Figure()

# Add the difference between Li(x) and pi(x) and the upper/lower bounds
fig.add_trace(go.Scatter(x=x_values, y=li_x - pi_x, mode='lines', name='Li(x) - pi(x)', line=dict(color='purple')))
fig.add_trace(go.Scatter(x=x_values, y=upper_bound, mode='lines', name='Upper Bound', line=dict(color='orange', dash='dash')))
fig.add_trace(go.Scatter(x=x_values, y=lower_bound, mode='lines', name='Lower Bound', line=dict(color='brown', dash='dash')))

fig.update_layout(title='Prime Number Theorem and Equivalent Statements',
                  xaxis_title='x',
                  yaxis_title='Difference',
                  legend=dict(x=0.8, y=0.1),
                  showlegend=True)

fig.show()

# Step 8: Final Interactive Visualization - Combining all Visualizations
fig = go.Figure()

# Add the Riemann zeta function on the critical line
fig.add_trace(go.Scatter(x=t_values, y=zeta_values, mode='lines', name='Riemann Zeta Function on Critical Line'))

# Add the zeros of the Riemann zeta function on the critical line
fig.add_trace(go.Scatter(x=zeros, y=[0] * len(zeros), mode='markers', marker=dict(color='red', size=5),
                         name='Zeros on Critical Line'))

# Add the zeros of the Riemann zeta function on the critical line (Symmetry)
fig.add_trace(go.Scatter(x=zeros_positive, y=[0] * len(zeros_positive), mode='markers', marker=dict(color='blue', size=5),
                         name='Zeros on Critical Line (Positive t)'))
fig.add_trace(go.Scatter(x=zeros_negative, y=[0] * len(zeros_negative), mode='markers', marker=dict(color='green', size=5),
                         name='Zeros on Critical Line (Negative t)'))

# Add the difference between Li(x) and pi(x) and the upper/lower bounds
fig.add_trace(go.Scatter(x=x_values, y=li_x - pi_x, mode='lines', name='Li(x) - pi(x)', line=dict(color='purple')))
fig.add_trace(go.Scatter(x=x_values, y=upper_bound, mode='lines', name='Upper Bound', line=dict(color='orange', dash='dash')))
fig.add_trace(go.Scatter(x=x_values, y=lower_bound, mode='lines', name='Lower Bound', line=dict(color='brown', dash='dash')))

fig.update_layout(title='Riemann Hypothesis - Interactive Visualization',
                  xaxis_title='t / x',
                  yaxis_title='zeta(1/2 + it) / Difference',
                  legend=dict(x=0.8, y=0.1),
                  showlegend=True)

fig.show()
