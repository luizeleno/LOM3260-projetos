import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as anim
import physics

# criando o objeto
pendulos = physics.DoublePendulum()

# resolvendo as EDOS
t, x1, y1, x2, y2 = pendulos.solve(tmin=0, dt=0.01, tmax=60, y0=[np.pi/3, 0, np.pi/2, 0])

L = pendulos.L

# Gráfico
fig = plt.figure()
ax = plt.axes(xlim=(-L, L), ylim=(-L, L), aspect='equal')
pendulo, = ax.plot([], [], 'bo-')
pendulo_trilha, = ax.plot([], [], 'r--')
tempo = ax.text(0.8, 0.95, '', transform=ax.transAxes)

# função de animação
def updatefig(n):
    pendulo.set_data([0, x1[n], x2[n]], [0, y1[n], y2[n]])
    pendulo_trilha.set_data(x2[:n], y2[:n])
    tempo.set_text(f't={t[n]:.2f} s')
    return pendulo, pendulo_trilha, tempo

a = anim(fig, updatefig, frames=t.size, blit=True, interval=5)
plt.show()
