import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import sympy as sp
import torch
from sklearn.linear_model import LinearRegression
from scipy.integrate import odeint

def charging(t, emf, R, C):
    return emf * (1 - np.exp(-t / (R * C)))

def discharging(t, V0, R, C):
    return V0 * np.exp(-t / (R * C))

R = 1.0  # Resistor value
C = 1.0  # Capacitor value
emf = 5.0  # EMF of the voltage source
V0 = 5.0  # Initial voltage of the capacitor

tau = R * C
time = np.linspace(0, 5 * tau, 1000)  # Adjust the time span as needed

charging_voltage = charging(time, emf, R, C)
discharging_voltage = discharging(time, V0, R, C)

plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.plot(time, charging_voltage)
plt.title('Charging Voltage vs Time')
plt.xlabel('Time')
plt.ylabel('Voltage')

plt.subplot(2, 2, 2)
plt.plot(time, discharging_voltage)
plt.title('Discharging Voltage vs Time')
plt.xlabel('Time')
plt.ylabel('Voltage')

# Create 3D plots for charging and discharging
fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot3D(time, charging_voltage, np.zeros_like(time))
ax1.set_title('3D Plot - Charging')
ax1.set_xlabel('Time')
ax1.set_ylabel('Voltage')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot3D(time, discharging_voltage, np.zeros_like(time))
ax2.set_title('3D Plot - Discharging')
ax2.set_xlabel('Time')
ax2.set_ylabel('Voltage')

plt.show()
