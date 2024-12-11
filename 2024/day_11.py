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

def get_input():
    puzzle_input = read_file_raw(puzzle_input_path)
    stones = {}
    for el in puzzle_input.split():
        stones[int(el)] = 1
    return stones        

def blink(stones: dict):

    new_stones = {}

    for stone_id, stone_count in stones.items():
        
        stone_id_length = len(str(stone_id))
       
        if stone_id == 0:
            new_stones[1] = stone_count + new_stones.get(1, 0)

        elif stone_id_length % 2 == 0:
            new_stone_id_1 = int(str(stone_id)[0:int(stone_id_length/2)])
            new_stone_id_2 = int(str(stone_id)[int(stone_id_length/2):])
            new_stones[new_stone_id_1] = stone_count + new_stones.get(new_stone_id_1, 0)
            new_stones[new_stone_id_2] = stone_count + new_stones.get(new_stone_id_2, 0)
        else:
            new_stone_id = stone_id * 2024
            new_stones[new_stone_id] = stone_count + new_stones.get(new_stone_id, 0)

    return new_stones


def part_one():

    stones = get_input()
    blinks = 25
    for _ in range(blinks):
        stones = blink(stones=stones)
    answer = sum([el for el in stones.values()])
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    stones = get_input()
    blinks = 75
    for _ in range(blinks):
        stones = blink(stones=stones)
    answer = sum([el for el in stones.values()])
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()