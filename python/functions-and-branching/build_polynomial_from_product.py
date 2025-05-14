def polynomial_from_roots(x, roots):
    p = 1
    for r in roots:
        p *= (x - r)
    return p

def test_polynomial_from_roots():
    roots = [1, 2, 3]
    test_x_values = [0, 3, 6]
    print("x     p(x)")
    print("------------")
    for x in test_x_values:
        px = polynomial_from_roots(x, roots)
        print(f"{x:<5} {px:<5}")

if __name__ == '__main__':
    test_polynomial_from_roots()