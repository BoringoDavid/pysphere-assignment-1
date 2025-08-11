# Ohm's Law Calculator
# Author: Boringo david 
#github: boringodavid

# Ask user for inputs
try:
    current = float(input("Enter the current (in A): "))
    resistance = float(input("Enter the resistance (in ohms): "))

    # Calculate voltage
    voltage = current * resistance

    # Output result
    print(f"The voltage is: {voltage} volts")

except ValueError:
    print("⚠ Please enter valid numeric values for current and resistance.")
