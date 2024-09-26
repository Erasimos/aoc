import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from constants import Colors
from day import Day
from ut import Vec2D, manhattan
from typing import List
import math
import re

day_nr = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_nr}.txt'

class Sensor():
    def __init__(self, pos: Vec2D, beacon: Vec2D):
        self.pos = pos
        self.beacon = beacon

    def find_coverage(self, y: int):
        range = manhattan(self.pos, self.beacon)
        y_dist = manhattan(self.pos, Vec2D(self.pos.x, y))
        
        if y_dist <= range:
            coverage = 1 + (2 *range) - (2 * y_dist)
        else :
            return 0

        if self.beacon.y == y:
            coverage -= 1
        
        if self.pos.y == y:
            coverage -= 1
        

        return coverage


def get_sensors():
    sensors = []
    puzzle_input = ut.read_file(puzzle_input_path)
    pattern = r"x=(-?\d+), y=(-?\d+)"
    for line in puzzle_input:
        (sensor_x, sensor_y), (beacon_x, beacon_y) = re.findall(pattern, line)
        sensors.append(Sensor(Vec2D(int(sensor_x), int(sensor_y)), Vec2D(int(beacon_x), int(beacon_y))))
    
    return sensors


def part_one():

    sensors = get_sensors()

    answer = sum([sensor.find_coverage(y=10) for sensor in sensors])

    ut.print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    ut.print_answer(part=2, day=day_nr, answer=answer)


#pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
#day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
#day.run()
part_one()

