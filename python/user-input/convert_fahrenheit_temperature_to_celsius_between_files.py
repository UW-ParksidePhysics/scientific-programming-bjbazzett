def convert_fahrenheit_to_celsius(fahrenheit):
    return (5.0 / 9.0) * (fahrenheit - 32)


def main():
    input_filename = "temperature2.txt"
    output_filename = "temperature3.txt"
    fahrenheit_values = []

    with open(input_filename, 'r') as file:
        for line in file:
            if "Fahrenheit degrees:" in line:
                    value = float(line.strip().split(":")[1])
                    fahrenheit_values.append(value)
    celsius_values = [convert_fahrenheit_to_celsius(f) for f in fahrenheit_values]

    with open(output_filename, 'w') as file:
        file.write(f"{'Fahrenheit':>12}    {'Celsius':>10}\n")
        file.write(f"{'-' * 12}    {'-' * 10}\n")
        for f, c in zip(fahrenheit_values, celsius_values):
            file.write(f"{f:12.2f}    {c:10.2f}\n")
    print(f"Converted temperatures posted in '{output_filename}'.")

if __name__ == '__main__':
    main()