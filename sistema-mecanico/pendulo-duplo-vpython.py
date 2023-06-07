import numpy as np
import vpython as vp
import physics

# criando o objeto
pendulos = physics.DoublePendulum()

# resolvendo as EDOS
ti, tf, dt = 0, 120, 0.01
t, x1, y1, x2, y2 = pendulos.solve(tmin=ti, dt=dt, tmax=tf)

# criando a cena em vpython
vp.scene.width = vp.scene.height = 500
vp.scene.background = vp.color.white

ball1 = vp.sphere(pos=vp.vector(x1[0], y1[0], 0), radius=0.05, color=vp.color.blue)
ball2 = vp.sphere(pos=vp.vector(x2[0], y2[0], 0), radius=0.05, color=vp.color.green)

rod1 = vp.cylinder(pos=vp.vector(0, 0, 0), axis=ball1.pos, radius=.02)
rod2 = vp.cylinder(pos=ball1.pos, axis=ball2.pos - ball1.pos, radius=.02)

peg = vp.box(pos=vp.vector(0, 0, 0), length=.1, height=.1, width=.1, color=vp.color.red) 

n = 1
while True:
    vp.rate(1 / dt)
    ball1.pos = vp.vector(x1[n], y1[n], 0)
    ball2.pos = vp.vector(x2[n], y2[n], 0)
    rod1.axis = ball1.pos
    rod2.pos = ball1.pos
    rod2.axis = ball2.pos - ball1.pos
    n = (n + 1) % t.size
