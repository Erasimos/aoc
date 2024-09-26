import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from constants import Colors
from day import Day

day_nr = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_nr}.txt'


def get_input():
    puzzle_input = ut.read_file(puzzle_input_path)


def part_one():

    input = get_input()

    answer = 0

    ut.print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    ut.print_answer(part=2, day=day_nr, answer=answer)


pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
day.run()


