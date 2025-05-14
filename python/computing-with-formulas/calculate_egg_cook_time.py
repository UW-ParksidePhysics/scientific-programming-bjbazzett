import math

density = 1.038
thermal_conductivity = 5.4e-3
boiling_temperature = 373
target_temperature = 343
room_temperature = 293
fridge_temperature = 277
heat_capacity = 3.7
desired_egg_temperature = 343

small_egg_mass = 47
large_egg_mass = 67

def calculate_cook_time(mass, start_temp):
    term1 = (mass ** (2/3)) * heat_capacity * (density ** (1/3))
    term2 = thermal_conductivity * (math.pi ** 2) * ((4 * math.pi / 3) ** (2/3))
    time_seconds = (term1 / term2) * math.log(0.76 * (boiling_temperature - start_temp) / (boiling_temperature - desired_egg_temperature))
    time_minutes = time_seconds / 60
    return time_seconds, time_minutes

times = {
    "Small egg from fridge": calculate_cook_time(small_egg_mass, fridge_temperature),
    "Small egg from room": calculate_cook_time(small_egg_mass, room_temperature),
    "Large egg from fridge": calculate_cook_time(large_egg_mass, fridge_temperature),
    "Large egg from room": calculate_cook_time(large_egg_mass, room_temperature)}

print("Egg cooking times (in minutes):")
for condition, time in times.items():
    print(f"{condition}: {time[1]:.1f} minutes")