import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from screen import AoCScreen
from ut import Vec2D
from constants import Colors


pixel_map = {'#': Colors.BLACK, '': Colors.WHITE, 'o': Colors.SAND_YELLOW}

aoc_screen = AoCScreen(pixel_map= pixel_map)

day = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day}.txt'


class Sandsystem():
    def __init__(self, rock_map: dict):
        self.rock_map = rock_map
        self.sand_pos = None
        self.abyss_y = max([pos.y for pos in rock_map.keys()])
        self.floor = self.abyss_y + 2

    def get_new_sand_pos(self):

        # Must stop on floor
        if self.sand_pos.y >= self.floor - 1: return None

        # Down
        if self.rock_map.get(self.sand_pos + Vec2D(0, 1), '.') == '.' and self.sand_pos.y < self.floor:
            return self.sand_pos + Vec2D(0, 1)

        # Left-Down
        elif self.rock_map.get(self.sand_pos + Vec2D(-1, 1), '.') == '.':
            return self.sand_pos + Vec2D(-1, 1)

        # Right-Down
        elif self.rock_map.get(self.sand_pos + Vec2D(1, 1), '.') == '.':
            return self.sand_pos + Vec2D(1, 1)

        return None

    def move_sand(self):
        self.sand_pos = Vec2D(500, 0)
        while True:
            
            if self.sand_pos.y > self.abyss_y: return False

            new_sand_pos = self.get_new_sand_pos()
            if new_sand_pos:
                self.sand_pos = new_sand_pos

            else:
                self.rock_map[self.sand_pos] = 'o'
                return True

    def move_sand_2(self):
        self.sand_pos = Vec2D(500, 0)
        while True:
            
            if self.rock_map.get(self.sand_pos, '.') == 'o':
                return False

            new_sand_pos = self.get_new_sand_pos()
            if new_sand_pos:
                self.sand_pos = new_sand_pos

            else:
                self.rock_map[self.sand_pos] = 'o'
                return True

    def fill(self):
        while self.move_sand():
            aoc_screen.render_grid(grid=self.rock_map)      
            pass

    def fill_2(self):
        while self.move_sand_2():
            aoc_screen.render_grid(grid=self.rock_map)      
            pass

def add_rock(rock_map: dict, p1: str, p2: str):
    
    p1_x, p1_y = eval(p1)
    p2_x, p2_y = eval(p2)

    for x in range(min(p1_x, p2_x), max(p1_x, p2_x) + 1):
        for y in range(min(p1_y, p2_y), max(p1_y, p2_y) + 1):
            rock_map[Vec2D(x, y)] = '#'

def get_rock_map():
    puzzle_input = ut.read_file(puzzle_input_path)
    rock_map = {}
    for line in puzzle_input: 
        for p1, p2 in zip(line.split(' -> '), line.split(' -> ')[1:]):
            add_rock(rock_map=rock_map, p1=p1, p2=p2) 
    return rock_map


def part_one():

    rock_map = get_rock_map()
    sandsystem = Sandsystem(rock_map=rock_map)
    sandsystem.fill()
    answer = sum([1 for tile in sandsystem.rock_map.values() if tile == 'o'])
    ut.print_answer(part=1, day=day, answer=answer)


def part_two():

    rock_map = get_rock_map()
    sandsystem = Sandsystem(rock_map=rock_map)
    sandsystem.fill_2()
    answer = sum([1 for tile in sandsystem.rock_map.values() if tile == 'o'])
    ut.print_answer(part=2, day=day, answer=answer)



part_one()
part_two()