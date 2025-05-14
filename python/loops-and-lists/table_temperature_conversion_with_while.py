temp_interval = 10
fahrenheit_temp = 0
max_temp = 100

while fahrenheit_temp <= max_temp:
    celsius = (fahrenheit_temp - 32) * 5/9
    print(f'{fahrenheit_temp:6}\t{celsius:6.3f}')
    fahrenheit_temp += temp_interval
