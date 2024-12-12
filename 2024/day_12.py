import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, read_file, print_answer, UDLR

import heapq

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'


def get_input():
    puzzle_input = read_file(puzzle_input_path)
    garden = {Vec2D(x, y): el for y, line in enumerate(puzzle_input) for x, el in enumerate(line)}
    return garden

def get_cost(regions: dict):
    pass

def get_edge_count(pos: Vec2D, garden: dict):

    count = 0
    tile = garden.get(pos, None)
    for direction in UDLR:
        neighbour_pos = pos + direction
        if not garden.get(neighbour_pos, '') == tile:
            count += 1
    return count

def is_corner_pos(garden: dict, pos: Vec2D):
    
    plant_type = garden.get(pos, None)

    down_pos = pos + Vec2D(0, 1)
    up_pos = pos + Vec2D(0, -1)
    left_pos = pos + Vec2D(-1, 0)
    right_pos = pos + Vec2D(1, 0)

    down_type = garden.get(down_pos, '')
    up_type = garden.get(up_pos, '')
    left_type = garden.get(left_pos, '')
    right_type = garden.get(right_pos, '')

    # Top left corner
    if 

    # Top right corner

    # Bottom left corner

    # Bottom righ corner

def get_sides(garden: dict, region: dict):
    sides = 0
    for pos in region.get('positions', []):
        if is_corner_pos(garden=garden, pos=pos):
            sides += 1

def get_regions(garden: dict):
    regions = []
    visited = {}
    
    for pos, region_name in garden.items():
        if visited.get(pos, False):
            continue
        else:

            plant_type = region_name
            new_region = {'plant': plant_type, 'area': 0, 'perimeter': 0, 'sides': 0, 'positions': []}
            area = 0
            perimeter = 0
            positions = []
            q = [pos]
            while q:
                current_pos = heapq.heappop(q)
                if visited.get(current_pos, False):
                    continue
                if garden.get(current_pos, '') == plant_type:
                    visited[current_pos] = True
                    area += 1
                    positions.append(current_pos)
                    perimeter += get_edge_count(pos=current_pos, garden=garden)
                    for direction in UDLR:
                        neighbour_pos = current_pos + direction
                        if not visited.get(neighbour_pos, False):
                            heapq.heappush(q, current_pos + direction)
            new_region['area'] = area
            new_region['perimeter'] = perimeter
            new_region['positions'] = positions
            new_region['sides'] = get_sides(garden=garden, region=new_region)
            regions.append(new_region)
                

    return regions
    
def get_cost_2(regions: dict):
    return sum([region.get('area', 0) * region.get('sides', 0) for region in regions])

def get_cost(regions: dict):
    return sum([region.get('area', 0) * region.get('perimeter', 0) for region in regions])

def part_one():

    garden = get_input()
    regions = get_regions(garden=garden)
    answer = get_cost(regions=regions)

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    garden = get_input()
    regions = get_regions(garden=garden)
    answer = get_cost_2(regions=regions)
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
#part_two()