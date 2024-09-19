import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from ut import Vec2D, UDLR_MAP


day = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day}.txt'

class Rope:
    def __init__(self, size):
        self.head = Vec2D(0, 0)
        self. tail = Rope(size - 1) if size > 1 else None
    
    def move(self, dir: Vec2D):
        self.head += dir

        if self.tail == None or self.tail.head in self.head.neighbors() or self.tail.head == self.head:
            return
        
        dxy = (self.head - self.tail.head).clamp()
        self.tail.move(dxy)

    def simulate(self, instructions) -> dict:
        
        tail = self
        while tail.tail:
            tail = tail.tail

        visited = {tail.head: True}
        
        for dir, stride in instructions:
            for _ in range(stride):
                self.move(dir=dir)
                visited[tail.head] = True
                
        return visited

def get_input():
    puzzle_input = ut.read_file(puzzle_input_path)
    return [(UDLR_MAP[direction], int(stride)) for direction, stride in (line.split() for line in puzzle_input)]


def part_one():

    instructions = get_input()
    rope = Rope(2)
    visited = rope.simulate(instructions=instructions)
    answer = len(visited)
    ut.print_answer(part=1, day=day, answer=answer)


def part_two():

    instructions = get_input()
    rope = Rope(10)
    visited = rope.simulate(instructions=instructions)
    answer = len(visited)
    ut.print_answer(part=2, day=day, answer=answer)


part_one()
part_two()