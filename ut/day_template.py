import os
import sys
from pathlib import Path
sys.path.insert(0, os.path.join(os.getcwd(), 'ut'))
from ut.day import Day
from ut.constants import Colors
from ut.common import Vec2D, read_file, print_answer

from ut.simulation_state import SimulationState
simulation_state = SimulationState()

day_nr = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_nr}.txt'

day_nr = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_nr}.txt'


def get_input():
    puzzle_input = read_file(puzzle_input_path)


def part_one():

    input = get_input()

    answer = 0

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    print_answer(part=2, day=day_nr, answer=answer)


def run_day():
    pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
    day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
    day.run()


part_one()
part_two()

# run_day()