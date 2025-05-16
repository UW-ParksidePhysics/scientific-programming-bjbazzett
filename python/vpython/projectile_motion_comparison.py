import vpython as vp
import numpy as np
import time

#It starts off on the flat plain, but you can ctrl-drag/scroll to see the animation at a different angle
g_earth = 9.8
g_mars = 3.7
g_moon = 1.6
field_length = 40  # along x
field_width = 20   # along z (gravity acts here)
field_height = 0.5
ball_radius = 0.5
theta = np.pi / 6  # 30 degrees

"""calculate velocity at different g's"""
def calculate_velocity_components(g, x_target, z_target, theta):
    sin_2theta = np.sin(2 * theta)
    if sin_2theta == 0:
        raise ValueError("Launch angle too shallow or steep for valid range.")
    v0_squared = g * z_target / sin_2theta
    v0 = np.sqrt(2 * v0_squared)
    vx = v0 * np.cos(theta)
    vz = v0 * np.sin(theta)
    return vx, vz

"""ball/field/label creation"""
def create_scene(label_text, field_color, ball_color, x_offset):
    field = vp.box(pos=vp.vector(x_offset + field_length / 2, field_height / 2, field_width / 2),
                   size=vp.vector(field_length, field_height, field_width),
                   color=field_color, opacity=0.3)
    label = vp.text(text=label_text,
                    pos=vp.vector(x_offset + field_length / 2, -1.5, -5),
                    height=2, depth=0.2,
                    color=field_color, align='center')
    ball = vp.sphere(pos=vp.vector(x_offset, ball_radius, 0),
                     radius=ball_radius,
                     color=ball_color,
                     make_trail=True)
    return field, ball

"""varying velocity with respect to g to reach corner"""
def launch_balls(planets, theta):
    time_step = 0.01
    max_flight_time = 0.0
    for planet in planets:
        vx, vz = calculate_velocity_components(planet['g'], field_length, field_width, theta)
        v0z = vz
        t_flight = 2 * v0z / planet['g']
        planet['velocity'] = vp.vector(vx, 0, vz)
        planet['flight_time'] = t_flight
        if t_flight > max_flight_time:
            max_flight_time = t_flight
    t = 0
    while t < max_flight_time:
        vp.rate(100)
        for planet in planets:
            if t <= planet['flight_time']:
                ball = planet['ball']
                v = planet['velocity']
                g = planet['g']
                ball.pos += v * time_step + vp.vector(0, 0, -0.5 * g * time_step ** 2)
                planet['velocity'] += vp.vector(0, 0, -g * time_step)
        t += time_step
x_offsets = [-50, 0, 50]

planets = [
    {
        'name': "EARTH",
        'g': g_earth,
        'field_color': vp.color.green,
        'ball_color': vp.color.blue,
        'offset': x_offsets[0]
    },
    {
        'name': "MARS",
        'g': g_mars,
        'field_color': vp.color.red,
        'ball_color': vp.color.magenta,
        'offset': x_offsets[1]
    },
    {
        'name': "MOON",
        'g': g_moon,
        'field_color': vp.color.gray(0.6),
        'ball_color': vp.color.white,
        'offset': x_offsets[2]}]

for planet in planets:
    _, ball = create_scene(planet['name'], planet['field_color'], planet['ball_color'], planet['offset'])
    planet['ball'] = ball
launch_balls(planets, theta)
time.sleep(3)
for planet in planets:
    _, ball = create_scene(planet['name'], planet['field_color'], planet['ball_color'], planet['offset'])
    planet['ball'] = ball

launch_balls(planets, np.pi / 2 - theta)