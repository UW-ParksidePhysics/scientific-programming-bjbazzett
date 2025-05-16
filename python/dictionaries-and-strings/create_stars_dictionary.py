"""tuples to dictionary list"""
def convert_list_of_tuples(star_data):
    stars = {}
    for name, distance, brightness, luminosity in star_data:
        stars[name] = {'distance': distance, 'apparent brightness': brightness, 'luminosity': luminosity}
    return stars
"""prints info for stars in nested dictionary"""
def print_star_information(stars, name):
    if name not in stars:
        print(f"Star '{name}' not found.")
        return
    data = stars[name]
    print(f"Star: {name}")
    print(f"    Distance (ly):            {data['distance']}")
    print(f"    Apparent brightness (m):  {data['apparent brightness']}")
    print(f"    Luminosity (L_sun):       {data['luminosity']}")
    print()

if __name__ == '__main__':
    nearby_star_data = [
        ('Alpha Centauri A', 4.3, 0.26, 1.56),
        ('Alpha Centauri B', 4.3, 0.077, 0.45),
        ('Alpha Centauri C', 4.2, 0.00001, 0.00006),
        ("Barnard's Star", 6.0, 0.00004, 0.0005),
        ('Wolf 359', 7.7, 0.000001, 0.00002),
        ('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
        ('Luyten 726-8 A', 8.4, 0.000003, 0.00006),
        ('Luyten 726-8 B', 8.4, 0.000002, 0.00004),
        ('Sirius A', 8.6, 1.00, 23.6),
        ('Sirius B', 8.6, 0.001, 0.003),
        ('Ross 154', 9.4, 0.00002, 0.0005),]
    stars = convert_list_of_tuples(nearby_star_data)
    print_star_information(stars, 'Sirius A')
    print_star_information(stars, "Barnard's Star")