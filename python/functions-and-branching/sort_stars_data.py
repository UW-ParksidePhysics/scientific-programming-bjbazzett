nearby_star_data = [
    ('Alpha Centauri A',    4.3,  0.26,      1.56),
    ('Alpha Centauri B',    4.3,  0.077,     0.45),
    ('Alpha Centauri C',    4.2,  0.00001,   0.00006),
    ("Barnard's Star",      6.0,  0.00004,   0.0005),
    ('Wolf 359',            7.7,  0.000001,  0.00002),
    ('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
    ('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
    ('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
    ('Sirius A',            8.6,  1.00,      23.6),
    ('Sirius B',            8.6,  0.001,     0.003),
    ('Ross 154',            9.4,  0.00002,   0.0005),
]

def star_tables(data):
    print("Distance from the Sun:")
    for star in sorted(nearby_star_data, key=lambda x: x[1]):
        print(f"{star[0]:<22} Distance: {star[1]} ly")
    print()

    print("Apparent brightness:")
    for star in sorted(nearby_star_data, key=lambda x: x[2]):
        print(f"{star[0]:<22} brightness: {star[2]}")
    print()

    print("Luminosity:")
    for star in sorted(nearby_star_data, key=lambda x: x[3]):
        print(f"{star[0]:<22} Luminosity: {star[3]}")
    print()

if __name__ == '__main__':
    star_tables(nearby_star_data)