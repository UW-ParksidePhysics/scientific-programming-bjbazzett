from vpython import *
# GlowScript 3.0 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

scene.background = color.white
scene.width = 600
scene.height = 600
scene.forward = vector(-.5,-.3,-1)

scene.caption= """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

xaxis=cylinder(color=vector(1,0,0), pos=vector(0,0,0), axis=vector(10,0,0), radius=0.3)
xlbl=label(pos=vector(11,0,0), text="X", color=color.red, opacity=0, height=30, box=0)
yaxis=cylinder(color=color.green, pos=vector(0,0,0), axis=vector(0,10,0), radius=0.3)
ylbl=label(pos=vector(0,11,0), text="Y", color=color.green, opacity=0, height=30, box=0)
zaxis=cylinder(color=color.blue, pos=vector(0,0,0), axis=vector(0,0,10), radius=0.3)

#vector comps as 4(April) 20(day of birth) 24 (sum of two)
a = 4
b = 20
c = 24

r = arrow(pos=vector(0, 0, 0), axis=vector(a, b, c), color= color.red, shaftwidth=1)

r_label = label(pos=vector(a, b, c), text=r"r = 4x̂ + 20ŷ + 24ẑ",
    height=20, box=0, color=color.red)
