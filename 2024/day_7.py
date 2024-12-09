import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, read_file, read_file_raw, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'
def get_input():
    puzzle_input = read_file(puzzle_input_path)
    equations = []
    for line in puzzle_input:
        equation = {}
        split_line = line.split()
        answer = int(split_line[0][0:-1])
        args = [int(el) for el in split_line[1:]]
        equation['answer'] = answer
        equation['args'] = args
        equations.append(equation)
    return equations

def get_possible_solutions(equation: dict):
    
    args = equation.get('args', [])
    possible_solutions = [args[0]]
    for arg in args[1:]:
        new_possible_solutions = []
        for sol in possible_solutions:
            new_possible_solutions.append(sol * arg)
            new_possible_solutions.append(sol + arg)
        possible_solutions = new_possible_solutions
    return possible_solutions
        
def get_possible_solutions_2(equation: dict):
    
    args = equation.get('args', [])
    possible_solutions = [args[0]]
    for arg in args[1:]:
        new_possible_solutions = []
        for sol in possible_solutions:
            new_possible_solutions.append(sol * arg)
            new_possible_solutions.append(sol + arg)
            new_possible_solutions.append(int(str(sol) + str(arg)))
        possible_solutions = new_possible_solutions
    return possible_solutions


def is_true_equation(equation: dict):
    possible_solutions = get_possible_solutions(equation=equation)
    if equation.get('answer', None) in possible_solutions:
        return True
    return False

def is_true_equation_2(equation: dict):
    possible_solutions = get_possible_solutions_2(equation=equation)
    if equation.get('answer', None) in possible_solutions:
        return True
    return False

def part_one():

    equations = get_input()
    true_equations = [equation for equation in equations if is_true_equation(equation=equation)]
    answer = sum([equation.get('answer', 0) for equation in true_equations])
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    equations = get_input()
    true_equations = [equation for equation in equations if is_true_equation_2(equation=equation)]
    answer = sum([equation.get('answer', 0) for equation in true_equations])
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