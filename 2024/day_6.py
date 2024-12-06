import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from copy import deepcopy

from ut.common import Vec2D, Vec2DMap, read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

turn_map = {
    Vec2D(1, 0): Vec2D(0, 1),
    Vec2D(0, 1): Vec2D(-1, 0),
    Vec2D(-1, 0): Vec2D(0, -1),
    Vec2D(0, -1): Vec2D(1, 0),
}

turn_sign_map = {
    Vec2D(1, 0): '>',
    Vec2D(0, 1): 'v',
    Vec2D(-1, 0): '<',
    Vec2D(0, -1): '^',
}

def get_map():
    puzzle_input = read_file(puzzle_input_path)
    guard_map = {}
    start_pos = None
    for y, line in enumerate(puzzle_input):
        for x, el in enumerate(line):
            if el == '#':
                guard_map[Vec2D(x, y)] = el
            elif el in ['<', '>', '^', 'v']:
                start_pos = Vec2D(x, y)
                guard_map[start_pos] = el
    
    return Vec2DMap(dict_map=guard_map), start_pos

def in_bounds(guard_map: Vec2DMap, pos: Vec2D):
    return pos.x > guard_map.min_x and pos.x < guard_map.max_x and pos.y > guard_map.min_y and pos.y < guard_map.max_y

def turn(direction: Vec2D):
    return turn_map.get(direction, None)

def traverse_guard_map(guard_map: Vec2DMap, start_pos: Vec2D):

    traversed_guard_map = guard_map

    current_direction = Vec2D(0, -1)
    current_position = start_pos
    while in_bounds(guard_map=guard_map, pos=current_position):

        new_position = current_position + current_direction

        if guard_map.dict_map.get(new_position, '.') == '#':
            current_direction = turn(current_direction)
        else:
            traversed_guard_map.dict_map[new_position] = turn_sign_map.get(current_direction, '?')
            current_position = new_position
    
    return traversed_guard_map

def count_visited(guard_map: Vec2DMap):
    count = 0

    for tile in guard_map.dict_map.values():
        if tile in ['<', '>', '^', 'v']:
            count += 1        
    
    return count

def is_loop(guard_map: Vec2DMap, start_pos: Vec2D):

    loops = False

    current_direction = Vec2D(0, -1)
    visited = {start_pos: [current_direction]}
    current_position = start_pos
    while in_bounds(guard_map=guard_map, pos=current_position):

        new_position = current_position + current_direction

        if guard_map.dict_map.get(new_position, '.') == '#':
            current_direction = turn(current_direction)
        else:
            current_position = new_position
            
            if current_direction in visited.get(current_position, []):
                loops = True
                break

            visited.setdefault(current_position, []).append(current_direction)
        
    return loops

def find_loops(guard_map: Vec2DMap, start_pos: Vec2D):

    loops = 0

    print('min_x: ', guard_map.min_x)
    print('max_x: ', guard_map.max_x)
    print('min_y: ', guard_map.min_y)
    print('max_x: ', guard_map.max_y)

    for x in range(guard_map.min_x, guard_map.max_x + 1):
        for y in range(guard_map.min_y, guard_map.max_y + 1):
            obst_pos = Vec2D(x, y)
            print(obst_pos)
            if guard_map.dict_map.get(obst_pos, '.') =='.':
                new_guard_map = deepcopy(guard_map)
                new_guard_map.dict_map[obst_pos] = '#'
                if is_loop(guard_map=new_guard_map, start_pos=start_pos):
                    loops += 1
    return loops
            

def part_one():

    guard_map, start_pos = get_map()

    traversed_guard_map = traverse_guard_map(guard_map=guard_map, start_pos=start_pos)
    answer = count_visited(guard_map=traversed_guard_map)

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    guard_map, start_pos = get_map()
    answer = find_loops(guard_map=guard_map, start_pos=start_pos)
    
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()




## OPTINAL PY GAME VISUALIZATION
###
###
### ---------------------------------------------------------------
from ut.day import Day
from ut.constants import Colors
from ut.simulation_state import SimulationState
simulation_state = SimulationState()

def run_day():
    pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
    day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
    day.run()

# run_day()