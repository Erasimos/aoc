import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, read_file_raw, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

class ClawMachine:
    def __init__(self, button_a: Vec2D, button_b: Vec2D, prize_location: Vec2D):
        self.button_a = button_a
        self.button_b = button_b
        self.prize_location = prize_location

    def get_cheapest_prize_2(self):

        self.prize_location = self.prize_location + Vec2D(10000000000000, 10000000000000)

        b_nom = (self.prize_location.y * self.button_a.x) - (self.prize_location.x * self.button_a.y)
        b_denom = ((self.button_a.x * self.button_b.y) - (self.button_a.y * self.button_b.x))

        b = b_nom / b_denom

        a_nom = (self.prize_location.x - (b * self.button_b.x))
        a_denom = self.button_a.x
        a = a_nom / a_denom 

        if a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
            tokens = a * 3 + b
            return tokens
        return 0

    def get_cheapest_prize(self):

        b_nom = (self.prize_location.y * self.button_a.x) - (self.prize_location.x * self.button_a.y)
        b_denom = ((self.button_a.x * self.button_b.y) - (self.button_a.y * self.button_b.x))

        b = b_nom / b_denom

        a_nom = (self.prize_location.x - (b * self.button_b.x))
        a_denom = self.button_a.x
        a = a_nom / a_denom 
        
        if a <= 100 and b <= 100 and a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
            tokens = a * 3 + b
            return tokens
        return 0

def get_claw_machine(chunk: str):
    split_chunk = chunk.splitlines()

    # Button A
    a_chunk = split_chunk[0].split()
    a_x = int(a_chunk[2].split('+')[1][0:-1])
    a_y = int(a_chunk[3].split('+')[1])
    button_a = Vec2D(a_x, a_y)

    # Button B
    b_chunk = split_chunk[1].split()
    b_x = int(b_chunk[2].split('+')[1][0:-1])
    b_y = int(b_chunk[3].split('+')[1])
    button_b = Vec2D(b_x, b_y)

    # Prize Location
    prize_chunk = split_chunk[2].split()
    prize_x = int(prize_chunk[1].split('=')[1][0:-1])
    prize_y = int(prize_chunk[2].split('=')[1])
    prize_location = Vec2D(prize_x, prize_y)

    return ClawMachine(button_a=button_a, button_b=button_b, prize_location=prize_location)

def get_input():
    puzzle_input = read_file_raw(puzzle_input_path)
    claw_machines = []
    for raw_chunk in puzzle_input.split('\n\n'):
        claw_machines.append(get_claw_machine(chunk=raw_chunk))
    return claw_machines

def part_one():

    claw_machines = get_input()
    answer = sum([claw_machine.get_cheapest_prize() for claw_machine in claw_machines])
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    claw_machines = get_input()
    answer = sum([claw_machine.get_cheapest_prize_2() for claw_machine in claw_machines])
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()