'''
    integrator: 
        class: GUI
'''

import numpy as np
from numpy import sin, cos, tan, log, exp, pi
import matplotlib.pyplot as plt
import matplotlib.gridspec as grsp
import matplotlib.widgets as widgets
import scipy.integrate as spi

class GUI:
    '''
        GUI - class
        Graphical user interface 
        
        Plot and integral of funcstring in [a, b]
        using N points in trapezoid or simpson as method
    '''
    
    def __init__(self, funcstring='cos(x)', a='0', b='pi', N=50):

        self.a = a
        self.b = b
        self.N = N
        self.metodo = 'trapezoid'
        self.funcstring = funcstring
        
        # creating function to be integrated
        self.func = lambda x: eval(self.funcstring)
        
        self.create_gui()
        
    def create_gui(self):

        # creating fig:
        self.fig = plt.figure(figsize=(12, 8))

        # using GridSpec to create panels (subplots)
        gs = grsp.GridSpec(8, 12, self.fig)

        # plot panel
        self.axplot = self.fig.add_subplot(gs[:-2, :])
        self.axplot.set_xlabel('x')
        self.axplot.set_ylabel('$f(x)$')

        # x and y axes
        self.axplot.axhline(0, color='k')
        self.axplot.axvline(0, color='k')

        # function plot 
        self.func_plot, = self.axplot.plot([], [])
        
        # auxiliary vertical lines at integration limits
        self.a_line, = self.axplot.plot([], [], color='r')
        self.b_line, = self.axplot.plot([], [], color='r')
        
        ### Controls (widgets)
        
        # TextBox for f(x)
        ax_f = self.fig.add_subplot(gs[-2, :])
        self.f_box = widgets.TextBox(ax_f, label='f(x)=', initial=self.funcstring)
        self.f_box.on_submit(self.update)

        # TextBox for a
        ax_a = self.fig.add_subplot(gs[-1, 0:2])
        self.a_box = widgets.TextBox(ax_a, label='a=', initial=f'{self.a}')
        self.a_box.on_submit(self.update)

        # TextBox for b
        ax_b = self.fig.add_subplot(gs[-1, 2:4])
        self.b_box = widgets.TextBox(ax_b, label='b=', initial=f'{self.b}')
        self.b_box.on_submit(self.update)

        # Slider for N
        ax_N = self.fig.add_subplot(gs[-1, 4:6])
        self.N_box = widgets.Slider(ax_N, label='N=', valinit=self.N, valmin=10, valmax=500, valstep=10, valfmt='%3d')
        self.N_box.on_changed(self.update)

        # RadioButtons for integration method
        ax_metodo = self.fig.add_subplot(gs[-1, 6])
        ax_metodo.set_aspect('equal')
        ax_metodo.axis('off')
        self.metodos = widgets.RadioButtons(ax_metodo, labels=['trapezoid', 'simpson'])
        self.metodos.on_clicked(self.update)

        # Panel for integral value
        ax_integral = self.fig.add_subplot(gs[-1, 7:])
        ax_integral.axis('off')
        self.integral_string = ax_integral.text(.5, .5, '', fontsize=15, horizontalalignment='center', verticalalignment='center', transform=ax_integral.transAxes)

        # populating widgets and plots:
        self.update(0)

        # showing window
        plt.tight_layout()
        plt.show()
    
    def update(self, event):
        '''
            function that will be called whenever the user interacts with the widgets
        '''
        
        self.funcstring = self.f_box.text
        self.func = lambda x: eval(self.funcstring)

        self.a = eval(self.a_box.text)
        self.b = eval(self.b_box.text)
        self.N = self.N_box.val
        
        x, y = self.create_arrays()
        
        self.axplot.set_xlim(self.a - (self.b-self.a)/20, self.b + (self.b-self.a)/20)
        self.axplot.set_ylim(y.min() - (y.max()-y.min())/20, y.max() + (y.max()-y.min())/20)
       
        self.a_line.set_data([self.a, self.a], [0, self.func(self.a)])
        self.b_line.set_data([self.b, self.b], [0, self.func(self.b)])

        self.func_plot.set_data(x, y)

        self.metodo = self.metodos.value_selected
        self.area = self.integral(x, y)
            
        self.integral_string.set_text(f'$\int_a^b f(x) dx = {self.area}$')
        
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def create_arrays(self):
        '''
            create x and y=f(x) arrays based on a, b, N
        '''
        
        x = np.linspace(self.a, self.b, self.N + 1)
        y = self.func(x)
        
        return x, y
    
    def integral(self, x, y):
        '''
            Integration using methods found in scipy.integrate
        '''

        if self.metodo == 'trapezoid':
            return spi.trapezoid(y, x)
        elif self.metodo == 'simpson':
            return spi.simpson(y, x)
        else:
            print('Método desconhecido')
            raise
