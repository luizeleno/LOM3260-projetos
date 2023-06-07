'''

    Create a Graphical User Interface (GUI)
    to access the maze solution

'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec
import matplotlib.widgets
import maze

class MAZEGUI:
    
    def __init__(self, nx=25, ny=25, mouse=(0, 1), cheese=(-2, -1), slow=False):
        '''
            GUI to visualize the maze, ans also its marking and solution
            
            nx, ny: width and height of maze
            mouse, cheese: maze entrance and exit 
            
            if slow == True, prints marking and solution progressively
        '''
        
        # creat a starting maze
        self.nx, self.ny = nx, ny
        self.mouse = mouse
        self.cheese = cheese
        self.Maze = maze.maze(nx, ny, self.mouse, self.cheese)
        
        self.slow = slow
        
        self.create_GUI()

    def generate(self, event):
        # generates and shows a new maze
        self.Maze = maze.maze(self.nx, self.ny, self.mouse, self.cheese)
        self.Maze_plot.set_array(self.Maze.maze)
        self.Maze_plot.set_cmap('gray')
        self.Maze_plot.set_clim(vmin=-1, vmax=0)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def mark(self, event):
        # marking the maze
        self.Maze_plot.set_array(self.Maze.maze)
        self.Maze_plot.set_clim(vmin=-1, vmax=self.Maze.marked.max())
        self.Maze_plot.set_cmap('turbo')
        if self.slow:
            c = self.Maze.maze.copy()
            for k in range(self.Maze.marked.max()):
                c[self.Maze.marked == k] = k
                self.Maze_plot.set_array(c)
                self.fig.canvas.draw()
                self.fig.canvas.flush_events()
        else:
            self.Maze_plot.set_array(self.Maze.marked)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

    def path(self, event):
        # tracing the solution path
        self.Maze_plot.set_cmap('gray')
        self.Maze_plot.set_array(self.Maze.maze)
        self.Maze_plot.set_clim(vmin=-1, vmax=1)
        if self.slow:
            c = self.Maze.maze.copy()
            for pos in self.Maze.path:
                c[pos] = 1
                self.Maze_plot.set_array(c)
                self.fig.canvas.draw()
                self.fig.canvas.flush_events()
        else:
            self.Maze_plot.set_array(self.Maze.solved)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

    def erase(self, event):
        # erasing path / markings, leaving only the maze
        self.Maze_plot.set_cmap('gray')
        self.Maze_plot.set_array(self.Maze.maze)
        self.Maze_plot.set_clim(vmin=-1, vmax=0)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def create_GUI(self):
        '''
            Creating the GUI
        '''

        self.fig = plt.figure(figsize=(7, 8), constrained_layout=True)

        gs = matplotlib.gridspec.GridSpec(10, 4, self.fig)

        # Creating the initial maze plot
        ax = self.fig.add_subplot(gs[:-1, :])
        ax.axis('off')
        self.Maze_plot = ax.imshow(self.Maze.maze, cmap='gray')

        # Controls (widgets)
        axgera = self.fig.add_subplot(gs[-1, 0])
        buttongera = matplotlib.widgets.Button(axgera, label='Generate', color='gold')
        buttongera.on_clicked(self.generate)

        axmarca = self.fig.add_subplot(gs[-1, 1])
        buttonmarca = matplotlib.widgets.Button(axmarca, label='Mark spaces', color='bisque')
        buttonmarca.on_clicked(self.mark)

        axsolve = self.fig.add_subplot(gs[-1, 2])
        buttonsolve = matplotlib.widgets.Button(axsolve, label='Solve', color='turquoise')
        buttonsolve.on_clicked(self.path)

        axapaga = self.fig.add_subplot(gs[-1, 3])
        buttonapaga = matplotlib.widgets.Button(axapaga, label='Erase', color='thistle')
        buttonapaga.on_clicked(self.erase)

        plt.show()
