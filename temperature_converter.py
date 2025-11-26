def celcius_to_fahrenheit(celcius):
    celcius = float(celcius)
    fahrenheit = (celcius * 9/5)+ 32
    print(f'{celcius}° celcius is {fahrenheit}° Fahrenheit')

def celcius_to_kelvin(celcius):
    celcius = float(celcius)
    kelvin = celcius + 273.15
    print(f'{celcius}° celcius is {kelvin} kelvin')

def fahrenheit_to_celcius(fahrenheit):
    fahrenheit = float(fahrenheit)
    celcius = (fahrenheit - 32) * 5/9
    print(f'{fahrenheit}° fahrenheit is {celcius}° celcius')

def fahrenheit_to_kelvin(fahrenheit):
    fahrenheit = float(fahrenheit)
    kelvin = (fahrenheit - 32)* 5/9 + 273.15
    print(f'{fahrenheit}° fahrenheit is {kelvin} kelvin')

def kelvin_to_celcius(kelvin):
    kelvin = float(kelvin)
    celcius = kelvin - 273.15
    print(f'{kelvin} kelvin is {celcius}° celcius')

def kelvin_to_fahrenheit(kelvin):
    kelvin = float(kelvin)
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print(f'{kelvin} kelvin is {fahrenheit}° fahrenheit')

while True:
    current_unit = input('What is your current unit?(Celcius, fahrenheit, or kelvin): ').lower()
    convert_to = input('And you wish to convert to...:  ').lower()
    value = input(f'value of {current_unit} you wish to convert to {convert_to}: ')
    try:
        value = float(value)
    except ValueError:
        print("Sorry, invalid value ")
        break
    if current_unit == "celcius" and convert_to == "fahrenheit":
        celcius_to_fahrenheit(value)
        break
    elif current_unit == "celcius" and convert_to == "kelvin":
        celcius_to_kelvin(value)
        break
    elif current_unit == "fahrenheit" and convert_to == "celcius":
        fahrenheit_to_celcius(value)
        break
    elif current_unit == "fahrenheit" and convert_to == "kelvin":
        fahrenheit_to_kelvin(value)
        break
    elif current_unit == "kelvin" and convert_to == "celcius":
        kelvin_to_celcius(value)
        break
    elif current_unit == "kelvin" and convert_to == "fahrenheit":
        kelvin_to_fahrenheit(value)
        break
    else:
        print("invalid, try again")

