import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from constant import Colors
from day import Day

day = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day}.txt'


def get_input():
    puzzle_input = ut.read_file(puzzle_input_path)


def part_one():

    input = get_input()

    answer = 0

    ut.print_answer(part=1, day=day, answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    ut.print_answer(part=2, day=day, answer=answer)


pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
day.run()


