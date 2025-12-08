import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, read_file_raw, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

class Range:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __repr__(self):
        return f"Range: low={self.low}, high={self.high}"

    def is_in(self, val: int):
        return val >= self.low and val <= self.high
    
    def get_size(self):
        return self.high - self.low + 1 

def get_input():
    ranges_raw, ids_raw = read_file_raw(puzzle_input_path).split('\n\n')
    ranges = []
    for line in ranges_raw.splitlines():
        low, high = line.split('-')
        ranges.append(Range(low=int(low), high=int(high)))

    ids = [int(line) for line in ids_raw.splitlines()]

    return ranges, ids

def insert_range(merged_ranges: list[Range], range: Range):

    overlaps = [range]
    non_overlaps = []

    for merged_range in merged_ranges:
        
        if merged_range.is_in(range.low) or merged_range.is_in(range.high) or range.is_in(merged_range.low) or range.is_in(merged_range.high):
            overlaps.append(merged_range)
        else:
            non_overlaps.append(merged_range)
    
    new_merged_range = Range(
        low=min([overlapping_range.low for overlapping_range in overlaps]),
        high=max([overlapping_range.high for overlapping_range in overlaps])
    )

    return non_overlaps + [new_merged_range]

def merge_ranges(ranges: list[Range]) -> list[Range]:
    merged_ranges = []
    for range in ranges:
        merged_ranges = insert_range(merged_ranges=merged_ranges, range=range)
    return merged_ranges

def get_fresh_ids(ranges: list[Range], ids: list):
    fresh_ids = []
    for id in ids:
        for range in ranges:
            if range.is_in(id):
                fresh_ids.append(id)
                break
    return fresh_ids

def get_total_fresh_ids(ranges: list[Range]):
    merged_ranges = merge_ranges(ranges=ranges)
    return sum([merged_range.get_size() for merged_range in merged_ranges])

def part_one():

    ranges, ids = get_input()
    fresh_ids = get_fresh_ids(ranges=ranges, ids=ids)
    answer = len(fresh_ids)
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    ranges, ids = get_input()    
    answer = get_total_fresh_ids(ranges=ranges)
    
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()