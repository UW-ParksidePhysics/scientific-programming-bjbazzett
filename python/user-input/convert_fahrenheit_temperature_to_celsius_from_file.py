def convert_fahrenheit_to_celsius(fahrenheit):
    return (5.0 / 9.0) * (fahrenheit - 32)


def main():
    filename = "temperature.txt"

    with open(filename, 'r') as file:
        lines = file.readlines()

    # Find the line with "Fahrenheit degrees"
    for line in lines:
        if "Fahrenheit degrees:" in line:
            parts = line.strip().split(':')
            if len(parts) == 2:
                fahrenheit = float(parts[1].strip())
                celsius = convert_fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit:.2f}°F is equivalent to {celsius:.2f}°C.")
                return

    print("Fahrenheit temperature not found in the file.")


if __name__ == '__main__':
    main()