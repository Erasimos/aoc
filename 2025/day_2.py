import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import read_file_raw, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

def get_input():
    puzzle_input = read_file_raw(puzzle_input_path).split(',')
    ranges = []
    for el in puzzle_input:
        start, stop = el.split('-')
        ranges.append({'start': int(start), 'stop': int(stop)})
    return ranges

def is_invalid(id):
    str_id = str(id)
    id_size = len(str_id)
    if id_size % 2 == 0:
        id_size_half = int(id_size/2)
        if str_id[0:id_size_half] == str_id[id_size_half:]:
            return True
    return False

def is_invalid_2(id):
    str_id = str(id)
    id_size = len(str_id)
    
    for sequence_size in range(1, int(id_size/2)+1):
        if id_size % sequence_size == 0:
            sequence_part = str_id[0:sequence_size]
            sequence_parts = int(id_size/sequence_size)
            if str_id == (sequence_part * sequence_parts):
                return True
    return False

def get_invalid_ids(r, version, invalid_ids):
    start = r.get('start', None)
    end = r.get('stop', None)
    for id in range(start, end + 1):

        invalid = False
        match version:
            case 1:
                invalid = is_invalid(id)
            case 2:
                invalid = is_invalid_2(id)

        if invalid:
            invalid_ids[id] = True

    return invalid_ids

def part_one():

    ranges = get_input()
    invalid_ids = {}
    for r in ranges:
        get_invalid_ids(r=r, version=1, invalid_ids=invalid_ids)

    answer = sum(invalid_ids.keys())

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    ranges = get_input()
    invalid_ids = {}
    for r in ranges:
        get_invalid_ids(r=r, version=2, invalid_ids=invalid_ids)

    answer = sum(invalid_ids.keys())

    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()