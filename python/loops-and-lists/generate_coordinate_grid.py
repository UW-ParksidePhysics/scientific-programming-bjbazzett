interval = 20
a = 1
b = 2
interval_length = (b - a) / interval

coordinates_loop = []
for i in range(interval + 1):
    coordinates_loop.append(a + i * interval_length)

coordinates_list_comprehension = [a + i * interval_length for i in range(interval + 1)]

print(f"For x in [{a}, {b}] with {interval} intervals, the interval length is h = {interval_length:.3f}, and")
print("Using a for loop:")
print(f"x = {coordinates_loop}")
print("Using list comprehension:")
print(f"x = {coordinates_list_comprehension}")