import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from typing import List

day_nr = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_nr}.txt'


class Robot:
    def __init__(self, robot_factory: 'RobotFactory'):
        self.robot_factory = robot_factory
        pass

    def mine(self):
        pass

class OreRobot(Robot):
    def __init__(self, robot_factory: 'RobotFactory'):
        super().__init__(robot_factory)

    def mine(self):
        return super().mine()

class ClayRobot(Robot):
    def __init__(self, robot_factory: 'RobotFactory'):
        super().__init__(robot_factory)

    def mine(self):
        return super().mine()

class ObsidianRobot(Robot):
    def __init__(self, robot_factory: 'RobotFactory'):
        super().__init__(robot_factory)

    def mine(self):
        return super().mine()

class GeodeRobot(Robot):
    def __init__(self, robot_factory: 'RobotFactory'):
        super().__init__(robot_factory)

    def mine(self):
        return super().mine()


class RobotFactory():
    def __init__(self, id: int, costs: dict[str, int]):
        self.robots: list[Robot] = [OreRobot(self)]
        self.id = id
        self.costs = costs
        self.resources = {
            'ore': 0,
            'clay': 0,
            'obsidian': 0,
            'geodes': 0
        }


    def run(self, minutes):
        for minute in minutes:
            self.step()
        return self.get_quality_level()

    def upgrade(self):
        pass        

    def step(self):
        for robot in self.robots:
            robot.mine()

    def get_quality_level(self):
        return 9 * self.id


def get_input():
    puzzle_input = ut.read_file(puzzle_input_path)


def get_blueprint() -> dict[str, int]

def part_one():

    input = get_input()

    answer = 0

    ut.print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    ut.print_answer(part=2, day=day_nr, answer=answer)


part_one()
part_two()

# run_day()