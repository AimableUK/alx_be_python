FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR

    print(f'{fahrenheit}°F is {(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR}°C')


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR

    print(f'{celsius}°C is {celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32}°F')


temperature = int(input("Enter the temperature to convert: "))
factor = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

# if temperature / 2 == :

if factor == "F":
    convert_to_celsius(temperature)
elif factor == "C":
    convert_to_fahrenheit(temperature)
