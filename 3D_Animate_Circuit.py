import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

# Define circuit components and properties
class Resistor:
    def __init__(self, resistance):
        self.resistance = resistance

class CurrentSource:
    def __init__(self, current):
        self.current = current

class Junction:
    def __init__(self):
        self.current_sources_in = []
        self.current_sources_out = []

    def add_current_source_in(self, current_source):
        self.current_sources_in.append(current_source)

    def add_current_source_out(self, current_source):
        self.current_sources_out.append(current_source)

# Apply Kirchhoff's first rule to calculate currents
def apply_kirchhoffs_first_rule(junction, resistors):
    total_current_in = sum(source.current for source in junction.current_sources_in)
    total_current_out = sum(source.current for source in junction.current_sources_out)
    total_resistance = sum(resistor.resistance for resistor in resistors)
    voltage_drop = total_current_in * total_resistance
    return total_current_in, total_current_out, voltage_drop

# Create an animated circuit visualization
def animate_circuit(junction, resistors, num_frames, animation_interval):
    fig, ax = plt.subplots()
    
    # Create circuit visualization (lines, arrows, labels)
    ax.add_patch(patches.Rectangle((0.1, 0.3), 0.1, 0.4, fill=False, color='black'))
    ax.add_patch(patches.Arrow(0.2, 0.5, 0.2, 0, width=0.02, color='blue'))
    ax.add_patch(patches.Arrow(0.2, 0.5, 0, -0.2, width=0.02, color='red'))
    ax.text(0.15, 0.2, 'R1', fontsize=12, color='black')
    ax.text(0.35, 0.2, 'R2', fontsize=12, color='black')
    ax.text(0.2, 0.7, 'I1', fontsize=12, color='blue')
    ax.text(0.4, 0.7, 'I2', fontsize=12, color='red')
    
    def update(frame):
        ax.clear()
        
        # Create circuit visualization (lines, arrows, labels)
        ax.add_patch(patches.Rectangle((0.1, 0.3), 0.1, 0.4, fill=False, color='black'))
        ax.add_patch(patches.Arrow(0.2, 0.5, 0.2, 0, width=0.02, color='blue'))
        ax.add_patch(patches.Arrow(0.2, 0.5, 0, -0.2, width=0.02, color='red'))
        ax.text(0.15, 0.2, 'R1', fontsize=12, color='black')
        ax.text(0.35, 0.2, 'R2', fontsize=12, color='black')
        ax.text(0.2, 0.7, 'I1', fontsize=12, color='blue')
        ax.text(0.4, 0.7, 'I2', fontsize=12, color='red')
        
        # Apply Kirchhoff's first rule
        total_in, total_out, voltage_drop = apply_kirchhoffs_first_rule(junction, resistors)
        
        # Update animation elements (current arrows, voltage labels)
        ax.text(0.6, 0.7, f'I1 = {total_in:.2f} A', fontsize=12, color='blue')
        ax.text(0.6, 0.6, f'I2 = {total_out:.2f} A', fontsize=12, color='red')
        ax.text(0.6, 0.5, f'Voltage Drop = {voltage_drop:.2f} V', fontsize=12, color='black')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal', adjustable='box')
        ax.axis('off')

    ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=animation_interval)
    plt.show()

# Create circuit components
resistor1 = Resistor(2.0)
resistor2 = Resistor(3.0)
current_source1 = CurrentSource(5.0)
current_source2 = CurrentSource(3.0)

# Create a junction and add components
junction = Junction()
junction.add_current_source_in(current_source1)
junction.add_current_source_in(current_source2)
junction.add_current_source_out(resistor1)
junction.add_current_source_out(resistor2)

# Animate the circuit (you can customize num_frames and animation_interval)
animate_circuit(junction, [resistor1, resistor2], num_frames=100, animation_interval=100)
