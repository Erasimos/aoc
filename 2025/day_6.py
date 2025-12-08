import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

def get_input_1():
    puzzle_input = read_file(puzzle_input_path)
    problems = {}   
    
    # Values in the problems
    for line in puzzle_input[0:-1]:
        for col, val in enumerate(line.split()):
            problems.setdefault(col, {}).setdefault('values', []).append(int(val))
    
    # Operators in the problems
    for col, op in enumerate(puzzle_input[-1].split()):
        problems[col]['op'] = op
        
    return problems

def get_input_2():
    puzzle_input = read_file(puzzle_input_path)
    problems = {}

    values = {}
    for line in puzzle_input[0:-1]:
        for col, val in enumerate(line): 
            values[col] = values.get(col, '') + val
    
    problem_index = 0
    for col in range(len(puzzle_input[0])):
        trimmed_value = values[col].replace(' ', '')
        if trimmed_value == '':
            problem_index += 1
        else:
            problems.setdefault(problem_index, {}).setdefault('values', []).append(int(trimmed_value))

    for problem_index, op in enumerate(puzzle_input[-1].split()):
        problems[problem_index]['op'] = op
    
    return problems

def solve_problem(problem: dict):

    op = problem['op']
    if op == '+':
        answer = 0
        for val in problem['values']:
            answer += val
        return answer
    elif op == '*':
        answer = 1
        for val in problem['values']:
            answer *= val
        return answer
    return None        

def part_one():

    answer = 0
    problems = get_input_1()
    print(problems)
    for problem in problems.values():
        answer += solve_problem(problem=problem)
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    answer = 0
    problems = get_input_2()
    for problem in problems.values():
        answer += solve_problem(problem=problem)
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()