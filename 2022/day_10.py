import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from typing import List
import math
from ut import Vec2D

day = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day}.txt'

class CRT:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.screen = {}
    
    def display(self):
        for y  in range(self.h):
            for x in range(self.w):
                screen_pos = Vec2D(x, y)
                print(self.screen.get(screen_pos, '.'), end='')
            print()

    def draw_pixel(self, cycle: int, sprite_pos: int):
        target_pixel_x = cycle % self.w
        target_pixel_y = int(cycle / self.w)

        if target_pixel_x in [sprite_pos, sprite_pos + 1, sprite_pos - 1]:
            self.screen[Vec2D(target_pixel_x, target_pixel_y)] = '#'

class Instruction:
    def __init__(self, op, args = []):
        self.op = op
        self.args = [int(arg) for arg in args]
        
    def __repr__(self):
            return f"Instruction(op={self.op}, args={self.args})"

class Computer:
    def __init__(self, crt: CRT = None):
        self.registers = {'x': 1}
        self.cycle = 0
        self.memory = {0: self.registers['x']}
        self.crt = crt

    def addx(self, arg):
        self.step_cycle()
        self.step_cycle()
        self.registers['x'] = self.registers['x'] + arg
        
    def step_cycle(self):
        self.cycle += 1
        self.memory[self.cycle] = self.registers['x']
        if self.crt:
            self.crt.draw_pixel(self.cycle - 1, self.registers['x'])

    def get_signal_strength(self, cycle):
        return cycle * self.memory[cycle]

    def run_program(self, program: List[Instruction]):
        
        for instruction in program:

            if instruction.op == 'noop':
                self.step_cycle()

            elif instruction.op == 'addx':      
                self.addx(instruction.args[0])
            
        
def get_input():
    puzzle_input = ut.read_file(puzzle_input_path)
    return  [Instruction(op=op, args=args) for op, *args in (line.split() for line in puzzle_input)]


def part_one():

    program = get_input()
    computer = Computer()
    computer.run_program(program=program)

    target_cycles = [20, 60, 100, 140, 180, 220]
    answer = sum(computer.get_signal_strength(cycle) for cycle in target_cycles)

    ut.print_answer(part=1, day=day, answer=answer)


def part_two():

    program = get_input()
    computer = Computer(crt=CRT(width=40, height=6))
    computer.run_program(program=program)
    computer.crt.display()
    answer = 0

    ut.print_answer(part=2, day=day, answer=answer)

part_one()
part_two()