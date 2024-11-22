import os
import sys
import re
import time
import math
from typing import List
from pathlib import Path
from copy import deepcopy
sys.path.insert(0, os.path.join(os.getcwd(), 'ut'))
from ut.day import Day
from ut.constants import Colors
from ut.common import Vec2D, read_file_raw, print_answer

from ut.simulation_state import SimulationState
simulation_state = SimulationState()

day_nr = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_nr}.txt'


turn_map = {
    'R': {
        Vec2D(0, -1): Vec2D(1, 0),
        Vec2D(1, 0): Vec2D(0, 1),
        Vec2D(0, 1): Vec2D(-1, 0),
        Vec2D(-1, 0): Vec2D(0, -1)
        },
    'L': {
        Vec2D(0, -1): Vec2D(-1, 0),
        Vec2D(-1, 0): Vec2D(0, 1),
        Vec2D(0, 1): Vec2D(1, 0),
        Vec2D(1, 0): Vec2D(0, -1)
        }
}

turn_value = {
    Vec2D(1, 0): 0,
    Vec2D(0, 1): 1,
    Vec2D(-1, 0): 2,
    Vec2D(0, -1): 3,
}


def get_input():
    raw_maze, raw_instructions = read_file_raw(puzzle_input_path).split('\n\n')
    pattern = r'\d+|[A-Za-z]'
    instructions = re.findall(pattern, raw_instructions)
    instructions = [int(x) if x.isdigit() else x for x in instructions]
    maze = {}

    start_pos = None
    y_min = math.inf
    x_min = math.inf

    for y, line in enumerate((raw_maze.splitlines())):
        for x, tile in enumerate(line):
            maze[Vec2D(x, y)] = tile

            if tile == '.' and y <= y_min:
                y_min = y
                if x < x_min:
                    x_min = x
                    start_pos = Vec2D(x, y)

    return maze, instructions, start_pos


def looparound_maze(maze: dict[Vec2D, str], pos: Vec2D, direction: Vec2D) -> Vec2D:

    new_pos = pos
    while not maze.get(new_pos, ' ') == ' ':
        new_pos = new_pos - direction
    return new_pos + direction


def step_maze(maze: dict[Vec2D, str], pos: Vec2D,  direction: Vec2D) -> Vec2D:
    new_pos = pos + direction
    new_tile = maze.get(new_pos, ' ')

    match new_tile:
        case '.':
            return new_pos
        case ' ':
            new_pos = looparound_maze(maze=maze, pos=pos, direction=direction)
            if maze.get(new_pos, ' ') == '#': return None
            else: return new_pos
        case '#':
            return None

def traverse_maze(maze: dict[Vec2D, str], instructions: List[dict], start_pos: Vec2D, start_direction: Vec2D):
    
    walked_path = deepcopy(maze)

    current_direction = start_direction
    current_pos = start_pos

    for instruction in instructions:

        #time.sleep(0.01)

        match instruction:
            case 'L':
                current_direction = turn_map['L'][current_direction]
            case 'R':
                current_direction = turn_map['R'][current_direction]
            case _:
                for _ in range(instruction):
                    new_pos = step_maze(maze=maze, pos=current_pos, direction=current_direction)
                    if new_pos:
                        current_pos = new_pos
                        walked_path[current_pos] = 'x'
                    else:
                        break

        simulation_state.state = walked_path

    return current_pos, current_direction


def get_password(pos: Vec2D, direction: Vec2D):
    t1 = 1000 * (pos.y + 1)
    t2 = 4 * (pos.x + 1)
    t3 = turn_value[direction]
    return t1 + t2 + t3

def part_one():

    maze, instructions, start_pos = get_input()
    end_pos, end_direction = traverse_maze(maze=maze, instructions=instructions, start_pos=start_pos, start_direction=Vec2D(1, 0))
    answer = get_password(pos=end_pos, direction=end_direction)
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    print_answer(part=2, day=day_nr, answer=answer)


pixel_map = {'#': Colors.GRAY, 
             '': Colors.WHITE, 
             '.': Colors.GREEN, 
             ' ': Colors.WHITE,
             'x': Colors.RED
}

day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
day.run()

