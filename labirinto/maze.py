import generate_maze

class maze:
    
    '''
        Mark and solve a maze
    '''
    
    def __init__(self, nx, ny, mouse=(0, 1), cheese=(-2, -1)):
        '''
            Init: creates a maze, mark and solve it
            
            self.maze: generated maze
            self.marked: marked maze
            self.solved: maze with solved path highlighted
        '''
        
        self.maze = generate_maze.create(nx, ny, ix=mouse[0], iy=mouse[1]-1, cheese=cheese)

        self.H, self.W = self.maze.shape  # Height and Width of maze
        self.marked = self.maze.copy()
        
        cheese_full = (self.H + cheese[0], self.W + cheese[1])

        self.mark(cheese_full)
        self.path = []
        self.find_path(mouse)
        self.trace_path(self.path)

    def neighbors(self, pos):
        '''
            returns the valid neighbors of a position in maze
            to be complemented by mark_neighbors()
        '''
        x, y = pos
        
        s = (x-1, y)  # posição superior
        i = (x+1, y)  # posição inferior
        e = (x, y-1)  # posição esquerda
        d = (x, y+1)  # posição direita
        P = [s, i, e, d]
        P = [p for p in P if p[0] >= 0 and p[0] < self.H and p[1] >= 0 and p[1] < self.W]
        return P

    def mark_neighbors(self, pos):
        '''
            completes the list of valid neighbors,
            which are those equal to zero or a 
            value higher than maze[pos].
            retorns the list of neighbors to be marked
        '''
        
        P = self.neighbors(pos)
        P = [p for p in P if self.marked[p] == 0 or self.marked[p] > self.marked[pos]]
        return P

    def mark(self, pos, k=1):
        '''
            mark the maze, starting as pos position
        '''
        self.marked[pos] = k
        viz = self.mark_neighbors(pos)
        for v in viz:
            self.mark(v, k+1)

    def find_path(self, pos):
        '''
            finds the path from mouse to cheese
            in a previously marked maze
        '''
        self.path.append(pos)
        k = self.marked[pos]
        neigh = self.neighbors(pos)
        move_to = [v for v in neigh if self.marked[v] == k-1]
        if len(move_to):
            self.find_path(move_to[0])

    def trace_path(self, path):

        self.solved = self.maze.copy()
        
        #including path in maze:
        for pos in path:
            self.solved[pos] = 1
