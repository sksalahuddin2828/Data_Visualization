import numpy as np

frequency = 60  # Frequency in Hz
sampling_rate = 1000  # Samples per second
duration = 1  # Duration of signal in seconds

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
voltage = np.sin(2 * np.pi * frequency * t)

from scipy.signal import find_peaks

def find_crossings(signal, target_value):
    peaks, _ = find_peaks(signal)
    crossings = []
    for peak in peaks:
        if signal[peak] >= target_value:
            before = peak - 1
            while before >= 0 and signal[before] >= target_value:
                before -= 1
            after = peak
            while after < len(signal) and signal[after] >= target_value:
                after += 1
            if before >= 0 and after < len(signal):
                crossings.append((before, after))
    return crossings

target_voltages = [0.5, 1.0, 0.0]
crossing_times = {}
for target_voltage in target_voltages:
    crossings = find_crossings(voltage, target_voltage)
    crossing_times[target_voltage] = [(t[before], t[after]) for before, after in crossings]

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(t, voltage, label="AC Voltage")
for target_voltage in target_voltages:
    times = crossing_times[target_voltage]
    for before, after in times:
        plt.plot([before, after], [target_voltage, target_voltage], 'ro-')
plt.xlabel("Time (s)")
plt.ylabel("Voltage")
plt.title("AC Voltage and Crossing Points")
plt.legend()
plt.grid()
plt.show()
