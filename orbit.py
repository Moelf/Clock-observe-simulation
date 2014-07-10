from visual import *
import sys
scene.autoscale = 1
scene.range = 2
scene.userspin = 1
counter=0
view=0

## create three objects, set their initial
##   position, radius, color, and other
##   properties: mass, momentum("p")
giant = sphere()
giant.pos = vector(-0.201, 0.020, 0)
giant.radius = 0.075;
giant.color = color.red
giant.mass = 0.7
giant.p = vector(0, 0.01, -0.01) * giant.mass

dwarf = sphere()
dwarf.pos = vector(1.5, 0, 0)
dwarf.radius = 0.056;
dwarf.color = color.yellow
dwarf.mass = 0.05
dwarf.p = -giant.p

moon = sphere()
moon.pos = vector(1,1,1)
moon.radius = 0.04;
moon.color = color.cyan
moon.mass = 0.00125
moon.p = 0.035 * dwarf.p

## tweak initial condition so that total momentum is zero
giant.p -= moon.p

## create 'curve' objects showing where we've been
for a in [giant, dwarf, moon]:
    a.orbit = curve(color=a.color, radius=0.01)


def pstep(giant, dwarf):
    dist = dwarf.pos - giant.pos
    force = G * giant.mass * dwarf.mass * dist / mag(dist) ** 3
    giant.p = giant.p + force * dt
    dwarf.p = dwarf.p - force * dt
    dist = dwarf.pos - giant.pos

def viewswitcher():
    global view,scene,giant
    if view==0:
        view=1
    elif view==1:
        view=2
    elif view==2:
        view=0

dt = 0.01
G = 1
while 1:
    ## set the picture update rate (100 times per second)
    rate(500)
    pstep(giant, dwarf)
    pstep(giant, moon)
    pstep(moon, dwarf)
    counter+=1
    """if counter%500==0:
        viewswitcher()
    if view==0:
        scene.center=giant.pos
    elif view==1:
        scene.center=dwarf.pos
    elif view==2:
        scene.center=moon.pos"""
    print giant.pos,dwarf.pos,moon.pos
    for a in [giant, dwarf, moon]:
        a.pos = a.pos + a.p / a.mass * dt
        a.orbit.append(pos=a.pos)