# Ask user to enter temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Now ask for Fahrenheit and convert to Celsius
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
celsius_converted = (fahrenheit_input - 32) * 5/9
print("Temperature in Celsius:", celsius_converted)
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

    fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
    celsius_converted = (fahrenheit_input - 32) * 5/9
    print("Temperature in Celsius:", celsius_converted)

except ValueError:
    print("Please enter a valid number!")