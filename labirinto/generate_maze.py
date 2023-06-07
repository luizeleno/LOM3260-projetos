import re
import numpy
import df_maze

def create(nx=30, ny=30, ix=0, iy=0, cheese=(-2, -1), seed=None):
    '''
     Maze dimensions (ncols, nrows)
        nx, ny = 30, 30 (default)
    Maze entry position ("mouse")
        ix, iy = 0, 0 (default)
    '''

    newmaze = df_maze.Maze(nx, ny, ix, iy, seed)
    newmaze.make_maze()

    s = f'{newmaze}'.split('\n')
    s = convert(s)
    
    s[ix][iy+1] = 0
    s[cheese[0]][cheese[1]] = 0

    return s

def convert(maze):
    '''
        replacing symbols in original maze by 0 and -1
    '''
    for i in range(len(maze)):
        maze[i] = maze[i].replace('|', 'A')
        maze[i] = maze[i].replace('-', 'A')
        maze[i] = maze[i].replace('+', 'A')
        maze[i] = maze[i].replace(' ', ' 0 ')
        maze[i] = maze[i].replace('A', ' -1 ')
        maze[i] = [int(n) for n in re.findall('-?\d+\.?\d*', maze[i])]

    maze_array = numpy.array(maze, dtype=int)
    return maze_array
