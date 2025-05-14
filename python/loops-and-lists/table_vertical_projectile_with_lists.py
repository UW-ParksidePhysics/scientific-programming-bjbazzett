initial_velocity = 10.00
grav_accel_titan = 1.352
grav_accel_trappist = 25.4

def y(t, initial_velocity, grav_accel):
    return initial_velocity * t - 0.5 * grav_accel * t ** 2

t_max = 2 * initial_velocity / min(grav_accel_titan, grav_accel_trappist)

times = []
positions_titan = []
positions_trappist = []

for i in range(9):
    t = i * t_max / 8
    times.append(t)
    positions_titan.append(y(t, initial_velocity, grav_accel_titan))
    positions_trappist.append(y(t, initial_velocity, grav_accel_trappist))

print("-----------------------------------------------------")
print("Titan (g = 1.352 m/s/s)  TRAPPIST-1b (g = 25.4 m/s/s)")
print("-----------------------------------------------------")
print("    t (s)         y (m)         t (s)         y (m)")
print("    -----         -----         -----         -----")

print("using a for loop:")
for t, y_titan, y_trappist in zip(times, positions_titan, positions_trappist):
    print(f"{t:10.3f}    {y_titan:10.3f}    {t:10.3f}    {y_trappist:10.3f}")

print("-----------------------------------------------------")