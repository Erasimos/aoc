import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

import math

from ut.day import Day
from ut.constants import Colors
from ut.common import Vec2D, read_file, print_answer

from ut.simulation_state import SimulationState
simulation_state = SimulationState()

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

def get_reports():
    return [[int(el) for el in line.split()] for line in read_file(puzzle_input_path)]

def is_safe_2(report: list):

    if is_safe(report=report): return True

    for index, _ in enumerate(report):
        if is_safe(report=report[0:index] + report[index + 1:]): return True

    return False
    
def is_safe(report: list):
    num_direction = math.copysign(1, report[0] - report[1])
    for index, val in enumerate(report[:-1]):
        step = val - report[index + 1]
        if not (math.copysign(1, step) == num_direction and abs(step) in [1,2,3]):
            return False
    return True


def part_one():

    reports = get_reports()
    answer = sum([is_safe(report) for report in reports])
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    reports = get_reports()
    answer = sum([is_safe_2(report) for report in reports])
    print_answer(part=1, day=day_nr, answer=answer)


def run_day():
    pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
    day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
    day.run()


part_one()
part_two()

# run_day()