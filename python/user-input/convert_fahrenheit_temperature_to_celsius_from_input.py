def convert_fahrenheit_to_celsius(fahrenheit):
    return (5.0 / 9.0) * (fahrenheit - 32)

def main():
    fahrenheit = float(input("Enter temperature in fahrenheit please: "))
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit:.2f}°F is equivalent to {celsius:.2f}°C.")

if __name__ == '__main__':
    main()