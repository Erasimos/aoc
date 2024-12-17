import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)
from math import pow
from ut.common import Vec2D, read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

class ThreeBitComputer:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.instruction_pointer = 0
        self.output = ''

    def run_program(self, program: list):

        while self.instruction_pointer >= 0 and self.instruction_pointer < len(program) - 1:
            #print(opcode)
            ##print(operand)

            opcode = program[self.instruction_pointer]
            operand = program[self.instruction_pointer + 1]

            match opcode:
                case 0:
                    self.adv(operand)
                case 1:
                    self.bxl(operand)
                case 2:
                    self.bst(operand)
                case 3:
                    self.jnz(operand)
                case 4:
                    self.bxc(operand)
                case 5:
                    self.out(operand)
                case 6:
                    self.bdv(operand)
                case 7:
                    self.cdv(operand)
                    
    def get_combo_operand(self, operand):

        if operand in [0, 1, 2, 3]:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        elif operand == 7:
            print('o Noh')
            return None

        return None
        
    def adv(self, operand):
        denom = pow(2, self.get_combo_operand(operand=operand))
        self.a = int(self.a / denom)
        self.instruction_pointer += 2
        
    def bxl(self, operand):
        self.b = self.b & operand
        self.instruction_pointer += 2

    def bst(self, operand):
        self.b = self.get_combo_operand(operand=operand) % 8
        self.instruction_pointer += 2

    def jnz(self, operand):
        if not self.a == 0:
            self.instruction_pointer = operand
        else:
            self.instruction_pointer += 2

    def bxc(self, operand):
        self.b = self.b | self.c
        self.instruction_pointer += 2

    def out(self, operand):
        output = self.get_combo_operand(operand=operand) % 8
        self.output += str(output) + ','
        self.instruction_pointer += 2

    def bdv(self, operand):
        denom = pow(2, self.get_combo_operand(operand=operand))
        self.b = int(self.a / denom)
        self.instruction_pointer += 2

    def cdv(self, operand):
        denom = pow(2, self.get_combo_operand(operand=operand))
        self.c = int(self.a / denom)
        self.instruction_pointer += 2

def part_one():

    pc = ThreeBitComputer(a=46323429, b=0, c=0)
    instructions = [2,4,1,1,7,5,1,5,4,3,0,3,5,5,3,0]
    pc.run_program(instructions)
    answer = pc.output

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
#part_two()