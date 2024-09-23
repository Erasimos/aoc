import os
import sys
from pathlib import Path
from typing import Callable
sys.path.append(os.getcwd() + '/ut')
from ut import Vec2D, UDLR
import ut
import heapq
import math

day = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day}.txt'

def get_heightmap():
    puzzle_input = ut.read_file(puzzle_input_path)

    heightmap = {}
    for y, line in enumerate(puzzle_input):
        for x, row in enumerate(line):
            if row == 'S':
                height = 0
                start = Vec2D(x, y)
            elif row == 'E':
                height = ord('z') - ord('a')
                goal = Vec2D(x, y)
            else:
                height = ord(row) - ord('a')

            heightmap[Vec2D(x, y)] = height

    size_x = len(puzzle_input[0])
    size_y = len(puzzle_input)

    return heightmap, start, goal


def in_bounds(graph:dict, pos: Vec2D):
    return not graph.get(pos, '') == ''

def get_neighbours(graph: dict, pos: Vec2D):
    
    neighbors = []

    for new_direction in UDLR:

        new_pos = pos + new_direction

        # Out of Bounds
        if not in_bounds(graph=graph, pos=new_pos):
            continue
        
        if graph[new_pos] - graph[pos] <= 1:
            neighbors.append(new_pos)

    return neighbors

def dijsktra(graph: dict, start: Vec2D, goal: Vec2D):

    # distance from start, node
    q = [(0, start)]
    distances = {start: 0}
    
    while q:

        current_distance, current_node = heapq.heappop(q)

        if current_node == goal:
            return current_distance
        
    
        neighbors = get_neighbours(graph=graph, pos=current_node)

        for neighbor in neighbors:
            new_distance = current_distance + 1

            if new_distance < distances.get(neighbor, math.inf):
                distances[neighbor] = new_distance
                heapq.heappush(q, (new_distance, neighbor))

    return math.inf


def part_one():

    heigthmap, start, goal = get_heightmap()

    answer = dijsktra(graph=heigthmap, start=start, goal=goal)

    ut.print_answer(part=1, day=day, answer=answer)


def part_two():

    heigthmap, start, goal = get_heightmap()

    starting_positions = [pos for pos, height in heigthmap.items() if height == 0]
    
    answer = min([dijsktra(graph=heigthmap, start=start_pos, goal=goal) for start_pos in starting_positions])

    ut.print_answer(part=2, day=day, answer=answer)


part_one()
part_two()