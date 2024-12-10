import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)
from copy import deepcopy
from ut.common import Vec2D, read_file, print_answer, UDLR, Vec2DMap

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

def get_input():
    puzzle_input = read_file(puzzle_input_path)
    top_map = {Vec2D(x, y): int(el) for y, line in enumerate(puzzle_input) for x, el in enumerate(line)}
    return top_map

def get_trails(top_map: dict, pos: Vec2D, path: list = []):
    
    new_path = deepcopy(path) 
    new_path.append(pos)
    
    trail_pos = top_map.get(pos, '')

    if trail_pos == 9:
        return [new_path]

    trails = []
    for direction in UDLR:
        new_pos = pos + direction
        new_trail_pos = top_map.get(new_pos, '')
        if not new_trail_pos == '.' and new_trail_pos == trail_pos + 1:
            trails += get_trails(top_map=top_map, pos=pos + direction, path=new_path)    
    return trails

def get_score_2(top_map: dict, trailheads: list):
    score = 0
    for trailhead in trailheads:
        new_trails = get_trails(top_map=top_map, pos=trailhead)
        score += len(new_trails)
    return score

def get_score(top_map: dict, trailheads: list):
    
    score = 0
    for trailhead in trailheads:
        new_trails = get_trails(top_map=top_map, pos=trailhead)
        uniqe_9s = {trail[-1]: True for trail in new_trails}
        score += len(uniqe_9s.keys())
    return score


def get_trailheads(top_map: dict):
    trailheads = []
    for pos, elevation in top_map.items():
        if elevation == 0:
            trailheads.append(pos)
    return trailheads

def part_one():

    top_map = get_input()
    trailheads = get_trailheads(top_map=top_map)
    answer = get_score(trailheads=trailheads, top_map=top_map)

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    top_map = get_input()
    trailheads = get_trailheads(top_map=top_map)
    answer = get_score_2(trailheads=trailheads, top_map=top_map)
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()




## OPTINAL PY GAME VISUALIZATION
###
###
### ---------------------------------------------------------------
from ut.day import Day
from ut.constants import Colors
from ut.simulation_state import SimulationState
simulation_state = SimulationState()

def run_day():
    pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
    day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
    day.run()

# run_day()