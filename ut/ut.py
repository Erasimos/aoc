import os

def read_file(file):
    f = open(file, 'r')
    content = f.read().splitlines()
    f.close()
    return content


def read_file_raw(file):
    f = open(file, 'r')
    content = f.read()
    f.close()
    return content


def print_answer(day, part, answer):
    print('The answer to day: ', day, ' part ', part, ' is: ', answer)
    

class Vec2D:


    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        if isinstance(other, Vec2D):
            return Vec2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vec2D):
            return Vec2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vec2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))


    def __lt__(self, other): 
        if isinstance(other, Vec2D):
            return (self.x + self.y) < (other.x + other.y)
        return NotImplemented
    

    def __neg__(self):
        """Negates the x and y values"""
        if isinstance(self, Vec2D):
            return Vec2D(-self.x, -self.y)
        return NotImplemented
    
    def neighbors(self):
        return [self + neighbor_dir for neighbor_dir in NEIGHBORS_2D]


def manhattan(v1: Vec2D, v2: Vec2D):
    return abs(v1.x - v2.x) + abs(v1.y - v2.y)


UDLR = [Vec2D(1, 0), Vec2D(-1, 0), Vec2D(0, 1), Vec2D(0, -1)]
NEIGHBORS_2D = [Vec2D(1, 0), Vec2D(-1, 0), Vec2D(0, 1), Vec2D(0, -1), Vec2D(1, 1), Vec2D(1, -1), Vec2D(-1, 1), Vec2D(-1, -1)]

ZERO_POS = Vec2D(0, 0)
RIGHT = Vec2D(1, 0)
LEFT = Vec2D(-1, 0)
UP = Vec2D(0, -1)
DOWN = Vec2D(0, 1)







