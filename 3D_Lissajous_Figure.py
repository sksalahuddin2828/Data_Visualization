import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
from IPython.display import display

def plot_waveforms(freq):
    t = np.linspace(0, 0.1, 500)
    V = np.sin(2 * np.pi * freq * t)
    I = np.sin(2 * np.pi * freq * t - np.pi / 4)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, V, label='Voltage')
    plt.plot(t, I, label='Current')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'Voltage and Current Waveforms (Frequency = {freq} Hz)')
    plt.legend()
    plt.grid()
    plt.show()

freq_slider = widgets.FloatSlider(value=50, min=1, max=100, step=1, description='Frequency (Hz)')
widgets.interactive(plot_waveforms, freq=freq_slider)

def plot_frequency_domain(freq):
    t = np.linspace(0, 1, 1000)
    signal = np.sin(2 * np.pi * freq * t)
    signal_fft = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), d=(t[1] - t[0]))
    
    plt.figure(figsize=(10, 6))
    plt.plot(freqs, np.abs(signal_fft))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Domain Analysis')
    plt.grid()
    plt.show()

freq_slider = widgets.FloatSlider(value=10, min=1, max=100, step=1, description='Frequency (Hz)')
widgets.interactive(plot_frequency_domain, freq=freq_slider)

theta = np.linspace(0, 2 * np.pi, 1000)
x = np.sin(3 * theta + np.pi / 3)
y = np.sin(2 * theta)

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Lissajous Figure')
plt.xlabel('Voltage')
plt.ylabel('Current')
plt.grid()
plt.show()
