from visual import *

giant = sphere()
giant.pos = vector(-1,0.20,0)
giant.radius = 0.075
giant.color = color.red
giant.mass = 5
giant.p = vector(0, 0.2, -0.3) * giant.mass

dwarf = sphere()
dwarf.pos = vector(1,0,0)
dwarf.radius = 0.04
dwarf.color = color.yellow
dwarf.mass = 1
dwarf.p = -giant.p

middle=sphere()

middle.radius=0.02
middle.color=color.cyan
middle.p=vector(0,0,0)
middle.mass=2

for a in [giant, dwarf,middle]:
  a.orbit = curve(color=a.color, radius = 0.01)

dt = 0.02
G = 1 
while 1:
  rate(100)

  dist = dwarf.pos - giant.pos
  force = G * giant.mass * dwarf.mass * dist / mag(dist)**3
  ## leapfrog method
  giant.p = giant.p + force*dt
  dwarf.p = dwarf.p - force*dt
  middle.pos=(giant.pos+dwarf.pos)/2
  for a in [giant, dwarf, middle]:
    a.pos = a.pos + a.p/a.mass * dt
    a.orbit.append(pos=a.pos)