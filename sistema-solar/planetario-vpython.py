'''
Simulação do sistema solar
inclui os planetas e o cometa Halley
'''

import numpy as np
import datetime as dt
import vpython as vp
import ephem
import halley

# creating the list of objects to be followed, including planets and Halley's comet
objects = [ephem.Mercury(), ephem.Venus(), ephem.Sun(), ephem.Mars(), ephem.Jupiter(), ephem.Saturn(), ephem.Uranus(), ephem.Neptune(), halley.create()]

N = len(objects)  # no. of objects
now = dt.datetime.now()

def locate(obj, date, earth=False):
    '''
        Determines the position of the object at date
        Converts from ecliptic (spherical) to cartesian coordinates 
        The xy plane will be the plane of the ecliptic, with the x axis pointing to the vernal equinox
    '''
    obj.compute(date)  # using ephem .compute() method to get object coordinates
    th, ph = obj.hlat, obj.hlon

    # earth must be treated separatelly
    if obj.name == 'Sun':  # i.e., the Earth
        r = obj.earth_distance
    else:
        r = obj.sun_distance

    # converting to cartesian coordinates
    x = r * np.cos(ph) * np.cos(th)
    y = r * np.sin(ph) * np.cos(th)
    z = r * np.sin(th)
    return x, y, z

# ******************************************
# color generator
# Returns (with yield) elements from colors. After len(colors) calls, wraps and starts again from the beginning
colors = [vp.color.orange, vp.color.green, vp.color.blue, vp.color.red, vp.color.magenta, vp.color.purple, vp.color.cyan, vp.vector(0.580, 0.254, 0.788)]
def pick_color():
    n = 0
    while True:
        yield colors[n]
        n = (n + 1) % len(colors)
color = pick_color()
# ******************************************

# criando a cena em vpython
vp.scene.width = vp.scene.height = 500
vp.scene.background = vp.color.white

# sun at the center
sun= vp.sphere(pos=vp.vector(0, 0, 0), radius=0.1, color=vp.color.yellow)

# creating animated objects
balls = []  # position of objects
tracks = []  # trace of the object's orbit
for (p, i) in zip(objects, range(N)):
    x, y, z = locate(p, now)
    pos = vp.vector(x, y, z)
    c = next(color)
    balls.append(vp.sphere(pos=pos, radius=0.075, color=c))
    tr = vp.curve(pos)
    tr.radius = .02
    tr.color = c
    tr.retain = 10 * 365  # will retain only the last tr.retain positions
    tracks.append(tr)

# animation function
n = 1
while True:
    vp.rate(250)
    date = now + dt.timedelta(days=n)  # increasing date day by day
    for (p, b, t) in zip(objects, balls, tracks):  # relocating objects
        x, y, z = locate(p, date)
        b.pos = vp.vector(x, y, z)
        t.append(b.pos)
    n += 1
