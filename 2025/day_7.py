import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

class LaserSim():
    def __init__(self, laser_map: dict):
        self.laser_map = laser_map
        self.splits = 0
        self.lasers = {}
        self.visits = {}
        self.timeline_counts = {}
        for key, value in self.laser_map.items():
            if value == 'S':
                self.lasers[key] = True
                self.visits[key] = 1
                self.laser_map[key] == '.'     
    
    def step_simulation(self):
        
        new_lasers = {}
        for laser_pos in self.lasers.keys():

            # move laser
            new_laser_pos = laser_pos + Vec2D(0, 1)

            tile = self.laser_map.get(new_laser_pos, None)
            # out of bonds
            if not tile:
                self.timeline_counts[laser_pos] = self.visits.get(laser_pos, 0)
                continue

            # splitter
            elif tile == '^':
                self.splits += 1
                new_laser_pos_left = new_laser_pos + Vec2D(-1, 0)
                new_laser_pos_right = new_laser_pos + Vec2D(1, 0)
                new_lasers[new_laser_pos_left] = True
                new_lasers[new_laser_pos_right] = True
                self.visits[new_laser_pos_left] = self.visits.get(laser_pos, 0) + self.visits.get(new_laser_pos_left, 0)
                self.visits[new_laser_pos_right] = self.visits.get(laser_pos, 0) + self.visits.get(new_laser_pos_right, 0)

            elif tile == '.':
                new_lasers[new_laser_pos] = True
                self.visits[new_laser_pos] = self.visits.get(laser_pos, 0) + self.visits.get(new_laser_pos, 0)

        self.lasers = new_lasers

    def run_simulation(self):
        while self.lasers:
            self.step_simulation()
        

def get_input():
    puzzle_input = read_file(puzzle_input_path)
    laser_map = {}
    for y, line in enumerate(puzzle_input):
        for x, el in enumerate(line):
            laser_map[Vec2D(x, y)] = el  
    return laser_map

def part_one():

    laser_map = get_input()
    laser_sim = LaserSim(laser_map=laser_map)
    laser_sim.run_simulation()
    answer = laser_sim.splits
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    laser_map = get_input()
    laser_sim = LaserSim(laser_map=laser_map)
    laser_sim.run_simulation()
    answer = sum(laser_sim.timeline_counts.values())
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()