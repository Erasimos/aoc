import math
import pyperclip
from typing import List, Callable
import heapq


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
    print('The answer to day:', day, 'part', part, 'is:', answer)




class Vec2DMap:
    def __init__(self, dict_map: dict):
        self.dict_map = dict_map
    
    def print_map(self):
        x_positions = [pos.x for pos in self.dict_map.keys()]
        y_positions = [pos.y for pos in self.dict_map.keys()]
        min_x, max_x = min(x_positions), max(x_positions)
        min_y, max_y = min(y_positions), max(y_positions)

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                tile = self.dict_map.get(Vec2D(x, y), '.')
                print(tile, end='')
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
    
    def manhattan(self, other):
        if isinstance(other, Vec2D):
            return abs(self.x - other.x) + abs(self.y - other.y)
        return NotImplemented

class Vec3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"

    def __add__(self, other):
        if isinstance(other, Vec3D):
            return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vec3D):
            return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vec3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __lt__(self, other): 
        if isinstance(other, Vec3D):
            return (self.x + self.y + self.z) < (other.x + other.y + other.z)
        return NotImplemented
    
    def __neg__(self):
        """Negates the x and y values"""
        return Vec3D(-self.x, -self.y, self.z)
    
    def neighbours(self):
        return [self + direction for direction in NEIGHBORS_3D]
    
    def clamp(self):
        clamped_x = 0 if self.x == 0 else math.copysign(1, self.x)
        clamped_y = 0 if self.y == 0 else math.copysign(1, self.y)
        clamped_z = 0 if self.z == 0 else math.copysign(1, self.z) 
        return Vec3D(clamped_x, clamped_y, clamped_z)
    
    



UDLR = [Vec2D(1, 0), Vec2D(-1, 0), Vec2D(0, 1), Vec2D(0, -1)]
UDLR_MAP = {'U': Vec2D(0, -1), 'D': Vec2D(0, 1), 'R': Vec2D(1, 0), 'L': Vec2D(-1, 0)}
NEIGHBORS_2D = [Vec2D(1, 0), Vec2D(-1, 0), Vec2D(0, 1), Vec2D(0, -1), Vec2D(1, 1), Vec2D(1, -1), Vec2D(-1, 1), Vec2D(-1, -1)]
NEIGHBORS_3D = [Vec3D(0, 0, 1), Vec3D(0, 0, -1), Vec3D(0, 1, 0), Vec3D(0, -1, 0), Vec3D(1, 0, 0), Vec3D(-1, 0, 0)]

ZERO_POS = Vec2D(0, 0)
RIGHT = Vec2D(1, 0)
LEFT = Vec2D(-1, 0)
UP = Vec2D(0, -1)
DOWN = Vec2D(0, 1)

def dijsktra(graph: dict, get_neighbours: Callable, start: Vec2D, goal: Vec2D):

    # distance from start, node
    q = [(0, start)]
    distances = {start: 0}
    
    while q:

        current_distance, current_node = heapq.heappop(q)

        if current_node == goal:
            return current_distance
        
    
        neighbors = get_neighbours(graph=graph, pos=current_node)

        for neighbor in neighbors:
            new_distance = current_distance + 1

            if new_distance < distances.get(neighbor, math.inf):
                distances[neighbor] = new_distance
                heapq.heappush(q, (new_distance, neighbor))

    return math.inf


def insert_sort(list: List, compare: Callable):
    sorted_list = []

    for el in list:

        for i, sorted_el in enumerate(sorted_list):
            if compare(el, sorted_el):
                sorted_list.insert(i, el)
                break
        else:
            sorted_list.append(el)

    return sorted_list
