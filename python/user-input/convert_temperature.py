"""conversion equations"""
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
def celsius_to_kelvin(c):
    return c + 273.15
def kelvin_to_celsius(k):
    return k - 273.15
def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))
def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def test_conversion():
    t = 21.3
    f = celsius_to_fahrenheit(t)
    k = celsius_to_kelvin(t)
    assert abs(fahrenheit_to_celsius(f) - t) < 0.01
    assert abs(kelvin_to_celsius(k) - t) < 0.01
    assert abs(kelvin_to_fahrenheit(fahrenheit_to_kelvin(f)) - f) < 0.01

def user_interface():
    import sys
    if len(sys.argv) != 3:
        print("Usage: python convert_temperature.py <temperature> <scale>")
        return
    try:
        t = float(sys.argv[1])
        s = sys.argv[2].upper()

        if s == 'C':
            print(f"{celsius_to_fahrenheit(t):.2f} F {celsius_to_kelvin(t):.2f} K")
        elif s == 'F':
            print(f"{fahrenheit_to_celsius(t):.2f} C {fahrenheit_to_kelvin(t):.2f} K")
        elif s == 'K':
            print(f"{kelvin_to_celsius(t):.2f} C {kelvin_to_fahrenheit(t):.2f} F")
        else:
            print("Invalid scale. Use 'C', 'F', or 'K'.")
    except ValueError:
        print("Invalid temperature. Please enter a number.")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'verify':
        test_conversion()
    else:
        user_interface()