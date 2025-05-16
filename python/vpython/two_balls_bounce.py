import vpython as vp

"""ball, wall, and bounce parameters"""
wall_center = vp.vector(0, 0, 0)
wall_dimensions = vp.vector(0.5, 10, 1)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.red)
ball_radius = 0.5
half_wall_width = wall_dimensions.x / 2
ball1 = vp.sphere(
    pos=vp.vector(-10, -wall_dimensions.y / 2, 0),
    radius=ball_radius,
    color=vp.color.blue,
    make_trail=True
)
ball1_velocity = vp.vector(5, 2, 0)
ball2 = vp.sphere(
    pos=vp.vector(-10, wall_dimensions.y / 2, 0),
    radius=ball_radius,
    color=vp.color.green,
    make_trail=True
)
ball2_velocity = vp.vector(5, -3, 0)
animation_time_step = 0.01
rate_of_animation = 1 / animation_time_step
stop_time = 5
time = 0

"""animation loop+ball bounce"""
while time < stop_time:
    vp.rate(rate_of_animation)
    ball1.pos += ball1_velocity * animation_time_step
    if abs(ball1.pos.x - wall.pos.x) <= (ball_radius + half_wall_width):
        ball1_velocity.x = -ball1_velocity.x
        ball1_velocity.y *= 0.8  # slightly reduce y velocity after bounce
    ball2.pos += ball2_velocity * animation_time_step
    if abs(ball2.pos.x - wall.pos.x) <= (ball_radius + half_wall_width):
        ball2_velocity.x = -ball2_velocity.x
        ball2_velocity.y *= 1.2

    time += animation_time_step