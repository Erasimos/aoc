import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from typing import List
from collections import deque

day_nr = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_nr}.txt'

class Node:
    def __init__(self, value: int):
        self.value = value 
        self.moved = False


class CircularList:
    def __init__(self, values: list[int]):

        self.elements = deque(Node(value=value) for value in values)
        self.original_order = list(self.elements)
        self.size = len(values)
        
    def remove(self, index: int):
        self.elements = self.elements[0:index] + self.elements[index+1:]

    def insert(self, index: int, node: Node):
        self.elements = self.elements[0:index] + [node] + self.elements[index:]

    def mix(self):

        for node in self.original_order:
            if not node.moved:
                current_index = self.elements.index(node)
                new_index = (current_index + node.value) % (self.size - 1)
                self.elements.remove(node)
                self.elements.insert(new_index, node)
                node.moved = True

        for node in self.elements:
            node.moved = False

    def print_list(self):
        for node in self.elements:
            print(node.value, end=', ')
        print()
        print()

    def get_zero_index(self):
        for index, node in enumerate(self.elements):
            if node.value == 0: return index
        return -1
        
    def get_answer(self):

        zero_index = self.get_zero_index()
        i1 = (zero_index + 1000) % self.size
        i2 = (zero_index + 2000) % self.size
        i3 = (zero_index + 3000) % self.size
        return self.elements[i1].value + self.elements[i2].value + self.elements[i3].value


def get_input():
    puzzle_input = ut.read_file(puzzle_input_path)
    return [int(el) for el in puzzle_input]    


def part_one():

    values = get_input()
    circular_list = CircularList(values=values)
    circular_list.mix()
    answer = circular_list.get_answer()
    ut.print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    decrypt_key = 811589153
    values = [decrypt_key * value for value in get_input()]
    circular_list = CircularList(values=values)

    for _ in range(10):
        circular_list.mix()
    answer = circular_list.get_answer()
    ut.print_answer(part=1, day=day_nr, answer=answer)



part_one()
part_two()
