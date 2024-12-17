import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, Vec2DMap, read_file, print_answer, dijsktra, UDLR

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'


from copy import deepcopy

def get_input():
    puzzle_input = read_file(puzzle_input_path)
    return { Vec2D(x, y): el for y, line in enumerate(puzzle_input) for x, el in enumerate(line)}

def get_start_and_end(graph: dict):
    start = None
    end = None
    for pos, el in graph.items():
        if el == 'S':
            start = pos
        if el == 'E':
            end = pos
    return start, end

def get_neighbours(graph: dict, pos: Vec2D, current_direction: Vec2D):

    neighbours = []

    for direction in UDLR:
        if direction == Vec2D(-1, -1) * current_direction:
            continue
        else:
            n_pos = pos + direction
            if not graph.get(n_pos, '#') == '#':
                neighbours.append((n_pos, direction))
    return neighbours

def find_all_points(graph: dict, current: Vec2D, end: Vec2D, direction: Vec2D, shortest_distance: int, distance: int, visited: dict, walked: dict):

    if visited.get(current, False): 
        return False

    visited[current] = True

    if current == end:
        walked[current] = True
        return True
    else:

        for n_direction in UDLR:
            if n_direction == Vec2D(-1, -1) * direction:
                continue

            new_distance = distance + 1
            if not n_direction == direction:
                new_distance += 100

            if new_distance > shortest_distance:
                continue

            n_pos = current + n_direction

            if visited.get(n_pos, False):
                continue

            if graph.get(n_pos, '#') == '#':
                continue

            if find_all_points(graph=graph, current=n_pos, end=end, direction=n_direction, shortest_distance=shortest_distance, distance=new_distance, visited=visited, walked=walked):
                walked[current] = True                 
    
    return walked.get(current, False)

def find_all_paths_of_distance(graph: dict, current: Vec2D, end: Vec2D, direction: Vec2D, shortest_distance: int, path: list, distance: int):

    if current == end:
        return [path]
    
    if distance >= shortest_distance:
        return []

    else:
        
        new_paths = []
        
        for n_direction in UDLR:
            if n_direction == Vec2D(-1, -1) * direction:
                continue
            else:

                n_pos = current + n_direction

                if graph.get(n_pos, '#') == '#':
                    continue

                new_distance = distance + 1
                if not n_direction == direction:
                    new_distance += 1000

                if new_distance > shortest_distance:
                    continue

                if n_pos in path: 
                    continue


                new_path = deepcopy(path)
                new_path.append(n_pos)
                new_paths += find_all_paths_of_distance(graph=graph, current=n_pos, end=end, direction=n_direction, shortest_distance=shortest_distance, path=new_path, distance=new_distance)

        return new_paths

def part_one():

    maze = get_input()
    start, end = get_start_and_end(graph=maze)
    answer = dijsktra(graph=maze, get_neighbours=get_neighbours, start=start, goal=end, direction=Vec2D(1, 0))

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    maze = get_input()
    start, end = get_start_and_end(graph=maze)
    shortest_path_dist = dijsktra(graph=maze, get_neighbours=get_neighbours, start=start, goal=end, direction=Vec2D(1, 0))
    all_shortest_paths = find_all_paths_of_distance(graph=maze, current=start, end=end, direction=Vec2D(1, 0), shortest_distance=shortest_path_dist, path=[start], distance=0)
    print(all_shortest_paths)
    shortest_path_positions = {}

    for path in all_shortest_paths:
        for pos in path:
            shortest_path_positions[pos] = True
    #walked = {start: True}
    #visited = {}
    #find_all_points(graph=maze, current=start, end=end, direction=Vec2D(1, 0), shortest_distance=shortest_path_dist, distance=0, visited=visited, walked=walked)
    answer = len(shortest_path_positions.keys())
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()