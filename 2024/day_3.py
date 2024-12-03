import os
import re
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

enabled = True

def get_input():
    return read_file(puzzle_input_path)

def get_valid_instructions_2(corrupted_memory: str):
    pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
    return re.findall(pattern, corrupted_memory)

def get_valid_instructions(corrupted_memory: str):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    return re.findall(pattern, corrupted_memory)

def evaluate_instruction_2(instruction: str):

    global enabled

    if instruction == 'do()':
        enabled = True
    elif instruction == 'don\'t()':
        enabled = False
    else:
        if enabled:
            return evaluate_instruction(instruction)
    return 0

def evaluate_instruction(instruction: str):
    num_1, num_2 = instruction.split('mul(')[1].split(')')[0].split(',')
    return int(num_1) * int(num_2)


def part_one():

    corrupted_memory = get_input()
    answer = 0
    for line in corrupted_memory:
        instructions = get_valid_instructions(corrupted_memory=line)
        answer += sum([evaluate_instruction(instruction) for instruction in instructions])
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    corrupted_memory = get_input()
    answer = 0
    for line in corrupted_memory:
        instructions = get_valid_instructions_2(corrupted_memory=line)
        answer += sum([evaluate_instruction_2(instruction) for instruction in instructions])
    print_answer(part=1, day=day_nr, answer=answer)

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