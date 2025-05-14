import math

air_density = 1.2
radius = .11
area = math.pi * radius ** 2
drag_coefficient = .2
grav_acceleration = 9.81
ball_mass = .43

def calculate_forces(ball_velocity):
    drag_force = 0.5 * air_density * ball_velocity ** 2 * area * drag_coefficient  # N
    gravitational_force = ball_mass * grav_acceleration  # N
    force_ratio = drag_force / gravitational_force

    print(f"\n--- For ball velocity: {ball_velocity} m/s ---")
    print(f"Drag force: {drag_force:.1f} N")
    print(f"Gravitational force: {gravitational_force:.1f} N")
    print(f"Ratio (drag/gravity): {force_ratio:.2f}")

calculate_forces(10)
calculate_forces(120)
