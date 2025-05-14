print(f"{'°F':>5} {'°C':>12} {'°C (Approximate)':>14}")

fahrenheit = 0

while fahrenheit <= 100:
    exact_celsius = (fahrenheit - 32) * 5/9
    approx_celsius = (fahrenheit - 30) / 2
    print(f"{fahrenheit:>5} {exact_celsius:12.2f} {approx_celsius:14.2f}")
    fahrenheit += 10