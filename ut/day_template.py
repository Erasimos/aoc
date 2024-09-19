import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut


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


part_one()
part_two()