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
        self.sensor_range = manhattan(pos, beacon)

    def get_edge_positions(self):

        positions = []
        for y in range(self.pos.y - self.sensor_range, self.pos.y + self.sensor_range + 1):
            x_offest = self.sensor_range - abs(self.pos.y - y) + 1
            left_pos = Vec2D(self.pos.x - x_offest, y)
            right_pos = Vec2D(self.pos.x + x_offest + 1, y)
            positions.append(left_pos)
            positions.append(right_pos)

        top_pos = Vec2D(self.pos.x, self.pos.y + self.sensor_range + 1)
        bottom_pos = Vec2D(self.pos.x, self.pos.y - self.sensor_range - 1)
        positions.append(top_pos)
        positions.append(bottom_pos)

        return positions

class SensorSystem():
    def __init__(self):
        self.tunnel_map = {}
        self.sensors: List[Sensor] = []
        self.cover_ranges = {}

    def add_sensor(self, sensor: Sensor):
        self.tunnel_map[sensor.pos] = 'S'
        self.tunnel_map[sensor.beacon] = 'B'
        self.sensors.append(sensor)
        

    def find_coverage(self, y: int):

        for sensor in self.sensors:
            y_dist = manhattan(sensor.pos, Vec2D(sensor.pos.x, y))
            
            if y_dist <= sensor.sensor_range:

                half_coverage = sensor.sensor_range - y_dist
                for x in range(sensor.pos.x - half_coverage, sensor.pos.x + half_coverage + 1):
                    self.tunnel_map.setdefault(Vec2D(x, y), '#')

        return list(self.tunnel_map.values()).count('#')

    def in_range(self, pos: Vec2D):
        for sensor in self.sensors:
            if manhattan(sensor.pos, pos) <= sensor.sensor_range: return True
        return False

    def out_of_bounds(self, pos: Vec2D):
        size = 4000000
        return pos.x < 0 or pos.x > size or pos.y < 0 or pos.y > size

    def find_tuning_frequency(self):
        for sensor in self.sensors:
            for pos in sensor.get_edge_positions():
                if not self.out_of_bounds(pos) and not self.in_range(pos):
                    return (pos.x * 4000000) + pos.y
        return None
    
def get_sensor_system():
    sensor_system = SensorSystem()
    puzzle_input = ut.read_file(puzzle_input_path)
    pattern = r"x=(-?\d+), y=(-?\d+)"
    for line in puzzle_input:
        (sensor_x, sensor_y), (beacon_x, beacon_y) = re.findall(pattern, line)
        sensor_system.add_sensor(Sensor(Vec2D(int(sensor_x), int(sensor_y)), Vec2D(int(beacon_x), int(beacon_y))))
    return sensor_system


def part_one():

    sensor_system = get_sensor_system()
    answer = sensor_system.find_coverage(y=2000000)
    #day.draw_grid(grid=sensor_system.tunnel_map)
    ut.print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    sensor_system = get_sensor_system()
    answer = sensor_system.find_tuning_frequency()
    ut.print_answer(part=2, day=day_nr, answer=answer)


pixel_map = {'#': Colors.BLUE, '': Colors.WHITE, 'S': Colors.RED, 'B': Colors.GREEN}
#day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
#day.run()
part_one()
part_two()

