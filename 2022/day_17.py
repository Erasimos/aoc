import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from ut import Vec2D
from constants import Colors
from day import Day
from typing import List
import time

day_nr = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_nr}.txt'

ROCKS = {
    '__': [Vec2D(0, 0), Vec2D(1, 0), Vec2D(2, 0), Vec2D(3, 0)],
    '+': [Vec2D(0,0), Vec2D(0, 1), Vec2D(0, -1), Vec2D(1, 0), Vec2D(-1, 0)],
    '_|': [Vec2D(0, 0), Vec2D(1, 0), Vec2D(2, 0), Vec2D(2, 1), Vec2D(2, 2)],
    '|': [Vec2D(0, 0), Vec2D(0, 1), Vec2D(0, 2), Vec2D(0, 3)],
    '::': [Vec2D(0, 0), Vec2D(1, 0), Vec2D(1, 0), Vec2D(1, 1)]
}

class Rock():
    def __init__(self, shape: str, y: int):
        self.positions = ROCKS[shape]
        self.spawn(y=y)

    def spawn(self, y: int):
        min_y = min([pos.y for pos in self.positions])
        min_x = min([pos.x for pos in self.positions])

        x_offset = 2 - min_x
        y_offset = y - min_y
        self.positions = [pos + Vec2D(x_offset, y_offset) for pos in self.positions]

    def move(self, movement: Vec2D, rock_tower: dict={}):

        new_positions = [pos + movement for pos in self.positions]
        if any(new_pos.y <= 0 for new_pos in new_positions): return False
        if any(new_pos.x < 0 or new_pos.x >= 7 for new_pos in new_positions): return False
        if any(rock_tower.get(new_pos, '.') == '#' for new_pos in new_positions): return False
        self.positions = new_positions
        return True
        
    def fall(self, jet_pattern, rock_tower: dict):

        for pos in self.positions: rock_tower[pos] = '@'
        print(self.positions)
        ut.print_dict_map(dict_map=rock_tower)
        for pos in self.positions: rock_tower[pos] = '.'
        # Jet
        match(jet_pattern):
            case '<': self.move(Vec2D(-1, 0)) 
            case '>': self.move(Vec2D(1, 0))          
        # Down
        moved = self.move(movement=Vec2D(0, -1), rock_tower=rock_tower)
    
        for pos in self.positions: rock_tower[pos] = '@'
        ut.print_dict_map(dict_map=rock_tower)
        for pos in self.positions: rock_tower[pos] = '.'

        return moved

class RockSystem():
    def __init__(self):
        self.rock_tower = {}
        self.jet_patterns = []
        self.jet_pattern_i = 0
        self.rock_sequence = ['__', '+', '_|', '|', '::']
        self.rock_sequence_i = 0
        self.tower_height = 0


    def fall_rock(self):
        
        new_rock = Rock(self.rock_sequence[self.rock_sequence_i],y=self.tower_height + 4)
        self.rock_sequence_i = (self.rock_sequence_i + 1) % 5

        while new_rock.fall(jet_pattern=self.jet_patterns[self.jet_pattern_i], rock_tower=self.rock_tower):
            self.jet_pattern_i = (self.jet_pattern_i + 1) % len(self.jet_patterns)

        for pos in new_rock.positions: self.rock_tower[pos] = '#'
        self.tower_height = max(pos.y for pos in new_rock.positions)

    def simulate(self, jet_patterns: List[str]):
        self.jet_patterns = jet_patterns
        self.jet_pattern_i = 0
        self.rock_sequence_i = 0
        self.rock_tower = {}
        self.tower_height = -1

        for rock in range(2022):
            self.fall_rock()
            
            print()
            
        return self.tower_height
    
def part_one():

    jet_pattterns = ut.read_file(puzzle_input_path)[0]
    rock_system = RockSystem()
    answer = rock_system.simulate(jet_patterns=jet_pattterns)
    ut.print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    jet_pattterns = ut.read_file(puzzle_input_path)
    rock_system = RockSystem()
    answer = rock_system.simulate(jet_patterns=jet_pattterns)

    answer = 0
    
    ut.print_answer(part=2, day=day_nr, answer=answer)


pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
#day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
#day.run()
part_one()
#part_two()
