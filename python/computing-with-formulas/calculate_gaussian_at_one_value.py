import math

mean = 0
standard_deviation = 1
input_value = 1

gaussian_function = (1 / (math.sqrt(2 * math.pi) * standard_deviation)) * math.exp(-0.5 * ((input_value - mean) / standard_deviation) ** 2)

print(f"Mean (m): {mean}")
print(f"Standard Deviation (s): {standard_deviation}")
print(f"Input Value (x): {input_value}")
print(f"Gaussian f(x): {gaussian_function:.6f}")