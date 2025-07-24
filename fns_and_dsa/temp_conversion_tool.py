FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR

    if is_number(fahrenheit):
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f'{fahrenheit}°F is {celsius}°C')
    else:
        print("Invalid temperature. Please enter a numeric value.")


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR

    if is_number(celsius):
        celsius = float(celsius)
        fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
        print(f'{celsius}°C is {fahrenheit}°F')
    else:
        print("Invalid temperature. Please enter a numeric value.")


temperature = input("Enter the temperature to convert: ")
factor = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if factor == "F":
    convert_to_celsius(temperature)
elif factor == "C":
    convert_to_fahrenheit(temperature)
