import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as mwidgets
import matplotlib.gridspec as mpg

class GUI:
    '''
        Graphical user interface to visualize and explore the Mandelbrot Fractal

        Parameters:
        1. N: create a NxN mesh in the complex plane (default: 750)
        2. NITERMAX: maximum number of steps before deciding if a point belongs to the fractal or not (default: 250)
        3. xlim: initial real axis limits (default: (-2, .5))
        4. ylim: initial imaginary axis limits (default: (-1.5, 1.5))
    '''

    def __init__(self, N=750, NITERMAX=250, xlim=(-2, .5), ylim=(-1.5, 1.5)):
        self.N = N
        self.NITERMAX = NITERMAX
        self.xlim, self.ylim = xlim, ylim
        self.xlim0, self.ylim0 = xlim, ylim  # original limits
        self.history = []  # previous plot limits

        self.mandelbrot()
        self.create()

    def mandelbrot(self):

        self.mandel = np.zeros((self.N, self.N))
        x = np.linspace(*self.xlim, self.N)
        y = np.linspace(*self.ylim, self.N)
        zx, zy = np.meshgrid(x, y)
        z = zx + zy * 1j

        # Mandelbrot set: $z \in C$ such that  $|c_n^2 + z|$ < 2 for $n \to \infty$ and $c_0 = 0$

        c = np.zeros_like(self.mandel) * 1j
        still_in_set = np.where(self.mandel < 2)
        for i in range(self.NITERMAX):  # TODO: would it be possible to vectorize this loop?
            c[still_in_set] = c[still_in_set] * c[still_in_set] + z[still_in_set]
            still_in_set = np.where(np.absolute(c) < 2)
            self.mandel[still_in_set] += 1

    def onselect(self, eclick, erelease):
        self.history.append((self.xlim, self.ylim))
        self.xlim = (eclick.xdata, erelease.xdata)
        self.ylim = (eclick.ydata, erelease.ydata)
        self.mandelbrot()
        self.plot()
    
    def plot(self):
        self.graph.set_array(self.mandel)
        self.graph.set_extent((*self.xlim, *self.ylim))

    def reset(self, event):
        self.history = []
        self.xlim, self.ylim = self.xlim0, self.ylim0
        self.mandelbrot()
        self.plot()

    def back(self, event):
        try:
            self.xlim, self.ylim = self.history.pop()
        except:
            pass  # history is already empty
        self.mandelbrot()
        self.plot()

    def create(self):
        '''
            Create Graphical Window
        '''

        fig = plt.figure(figsize=(12, 8), constrained_layout=True)
        gs = mpg.GridSpec(8, 12, figure=fig)

        self.ax = fig.add_subplot(gs[:-1, :])
        self.ax.set_xlabel(f'$\Re(c)$')
        self.ax.set_ylabel(f'$\Im(c)$')
        props = {'facecolor':'pink', 'alpha':0.5}
        rect = mwidgets.RectangleSelector(self.ax, self.onselect, interactive=False, props=props)

        self.graph = self.ax.imshow(self.mandel, origin='lower', cmap='turbo', extent=(*self.xlim, *self.ylim), aspect='equal', vmin=0, vmax=self.NITERMAX)

        axr = fig.add_subplot(gs[-1, :6])
        reset = mwidgets.Button(axr, label='Restart')
        reset.on_clicked(self.reset)

        axu = fig.add_subplot(gs[-1, 6:])
        back = mwidgets.Button(axu, label='Back one step')
        back.on_clicked(self.back)
    
        plt.show()
