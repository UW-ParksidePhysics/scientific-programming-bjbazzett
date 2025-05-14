"""
I could not, for the life of me, get the python shell to import the module. Used python 3.13 from the windows store,git command/bash, windows command prompt. Any online versions also failed to work.
"""

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def celsius_to_fahrenheit(celsius):
    return (9 / 5) * celsius + 32

def celsius_to_kelvin(celsius):
    return celsius + 273

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273

