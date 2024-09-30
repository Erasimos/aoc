import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
from constants import Colors
from day import Day
from ut import Vec3D
import ut
import heapq

day_nr = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_nr}.txt'


def get_lava_grid():
    return {Vec3D(int(coords[0]), int(coords[1]), int(coords[2])): '#' for line in ut.read_file(puzzle_input_path) if (coords := line.split(','))}


def get_surface_area(lava_grid: dict[Vec3D, str]):
    return [lava_grid.get(neighbour, '.') for pos in lava_grid.keys() for neighbour in pos.neighbours()].count('.')


def part_one():

    lava_grid = get_lava_grid()
    answer = get_surface_area(lava_grid=lava_grid)
    ut.print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    lava_grid = get_lava_grid()
    answer = get_surface_area(lava_grid=lava_grid)
    ut.print_answer(part=2, day=day_nr, answer=answer)


def run_day():
    pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
    day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
    day.run()


part_one()
part_two()

# run_day()