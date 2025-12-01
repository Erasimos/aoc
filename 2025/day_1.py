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

class Dial:

    def __init__(self, size):
        self.value = 50
        self.size = size
    
    def turn(self, direction, steps):
        match direction:
            case 'R':
                self.value = (self.value + steps) % self.size
                
            case 'L':
                self.value = (self.value - steps) % self.size
 

    def turn_2(self, direction, steps):

        loops = 0

        match direction:
            case 'R':
                new_value = self.value + steps
                while new_value >= self.size:
                    new_value -= self.size

                    loops += 1

                self.value = new_value
                if self.value == 0:
                    loops -= 1
                
            case 'L':
                if self.value == 0:
                    loops = -1

                new_value = self.value - steps
                while new_value < 0:
                    new_value += self.size

                    loops += 1

                self.value = new_value
        if self.value == 0: loops+= 1
        return loops


    def execute(self, rotations):
        zero_count = 0
        for rotation in rotations:
            direction, steps = rotation
            self.turn(direction=direction, steps=steps)
            
            if self.value == 0:
                zero_count += 1

        return zero_count
    
    def execute_2(self, rotations):
        zero_count = 0
        for rotation in rotations:
            direction, steps = rotation
            zero_count += self.turn_2(direction=direction, steps=steps)
        return zero_count


def get_input():
    puzzle_input = read_file(puzzle_input_path)
    rotations = []
    for line in puzzle_input:
        direction = line[0]
        steps = int(line[1:])
        rotations.append((direction, steps))
    return rotations

def part_one():

    rotations = get_input()
    dial = Dial(size=100)
    answer = dial.execute(rotations=rotations)
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    rotations = get_input()
    dial = Dial(size=100)
    answer = dial.execute_2(rotations=rotations)    
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()