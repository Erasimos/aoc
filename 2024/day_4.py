import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, read_file, print_answer, NEIGHBORS_2D

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

def get_word_puzzle():
    puzzle_input =  read_file(puzzle_input_path)
    word_puzzle = {Vec2D(x, y): tile for y, line in enumerate(puzzle_input) for x, tile in enumerate(line)}
    return word_puzzle

def is_X_mas(word_puzzle: dict, pos: Vec2D):
    if word_puzzle.get(pos, '') == 'A':
        corner_seq: str = ''
        c1 = word_puzzle.get(pos + Vec2D(1, 1), '')
        c2 = word_puzzle.get(pos + Vec2D(1, -1), '')
        c3 = word_puzzle.get(pos + Vec2D(-1, 1), '')
        c4 = word_puzzle.get(pos + Vec2D(-1, -1), '')
        corner_seq += c1
        corner_seq += c2
        corner_seq += c3
        corner_seq += c4

        if corner_seq.count('S') == 2 and corner_seq.count('M') == 2 and not c1 == c4:
            return True
    return False


def find_X_mas(word_puzzle: dict):
    return sum([is_X_mas(word_puzzle=word_puzzle, pos=pos) for pos in word_puzzle.keys()])

def find_occurrences_pos(word_puzzle: dict, pos: Vec2D , word: str) -> int:
    occurences = 0
    c1: str = word_puzzle.get(pos, '')
    for direction in NEIGHBORS_2D:
        seq: str = c1
        for i in range(1, len(word)):
            seq += word_puzzle.get(pos + (direction * i), '')
        if seq == word:
            occurences += 1
    return occurences


def find_occurrences(word_puzzle: dict, word: str) -> int:
    return sum([find_occurrences_pos(word_puzzle=word_puzzle, pos=pos, word=word) for pos in word_puzzle.keys()])


def part_one():

    word_puzzle = get_word_puzzle()
    answer = find_occurrences(word_puzzle=word_puzzle, word='XMAS')

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    word_puzzle = get_word_puzzle()
    answer = find_X_mas(word_puzzle=word_puzzle)
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