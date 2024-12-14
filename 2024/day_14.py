import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)
from typing import List
from ut.common import Vec2D, read_file, print_answer
import re

from ut.simulation_state import SimulationState
simulation_state = SimulationState()


day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

class Robot:
    def __init__(self, pos: Vec2D, vel: Vec2D):
        self.pos = pos
        self.vel = vel

    def move(self, room_w: int, room_h: int):
        new_x = (self.pos.x + self.vel.x) % room_w
        new_y = (self.pos.y + self.vel.y) % room_h
        self.pos = Vec2D(new_x, new_y)

    def get_quadrant(self, room_w: int, room_h: int):

        mid_x = int((room_w - 1) / 2)
        mid_y = int((room_h - 1) / 2)

        if self.pos.x < mid_x:

            if self.pos.y < mid_y:
                return 3
            
            if self.pos.y > mid_y:
                return 1
            
        if self.pos.x > mid_x:

            if self.pos.y < mid_y:
                return 4
            
            if self.pos.y > mid_y:
                return 2

        return 0

class Bathroom:
    def __init__(self, height: int, width: int, robots: List[Robot]):
        self.h = height
        self.w = width
        self.robots = robots
        self.max_middle = 0

    def elapse_time(self, time: int):
        for _ in range(time):
            for robot in self.robots:
                robot.move(room_w=self.w, room_h=self.h)

    def quadrant_count(self):
        q_counts = {}

        for robot in self.robots:
            q = robot.get_quadrant(room_w=self.w, room_h=self.h)
            q_counts[q] = q_counts.get(q, 0) + 1
        
        return q_counts

    def get_safety_factor(self):

        q_counts = {}

        for robot in self.robots:
            q = robot.get_quadrant(room_w=self.w, room_h=self.h)
            q_counts[q] = q_counts.get(q, 0) + 1

        return q_counts[1] * q_counts[2] * q_counts[3] * q_counts[4]



    def print_bathroom(self, i: int):

        q_count = self.quadrant_count()
        q_tolerance = 250

        if q_count[1] > q_tolerance or q_count[2] > q_tolerance or q_count[3] > q_tolerance or q_count[4] > q_tolerance:

            self.max_middle = q_count[0]
            
            print('elapsed_time: ', i)

            for y in range(self.h):
                for x in range(self.w):
                    is_robot = False
                    for robot in self.robots:
                        if Vec2D(x, y) == robot.pos:
                            print('X', end='')
                            is_robot = True
                            break
                    if not is_robot:
                        print(' ', end='')
                print()
            print()
            print()
        

        

def get_input():
    puzzle_input = read_file(puzzle_input_path)
    pattern = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
    robots = []
    for line in puzzle_input:
        px, py, vx, vy = map(int, pattern.match(line).groups())
        robots.append(Robot(pos=Vec2D(px, py), vel=Vec2D(vx, vy)))
    return robots

def part_one():

    robots = get_input()
    
    bathroom = Bathroom(height=103, width=101, robots=robots)
    bathroom.elapse_time(100)
    answer = bathroom.get_safety_factor()
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():


    robots = get_input()
    
    bathroom = Bathroom(height=103, width=101, robots=robots)
    for i in range(155034):
        bathroom.elapse_time(1)
        bathroom.print_bathroom(i)    
    answer = 0
    
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()
