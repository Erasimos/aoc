import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)
from math import inf
from ut.common import Vec2D, Vec2DMap, read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'
def get_input():
    
    puzzle_input = read_file(puzzle_input_path)
    antenna_map = {}

    map_size = {}

    max_x = -inf
    min_x = inf
    max_y = -inf
    min_y = inf

    for y, line in enumerate(puzzle_input):
        for x, el in enumerate(line):
            if not el == '.':
                antenna_map.setdefault(el, []).append(Vec2D(x, y))         
            
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            max_y = max(max_y, y)
            min_y = min(min_y, y)

    map_size['max_x'] = max_x
    map_size['min_x'] = min_x
    map_size['max_y'] = max_y
    map_size['min_y'] = min_y

    return antenna_map, map_size


def get_antinode(pos_1: Vec2D, pos_2: Vec2D):

    dir = pos_2 - pos_1
    antinode_1 = pos_1 - dir
    antinode_2 = pos_2 + dir
    return antinode_1, antinode_2

def out_of_bounds(pos: Vec2D, map_size: dict):

    if pos.x < map_size.get('min_x'): return True
    if pos.x > map_size.get('max_x'): return True
    if pos.y < map_size.get('min_y'): return True
    if pos.y > map_size.get('max_y'): return True

    return False

def get_antinode_map(antenna_map: dict, map_size: dict):

    antinode_map = {}


    for freq, freq_positions in antenna_map.items():
        
        for i, pos_1 in enumerate(freq_positions):
            for pos_2 in freq_positions[i+1:]:

                antinode_1, antinode_2 = get_antinode(pos_1=pos_1, pos_2=pos_2)

                if not out_of_bounds(pos=antinode_1, map_size=map_size):
                    antinode_map[antinode_1] = freq
                if not out_of_bounds(pos=antinode_2, map_size=map_size):
                    antinode_map[antinode_2] = freq
    return antinode_map


def get_antinode_map_2(antenna_map: dict, map_size: dict):

    antinode_map = {}


    for freq, freq_positions in antenna_map.items():
        
        for i, pos_1 in enumerate(freq_positions):
            for pos_2 in freq_positions[i+1:]:

                # direction 1
                dir = pos_2 - pos_1
                factor = 0
                while True:
                    
                    antinode = pos_1 - (factor * dir)

                    if out_of_bounds(pos=antinode, map_size=map_size):
                        break
                    else:
                        antinode_map[antinode] = freq
                        factor += 1

                # direction 2
                factor = 0
                while True:
                    antinode = pos_2 + (factor * dir)

                    if out_of_bounds(pos=antinode, map_size=map_size):
                        break
                    else:
                        antinode_map[antinode] = freq
                        factor += 1

    return antinode_map


def part_one():

    antenna_map, map_size = get_input()
    antinode_map = get_antinode_map(antenna_map=antenna_map, map_size=map_size)
    answer = len(antinode_map.keys())
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    antenna_map, map_size = get_input()
    antinode_map = get_antinode_map_2(antenna_map=antenna_map, map_size=map_size)
    answer = len(antinode_map.keys())
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