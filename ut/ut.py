import os
import math
import pyperclip

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
    pyperclip.copy(answer)
    print('The answer to day: ', day, ' part ', part, ' is: ', answer)


def print_dict_map(dict_map: dict):

    min_x = int(min([pos.x for pos in dict_map.keys()]))
    max_x = int(max([pos.x for pos in dict_map.keys()]))
    min_y = int(min([pos.y for pos in dict_map.keys()]))
    max_y = int(max([pos.y for pos in dict_map.keys()]))

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if dict_map.get(Vec2D(x, y), False):
                print('#', end='')
            else:
                print('.', end='')
        print()

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
        return Vec2D(-self.x, -self.y)
    
    def clamp(self):
        self.x = 0 if self.x == 0 else math.copysign(1, self.x)
        self.y = 0 if self.y == 0 else math.copysign(1, self.y)
        return self

    def neighbors_orthogonal(self):
        return [self + neighbor_dir for neighbor_dir in UDLR]


    def neighbors(self):
        return [self + neighbor_dir for neighbor_dir in NEIGHBORS_2D]


def manhattan(v1: Vec2D, v2: Vec2D):
    return abs(v1.x - v2.x) + abs(v1.y - v2.y)


UDLR = [Vec2D(1, 0), Vec2D(-1, 0), Vec2D(0, 1), Vec2D(0, -1)]
UDLR_MAP = {'U': Vec2D(0, -1), 'D': Vec2D(0, 1), 'R': Vec2D(1, 0), 'L': Vec2D(-1, 0)}
NEIGHBORS_2D = [Vec2D(1, 0), Vec2D(-1, 0), Vec2D(0, 1), Vec2D(0, -1), Vec2D(1, 1), Vec2D(1, -1), Vec2D(-1, 1), Vec2D(-1, -1)]

ZERO_POS = Vec2D(0, 0)
RIGHT = Vec2D(1, 0)
LEFT = Vec2D(-1, 0)
UP = Vec2D(0, -1)
DOWN = Vec2D(0, 1)
