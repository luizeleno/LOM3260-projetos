import matplotlib.pyplot as plt
import matplotlib.animation as animation
import simulation
import select_material

# **********************************************
# definindo os parâmetros das simulações

# geometria da placa
chapa = simulation.geometry(Lx=1, Ly=1, Lz=5e-3)

#inicializando a base de dados de materiais:
db = select_material.material_database('materiais.xls')

# selecionando materiais
cobre = db.select('Cobre')
ouro = db.select('Ouro')
ferro = db.select('Ferro')
bronze = db.select('Bronze')

# parâmetros do processo de estampagem
estampa = simulation.stamping(Tinitial=100, Tstamp=800, text='PYTHON', fontsize=21)

# definindo condição de resfriamento/aquecimento
conv = simulation.convection(Trefr=400, h=2000)

# **********************************************
# inicializando as simulações 

simulacao1 = simulation.DiffFin(chapa, cobre,  estampa, conv)
simulacao2 = simulation.DiffFin(chapa, ouro,    estampa, conv)
simulacao3 = simulation.DiffFin(chapa, ferro, estampa, conv)
simulacao4 = simulation.DiffFin(chapa, bronze,   estampa, conv)

# **********************************************
# Gráficos

fig = plt.figure(figsize=(7, 9), constrained_layout=True)
plt.suptitle('Resfriamento de chapas finas')

# função para criar um painel no eixo ax
def painel(simulacao, ax, titulo=''):

    ax.set_title(titulo)
    ax.set_xlabel(f'$x$ (m)')
    ax.set_ylabel(f'$y$ (m)')

    im = ax.imshow(simulacao.T, vmin=0, vmax=simulacao.stamping.Tstamp, origin='lower', cmap='turbo', extent=(0, simulacao.geometry.Lx, 0, simulacao.geometry.Ly))
    plt.colorbar(im, ax=ax, location='bottom', orientation='horizontal', label='$T$ (°C)', shrink=.75)

    return im

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

im1 = painel(simulacao1, ax1, f'{simulacao1.material.name}')
im2 = painel(simulacao2, ax2, f'{simulacao2.material.name}')
im3 = painel(simulacao3, ax3, f'{simulacao3.material.name}')
im4 = painel(simulacao4, ax4, f'{simulacao4.material.name}')

# mostrando o tempo no Painel 1
time_label = ax1.text(0, 0, f'$t = 0$ s', fontsize=16)
time_label.set_bbox(dict(facecolor='white', alpha=0.5, edgecolor='red'))

# **********************************************
# Animação

# função de animação
n = 0
def animate(i):
    global pause, n
    if not pause:
        for s, im in zip([simulacao1, simulacao2, simulacao3, simulacao4], [im1, im2, im3, im4]):
            s.evolve()
            im.set_array(s.T)
        time_label.set_text(f'$t = {n * simulacao1.dt: .2f}$ s')
        n += 1        
    return  im1, im2, im3, im4, time_label

# Função para pausar com o mouse
pause = True  # se pause=True, começa pausado
def onClick(event):
    global pause
    pause ^= True
fig.canvas.mpl_connect('button_press_event', onClick)

delay=1
anim = animation.FuncAnimation(fig, animate, interval=delay, blit=True)

plt.show()
