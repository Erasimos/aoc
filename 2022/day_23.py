import os
import sys
from pathlib import Path
sys.path.insert(0, os.path.join(os.getcwd(), 'ut'))
from ut.day import Day
from ut.constants import Colors
from ut.common import Vec2D, read_file, print_answer, print_dict_map

import time

from ut.simulation_state import SimulationState
simulation_state = SimulationState()



day_nr = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_nr}.txt'

day_nr = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_nr}.txt'



direction_neighbours = {
    'N': [Vec2D(-1, -1), Vec2D(0, -1), Vec2D(1, -1)],
    'S': [Vec2D(-1, 1), Vec2D(0, 1), Vec2D(1, 1)],
    'W': [Vec2D(-1, -1), Vec2D(-1, 0), Vec2D(-1, 1)],
    'E': [Vec2D(1, -1), Vec2D(1, 0), Vec2D(1, 1)],
}

directions = {
    'N': Vec2D(0, -1),
    'S': Vec2D(0, 1),
    'W': Vec2D(-1, 0),
    'E': Vec2D(1, 0),
}

def get_input():
    puzzle_input = read_file(puzzle_input_path)
    elf_map = {}
    for y, line in enumerate(puzzle_input):
        for x, el in enumerate(line):
            if el == '#':
                elf_map[Vec2D(x, y)] = el
    return elf_map

class GameOfElfs:
    def __init__(self, elf_map: dict):
        self.elf_map = elf_map
        self.dir_index = 0
        self.directions = ['N', 'S', 'W', 'E']

    
    def is_alone(self, elf_pos: Vec2D):
        for neighbour in elf_pos.neighbors():
            if self.elf_map.get(neighbour, '') == '#':
                return False
        return True
        
    def get_proposal(self, elf_pos: Vec2D):

        for i in range(4):

            current_direction_index = (self.dir_index + i) % len(self.directions)
            current_direction = self.directions[current_direction_index]

            for neighbour in direction_neighbours[self.directions[current_direction_index]]:
                if self.elf_map.get((elf_pos + neighbour), '') == '#':
                    break
            else:
                return elf_pos + directions[current_direction]

        
        return None



    def round(self):
        moving_elfs = []
        moving_proposals = {}

        for elf_pos, _ in self.elf_map.items():
            if self.is_alone(elf_pos=elf_pos):
                continue
            else:
                 move_proposal = self.get_proposal(elf_pos=elf_pos)
                 if move_proposal:
                    moving_proposals[move_proposal] = moving_proposals.get(move_proposal, 0) + 1 
                    moving_elfs.append((elf_pos, move_proposal))

        for moving_elf, move_proposal in moving_elfs:
            if moving_proposals.get(move_proposal, 0) <= 1:
                self.elf_map.pop(moving_elf)
                self.elf_map[move_proposal] = '#'

        return moving_elfs


    def rounds(self, rounds: int):
        for _ in range(rounds):
            self.round()
            self.dir_index = (self.dir_index + 1) % len(self.directions)

    def emtpy_spaces(self):

        x_positions = [pos.x for pos in self.elf_map.keys()]
        y_positions = [pos.y for pos in self.elf_map.keys()]
        min_x, max_x = min(x_positions), max(x_positions)
        min_y, max_y = min(y_positions), max(y_positions)

        size_x = (max_x - min_x) + 1
        size_y = (max_y - min_y) + 1 

        return size_x * size_y - len(self.elf_map.items())

    def scatter(self):
        rounds = 1
        while self.round():
            self.dir_index = (self.dir_index + 1) % len(self.directions)
            rounds += 1
        return rounds

def part_one():

    elf_map = get_input()
    game_of_elfs = GameOfElfs(elf_map=elf_map)
    game_of_elfs.rounds(10)    

    answer = game_of_elfs.emtpy_spaces()

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    elf_map = get_input()
    game_of_elfs = GameOfElfs(elf_map=elf_map)
    answer = game_of_elfs.scatter() 
    print_answer(part=2, day=day_nr, answer=answer)


def run_day():
    pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
    day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
    day.run()


part_one()
part_two()

#run_day()