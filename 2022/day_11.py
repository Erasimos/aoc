from ast import Call
import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from typing import List, Callable, Dict
from operator import mul, add

operation_map = {
    '*': mul,
    '+': add
}

day = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day}.txt'

class Monkey:

    monkeys = {}
    worry_scaling = 1

    def __init__(self, items: List[int], op: Callable, op_val, test_val: int, true_dest: int, false_dest: int, id: int):
        self.items = items
        self.op = op
        self.op_val = op_val
        self.test_val = test_val
        self.true_dest = true_dest
        self.false_dest = false_dest
        self.id = id
        self.inspections = 0
        self.__class__.monkeys[self.id] = self
        self.__class__.worry_scaling *= test_val
        

    
    def play(self):

        for item in self.items:
            if self.op_val == 'old':
                worry_lvl = self.op(item, item)
            else:
                worry_lvl = self.op(item, self.op_val)

            worry_lvl = worry_lvl // 3

            dest_monkey = self.true_dest if worry_lvl % self.test_val == 0 else self.false_dest
            self.__class__.monkeys[dest_monkey].items.append(worry_lvl)
            self.inspections += 1

        self.items = []


    def play_2(self):

        for item in self.items:
            if self.op_val == 'old':
                worry_lvl = self.op(item, item)
            else:
                worry_lvl = self.op(item, self.op_val)

            worry_lvl = worry_lvl % self.worry_scaling
            

            dest_monkey = self.true_dest if worry_lvl % self.test_val == 0 else self.false_dest
            self.__class__.monkeys[dest_monkey].items.append(worry_lvl)
            self.inspections += 1

        self.items = []

def get_monkeys() -> List[Monkey]:
    puzzle_input = ut.read_file_raw(puzzle_input_path)

    monkeys = []

    for i, chunk in enumerate(puzzle_input.split('\n\n')):
        
        split_chunk = chunk.split('\n')

        items = [int(item) for item in split_chunk[1].split(':')[1].split(',')]
        
        op_line = split_chunk[2].split(':')[1].split()
        
        op_val = int(op_line[-1]) if not op_line[-1] == 'old' else op_line[-1]
        op = operation_map[op_line[-2]]

        test_val = int(split_chunk[3].split()[-1])    

        true_dest = int(split_chunk[4].split()[-1])
        false_dest = int(split_chunk[5].split()[-1])

        monkey = Monkey(items=items, op=op, op_val=op_val, test_val=test_val, true_dest=true_dest, false_dest=false_dest, id=i)
        monkeys.append(monkey)

    return monkeys


def part_one():

    monkeys = get_monkeys()
    rounds = 20

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.play()
        
    inspections = sorted([monkey.inspections for monkey in monkeys])
    answer = inspections[-1] * inspections[-2]
    
    ut.print_answer(part=1, day=day, answer=answer)


def part_two():

    monkeys = get_monkeys()
    rounds = 10000

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.play_2()

    inspections = sorted([monkey.inspections for monkey in monkeys])
    answer = inspections[-1] * inspections[-2]
    ut.print_answer(part=2, day=day, answer=answer)


part_one()
part_two()