import math

def gaussian(position, mean = 0, standard_deviation = 1):
    sigma = standard_deviation
    x_bar = mean
    coeff = 1 / (math.sqrt(2 * math.pi) * sigma)
    exponent = -0.5 * ((position - x_bar) / sigma) ** 2
    return coeff * math.exp(exponent)

def print_gaussian_table(mean = 0, standard_deviation = 1, n = 11):
    start = mean - 5 * standard_deviation
    end = mean + 5 * standard_deviation
    step = (end - start) / (n - 1)

    print(f"{'x':>10} {'f(x)':>20}")
    print("-" * 30)

    for i in range(n):
        x = start + i * step
        fx = gaussian(x, mean, standard_deviation)
        print(f"{x:10.4f} {fx:20.8f}")

if __name__ == '__main__':
    print_gaussian_table(mean=0, standard_deviation=1, n=11)