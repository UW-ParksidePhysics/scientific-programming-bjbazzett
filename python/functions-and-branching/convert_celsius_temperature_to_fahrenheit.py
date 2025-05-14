def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit- 32) * 5/9

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 5/9) + 32

def test_temperatures():
    celsius_temperatures = [0, 21, 100]

    print("---------------------------------------------------------------")
    print("Celsius (°C)   → Fahrenheit (°F)   → Back to Celsius (°C)")
    print("---------------------------------------------------------------")

    for temp_c in celsius_temperatures:
        temp_f = convert_celsius_to_fahrenheit(temp_c)
        temp_c_back = convert_fahrenheit_to_celsius(temp_f)
        print(f"{temp_c:10.2f}     → {temp_f:10.2f}       → {temp_c_back:10.2f}")

    print("---------------------------------------------------------------")

if __name__ == '__main__':
    test_temperatures()