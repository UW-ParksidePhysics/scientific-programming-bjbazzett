initial_velocity = 10.00  # m/s
grav_accel_titan = 1.352  # m/s^2
grav_accel_trappist = 25.4  # m/s^2

def y(t, initial_velocity, grav_accel):
    return initial_velocity * t - 0.5 * grav_accel * t ** 2

t_max_titan = 2 * initial_velocity / grav_accel_titan
t_max_trappist = 2 * initial_velocity / grav_accel_trappist

t_max = min(t_max_titan, t_max_trappist)

times = []
positions_titan = []
positions_trappist = []

for i in range(9):
    t = i * t_max / 8  # equally spaced times
    times.append(t)
    positions_titan.append(y(t, initial_velocity, grav_accel_titan))
    positions_trappist.append(y(t, initial_velocity, grav_accel_trappist))

times_positions = [times, [positions_titan, positions_trappist]]

print("-----------------------------------------------------")
print("Titan (g = 1.352 m/s/s)  Trappist-1b (g = 25.4 m/s/s)")
print("-----------------------------------------------------")
print("    t (s)         y (m)         t (s)         y (m)")
print("    -----         -----         -----         -----")

for i in range(len(times_positions[0])):
    t_titan = times_positions[0][i]
    y_titan = times_positions[1][0][i]
    t_trappist = times_positions[0][i]
    y_trappist = times_positions[1][1][i]

    if y_trappist >= 0:
        print(f"{t_titan:10.2f}    {y_titan:10.2f}    {t_trappist:10.2f}    {y_trappist:10.2f}")

print("-----------------------------------------------------")