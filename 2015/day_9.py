import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

import ut
import math
from ut.day import Day
from ut.constants import Colors
from ut.common import Vec2D, read_file, print_answer

from ut.simulation_state import SimulationState
simulation_state = SimulationState()

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

class Edge:
    def __init__(self, destination: str, distance: int):
        self.destination = destination
        self.distance = distance

class Node:
    def __init__(self, name: str):
        self.name = name
        self.edges = []

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, node: Node):
        self.nodes[node.name] = node

    def find_shortest_route(self):
        
        shortest_route = math.inf

        for origin, node in self.nodes.items():
            visited = {}
            while len(visited.keys()) < len(self.nodes.keys()):
                


def get_input():
    puzzle_input = read_file(puzzle_input_path)
    graph = Graph()
    for line in puzzle_input:
        split_line = line.split()
        origin = split_line[0]
        destination = split_line[2]
        distance = int(split_line[4])

        edge = Edge(destination=destination, distance=distance)
        node = Node(origin)
        old_node: Node = graph.nodes.get(origin, None)

        if not old_node:
            node.add_edge(edge=edge)
            graph.add_node(node=node)
        else:
            old_node.add_edge(edge=edge)
    return graph

def part_one():

    graph = get_input()
    answer = graph.find_shortest_route()

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    print_answer(part=2, day=day_nr, answer=answer)


def run_day():
    pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
    day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
    day.run()


part_one()
part_two()

# run_day()