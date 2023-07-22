import numpy as np

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

def main():
    z = complex(input("Enter a complex number in the format a+bj: "))
    n = int(input("Enter an integer n: "))
    operation = input("Choose an operation (power/add/subtract/multiply/divide): ")

    if operation == "power":
        result = complex_power(z, n)
    elif operation == "add":
        z2 = complex(input("Enter another complex number in the format a+bj: "))
        result = complex_add(z, z2)
    elif operation == "subtract":
        z2 = complex(input("Enter another complex number in the format a+bj: "))
        result = complex_subtract(z, z2)
    elif operation == "multiply":
        z2 = complex(input("Enter another complex number in the format a+bj: "))
        result = complex_multiply(z, z2)
    elif operation == "divide":
        z2 = complex(input("Enter another complex number in the format a+bj: "))
        result = complex_divide(z, z2)
    else:
        print("Invalid operation. Please choose a valid operation.")
        return

    print(f"Result: {result}")
    plot_complex_numbers([z, result], 'Complex Numbers Visualization')

if __name__ == "__main__":
    main()
