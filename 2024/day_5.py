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
    raw_rules, raw_updates = read_file_raw(puzzle_input_path).split('\n\n')
    
    rules = {}
    for line in raw_rules.splitlines():
        v1, v2 = line.split('|')

        rules.setdefault(int(v2), []).append(int(v1))

    updates = []
    for line in raw_updates.splitlines():
        split_line = line.split(',')
        updates.append([int(el) for el in split_line])

    return rules, updates

def is_valid_update(update: list, rules: dict):

    applied_rules = {}

    for index, value in enumerate(update):
        for num in rules.get(value, []):
            if num in update[index + 1:]:
                if not applied_rules.get(num, False):
                    return False 
        applied_rules[value] = True
    return True
    
def correct_update(invalid_update: list, rules: dict):
    is_corrected = False
    while not is_corrected:

        is_corrected = True
        swapped = False

        applied_rules = {}

        for index, value in enumerate(invalid_update):
            for num in rules.get(value, []):
                if num in invalid_update[index + 1:]:
                    if not applied_rules.get(num, False):
                        is_corrected = False
                        swap_index = invalid_update.index(num)
                        invalid_update[swap_index] = value
                        invalid_update[index] = num
                        swapped = True
                        applied_rules[num] = True
                        break

            if swapped:
                break
            else:
                applied_rules[value] = True
    return invalid_update

def get_answer(valid_updates):
    return sum([valid_update[int(len(valid_update)/2)] for valid_update in valid_updates])

def part_one():

    rules, updates = get_input()
    valid_updates = [update for update in updates if is_valid_update(update=update, rules=rules)]
    answer = get_answer(valid_updates=valid_updates)

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    rules, updates = get_input()
    invalid_updates = [update for update in updates if not is_valid_update(update=update, rules=rules)]
    corrected_updates = []
    for invalid_update in invalid_updates:
        corrected_updates.append(correct_update(invalid_update=invalid_update, rules=rules))
    answer = get_answer(valid_updates=corrected_updates)
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()




## OPTINAL PY GAME VISUALIZATION
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