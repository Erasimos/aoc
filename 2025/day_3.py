import os
import sys
import math
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

def get_input():
    return [[int(el) for el in line] for line in read_file(puzzle_input_path)]

def get_highest_with_index(l):
    highest = -math.inf
    highest_index = None
    for index, val in enumerate(l):
        if val > highest:
            highest = val
            highest_index = index
    return highest, highest_index

def get_largest_joltage(bank, size):
    joltage = ''
    jolt_size = size
    index = 0
    for i in range(size):
        jolt_cut = -jolt_size + 1
        if jolt_cut < 0:
            val, new_index = get_highest_with_index(bank[(index):-jolt_size+1])
        else:
            val, new_index = get_highest_with_index(bank[(index):])
        joltage += str(val)
        index += new_index + 1
        jolt_size -= 1
    return int(joltage)

def part_one():
    banks = get_input()
    answer = sum([get_largest_joltage(bank, 2) for bank in banks])
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():
    banks = get_input()    
    answer = sum([get_largest_joltage(bank, 12) for bank in banks])
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()