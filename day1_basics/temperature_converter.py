# Temperature Converter

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheot to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# User Input
temperature = float(input("Enter the temperature: "))
unit = input("Is this in Celsius or Fahrenheit (C/F)? ").lower()

if unit == 'c':
    print(f"{temperature}°C is {celsius_to_fahrenheit(temperature)}°F")
elif unit == 'f':
    print(f"{temperature}°F is {fahrenheit_to_celsius(temperature)}°C")
else:
    print("Invalid unit entered!")# Add this line to handle invalid inputs