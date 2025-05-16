import math

"""compute gaussian function"""
def gaussian(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x**2)

"""adjust points for array"""
def main():
    x_values = []
    y_values = []
    num_points = 41
    start = -4
    end = 4
    step = (end - start) / (num_points - 1)
    for i in range(num_points):
        x = start + i * step
        y = gaussian(x)
        x_values.append(x)
        y_values.append(y)
    for x, y in zip(x_values, y_values):
        print(f"x = {x:.2f}, g(x) = {y:.5f}")

if __name__ == '__main__':
    main()