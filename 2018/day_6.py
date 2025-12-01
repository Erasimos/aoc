import os
import sys
import math
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

def get_input():
    coordinates = []
    for line in read_file(puzzle_input_path):
        x, y = line.split(', ')
        coordinates.append(Vec2D(int(x), int(y)))
    return coordinates

def get_boundary(coordinates):
    min_x = math.inf
    min_y = math.inf
    max_x = -math.inf
    max_y = -math.inf
    
    for c in coordinates:
        x = c.x
        y = c.y
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    return min_x, max_x, min_y, max_y

def get_closests(p1: Vec2D, coordinates):
    distance = math.inf
    closests = []
    for c in coordinates:
        m_dist = p1.manhattan(c)
        if m_dist < distance:
            closests = [c]
            distance = m_dist
        elif m_dist == distance:
            closests.append(c)
    return closests

def get_areas(coordinates):
    areas = {}

    min_x, max_x, min_y, max_y = get_boundary(coordinates)
    
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            closests = get_closests(Vec2D(x, y), coordinates)
            if len(closests) == 1:
                c = closests[0]
                areas[c] = areas.get(c, 0) + 1
                if x in [min_x, max_x] or y in [min_y, max_y]:
                    areas[c] = math.inf
    return areas

def part_one():

    coordinates = get_input()
    areas = get_areas(coordinates)
    answer = -math.inf
    for p, area in areas.items():
        if not area == math.inf and area > answer:
            answer = area 
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
#part_two()