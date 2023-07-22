import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def complex_power(z, n):
    # Calculate the nth power of a complex number z using De Moivre's theorem
    modulus = np.abs(z)
    argument = np.angle(z)
    new_modulus = modulus ** n
    new_argument = argument * n
    return new_modulus * np.exp(1j * new_argument)

def complex_add(z1, z2):
    # Add two complex numbers z1 and z2
    return z1 + z2

def complex_subtract(z1, z2):
    # Subtract z2 from z1
    return z1 - z2

def complex_multiply(z1, z2):
    # Multiply two complex numbers z1 and z2
    return z1 * z2

def complex_divide(z1, z2):
    # Divide z1 by z2
    return z1 / z2

def euler_identity(angle):
    # Evaluate Euler's identity for a given angle in radians
    return np.exp(1j * angle)

def plot_complex_numbers(z_values, title):
    real_part = np.real(z_values)
    imag_part = np.imag(z_values)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(real_part, imag_part, 0, c='b', marker='o')
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')
    ax.set_zlabel('0')
    ax.set_title(title)
    plt.show()

def calculate():
    try:
        z = complex(complex_entry.get())
        n = int(n_entry.get())
        operation = operation_var.get()

        if operation == "Power":
            result = complex_power(z, n)
        elif operation == "Add":
            z2 = complex(complex_entry2.get())
            result = complex_add(z, z2)
        elif operation == "Subtract":
            z2 = complex(complex_entry2.get())
            result = complex_subtract(z, z2)
        elif operation == "Multiply":
            z2 = complex(complex_entry2.get())
            result = complex_multiply(z, z2)
        elif operation == "Divide":
            z2 = complex(complex_entry2.get())
            result = complex_divide(z, z2)
        else:
            messagebox.showerror("Error", "Invalid operation. Please choose a valid operation.")
            return

        result_label.config(text=f"Result: {result}")
        plot_complex_numbers([z, result], 'Complex Numbers Visualization')
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the GUI window
root = tk.Tk()
root.title("Complex Number Operations")
root.geometry("400x400")

# Complex number input
complex_label = tk.Label(root, text="Enter a complex number (a+bj):")
complex_label.pack()
complex_entry = tk.Entry(root)
complex_entry.pack()

# Integer n input
n_label = tk.Label(root, text="Enter an integer n:")
n_label.pack()
n_entry = tk.Entry(root)
n_entry.pack()

# Operation selection
operation_var = tk.StringVar(root)
operation_var.set("Power")
operation_options = ["Power", "Add", "Subtract", "Multiply", "Divide"]
operation_menu = tk.OptionMenu(root, operation_var, *operation_options)
operation_menu.pack()

# Second complex number input (only for certain operations)
complex_label2 = tk.Label(root, text="Enter another complex number (a+bj):")
complex_entry2 = tk.Entry(root)
complex_label2.pack()
complex_entry2.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI
root.mainloop()
