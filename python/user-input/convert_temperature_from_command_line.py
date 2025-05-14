import sys

def convert_fahrenheit_to_celsius(fahrenheit):
    return (5.0 / 9.0) * (fahrenheit - 32)

def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Missing Fahrenheit temperature on the command line.")
        fahrenheit = float(sys.argv[1])
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F is equivalent to {celsius:.2f}°C.")

    except IndexError as e:
        print(f"Error: {e}")
        print("Usage: python script.py <temperature_in_fahrenheit>")

    except ValueError:
        print("Error: The provided temperature must be a numeric value.")
        print("Usage: python script.py <temperature_in_fahrenheit>")

if __name__ == '__main__':
    main()