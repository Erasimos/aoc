import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

import ut
import math
from ut.day import Day
from ut.constants import Colors
from ut.common import Vec2D, read_file, print_answer

from ut.simulation_state import SimulationState
simulation_state = SimulationState()

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'


def get_input():
    puzzle_input = read_file(puzzle_input_path)
    left_list = []
    right_list = []
    for line in puzzle_input:
        split_el = line.split()
        left_list.append(int(split_el[0]))
        right_list.append(int(split_el[1]))
    return left_list, right_list


def get_similarity_score(left_list: list, right_list: list):
    similarity_score = 0
    for val in left_list:
        similarity_score += val * right_list.count(val)
    return similarity_score

def part_one():

    left_list, right_list = get_input()
    left_list.sort()
    right_list.sort()
    paired_list = list(zip(left_list, right_list))
    answer = sum([abs(right_val - left_val) for left_val, right_val in paired_list])
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    left_list, right_list = get_input()
    answer = get_similarity_score(left_list=left_list, right_list=right_list)
    print_answer(part=2, day=day_nr, answer=answer)


def run_day():
    pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
    day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
    day.run()


part_one()
part_two()

# run_day()