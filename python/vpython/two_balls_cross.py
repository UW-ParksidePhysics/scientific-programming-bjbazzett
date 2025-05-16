import vpython as vp

"""blue/redball settings and animation settings"""
initial_position_1 = vp.vector(-5, -2, -1)
initial_velocity_1 = vp.vector(1, 0.4, 0.2)
ball_1 = vp.sphere(pos=initial_position_1, radius=0.2,
                   color=vp.color.red, make_trail=True, retain=100)
initial_position_2 = vp.vector(5, 2, 1)
initial_velocity_2 = vp.vector(-1, -0.4, -0.2)
ball_2 = vp.sphere(pos=initial_position_2, radius=0.2,
                   color=vp.color.blue, make_trail=True, retain=100)
animation_time_step = 0.05
rate_of_animation = 1 / animation_time_step
time_step = 0.05
stop_time = 10.0
time = 0.0

"""animation loop"""
while time < stop_time:
    vp.rate(rate_of_animation)
    ball_1.pos = initial_position_1 + initial_velocity_1 * time
    ball_2.pos = initial_position_2 + initial_velocity_2 * time

    time += time_step