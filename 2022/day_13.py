import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from typing import List
from functools import reduce

day = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day}.txt'


def get_data_pairs():
    puzzle_input = ut.read_file_raw(puzzle_input_path)
    return [[eval(line) for line in chunk.split()] for chunk in puzzle_input.split('\n\n')]


def get_all_packets():
    return [eval(line) for line in ut.read_file(puzzle_input_path) if not line == '']


def compare(left, right):
    
    if isinstance(left, int) and isinstance(right, int):
        if left < right: return True
        elif left == right: return None
        elif left > right: return False

    new_left = left if isinstance(left, List) else [left]
    new_right = right if isinstance(right, List) else [right]

    for i, l_val in enumerate(new_left):
        try: r_val = new_right[i]
        except: return False
        match compare(l_val, r_val):
            case True: return True
            case False: return False
            case None: continue

    if len(new_left) == len(new_right): return None
    else: return True


def part_one():

    data_pairs = get_data_pairs()
    answer = sum([compare(left, right) * (i + 1) for i, (left, right) in enumerate(data_pairs)])
    ut.print_answer(part=1, day=day, answer=answer)


def part_two():

    divider_packets = [[[2]], [[6]]]
    data_packets = get_all_packets() + divider_packets
    sorted_data_packets = ut.insert_sort(list=data_packets, compare=compare)
    answer = reduce(lambda x, y: x * y, [(i + 1) for i, packet in enumerate(sorted_data_packets) if packet in divider_packets])
    
    ut.print_answer(part=2, day=day, answer=answer)


part_one()
part_two()