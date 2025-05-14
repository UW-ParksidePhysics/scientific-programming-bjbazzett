initial_velocity = 10
grav_accel_titan = 1.352
grav_accel_trappist_1b = 25.4

def y(t, initial_velocity, g):
    return initial_velocity * t - 0.5 * g * t ** 2

t_max = 2 * initial_velocity / min(grav_accel_titan, grav_accel_trappist_1b)

print("For initial velocity of 10.00 m/s:")
print("-----------------------------------------------------")
print("Titan (g = 1.352 m/s/s)  Trappist-1b (g = 25.4 m/s/s)")
print("-----------------------------------------------------")
print("    t (s)         y (m)         t (s)         y (m)")
print("-----------------------------------------------------")

for i in range(9):
    t = i * t_max / 8
    y_titan = y(t, initial_velocity, grav_accel_titan)
    y_trappist = y(t, initial_velocity, grav_accel_trappist_1b)
    print(f"{t:10.3f}    {y_titan:10.3f}    {t:10.3f}    {y_trappist:10.3f}")

print("using a while loop:")
t = 0
i = 0
while t <= t_max:
    y_titan = y(t, initial_velocity, grav_accel_titan)
    y_trappist = y(t, initial_velocity, grav_accel_trappist_1b)
    print(f"{t:10.3f}    {y_titan:10.3f}    {t:10.3f}    {y_trappist:10.3f}")
    t = (i + 1) * t_max / 8  # increment time (same logic for uniform spacing)
    i += 1
print("-----------------------------------------------------")