max_integer = 100
sum_loop = 0

for i in range(1, max_integer + 1):
    sum_loop += i

sum_formula = max_integer * (max_integer + 1) // 2

print(f"n = {max_integer}")
print(f"sum(1, n) = {sum_loop}")
print(f"n(n+1)/2 = {sum_formula}")