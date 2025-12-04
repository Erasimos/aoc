import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2DMap, Vec2D, read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

def get_input():
    return {Vec2D(x=x, y=y): el for y, line in enumerate(read_file(puzzle_input_path)) for x, el in enumerate(line)}

def is_reachable(pos: Vec2D, department_map: dict):
    paper_count = 0
    for n_pos in pos.neighbors():
        if department_map.get(n_pos, '.') == '@': paper_count += 1
    return paper_count < 4
    
def get_reachable_rolls(department_map: dict):
    reachable_rolls = {}
    for d_pos in department_map.keys():
        if department_map.get(d_pos, '.') == '@' and is_reachable(pos=d_pos, department_map=department_map):
            reachable_rolls[d_pos] = True
    return reachable_rolls

def remove_paper(department_map: dict):
    total_paper = 0
    reachable_rolls = get_reachable_rolls(department_map=department_map)
    while reachable_rolls:
        for p_pos in reachable_rolls.keys():
            department_map[p_pos] = '.'
            total_paper += 1
        reachable_rolls = get_reachable_rolls(department_map=department_map)
    return total_paper

def part_one():

    department_map = get_input()
    reachable_rolls = get_reachable_rolls(department_map=department_map)
    answer = len(reachable_rolls.keys())
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    department_map = get_input()
    answer = remove_paper(department_map=department_map)
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()