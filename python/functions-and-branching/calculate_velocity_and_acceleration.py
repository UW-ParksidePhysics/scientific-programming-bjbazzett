def calculate_velocity_and_acceleration(positions, times, index, time_step=1e-6):
    i = index
    t_prev = times[i - 1]
    t_curr = times[i]
    t_next = times[i + 1]

    x_prev = positions[i - 1]
    x_curr = positions[i]
    x_next = positions[i + 1]

    velocity = (x_next - x_prev) / (t_next - t_prev)

    acceleration = 2 / (t_next - t_prev) * (
        (x_next - x_curr) / (t_next - t_curr) - (x_curr - x_prev) / (t_curr - t_prev)
    )

    return velocity, acceleration

def test_kinematics():
    constant_velocity = 10.0
    times = [0.0, 0.5, 2.2]
    positions = [constant_velocity * t for t in times]

    print("Test for motion based on GPS:")
    print("Times:     ", times)
    print("Positions: ", positions)

    velocity, acceleration = calculate_velocity_and_acceleration(positions, times, index=1)

    print(f"Calculated velocity at i=1: {velocity:.6f} m/s")
    print(f"Calculated acceleration at i=1: {acceleration:.6f} m/s²")

if __name__ == '__main__':
    test_kinematics()