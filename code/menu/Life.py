from BaseMenuItem import BaseMenuItem
from itertools import product
from random import choice
from time import sleep
from sense_hat import SenseHat


# Code taken from here: https://github.com/bennuttall/sense-hat-examples
class Life(BaseMenuItem):
    def __init__(self, sense, width, height):
        self.sense = sense   
        self.size = (width, height)
        self.random_world()       
       
    def __str__(self):
        width, height = self.size
        return '\n'.join(
            ' '.join(
                self.draw_cell(x, y) for x in range(width)
            )
            for y in range(height)
        )

    def __iter__(self):
        return self

    def __next__(self):
       
        return self

    next = __next__

    def evolve_cell(self, cell):
        alive = cell in self.live_cells
        neighbours = self.count_neighbours(cell)
        return neighbours == 3 or (alive and neighbours == 2)

    def count_neighbours(self, cell):
        x, y = cell
        deltas = set(product([-1, 0, 1], repeat=2)) - set([(0, 0)])
        neighbours = ((x + dx, y + dy) for (dx, dy) in deltas)
        return sum(neighbour in self.live_cells for neighbour in neighbours)

    def evolve_world(self):
        width, height = self.size
        world = product(range(width), range(height))
        self.live_cells = {cell for cell in world if self.evolve_cell(cell)}

    def random_world(self):
        width, height = self.size
        world = product(range(width), range(height))
        self.live_cells = {cell for cell in world if choice([0, 1])}

    def draw_cell(self, x, y):
        cell = (x, y)
        return 'O' if cell in self.live_cells else ' '

    def get_cell_color(self, x, y):
        cell = (x, y)
        red = (255, 0, 0)
        black = (0, 0, 0)
        return red if cell in self.live_cells else black

    def update(self):
        width, height = self.size      
        for x in range(width):
            for y in range(height):
                color = self.get_cell_color(x, y)                            
                self.sense.set_pixel(x, y, color)
        
        return hash(str(self.live_cells)) # are we stable yet?

    #def different(self, col1, col2):
    #    return not (col1[0]==col2[0] and col1[1]==col2[1] and col1[2]==col2[2])

    def select(self):        
        self.random_world()         
        print "Game of Life - randomized"
        
    def deselect(self):
        pass

    def loop(self):
        self.evolve_world()
        print "Game of Life - step"
        print(self.update())
        sleep(0.2)