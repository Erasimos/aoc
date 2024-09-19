import ut
from ut import Position, UDLR
import math
import heapq


def in_bounds(graph:dict, pos: Position):
    return not graph.get(pos, '') == ''


def get_neighbors_ultra_cubicle(graph: dict, pos: Position, direction: Position, forward_counter: int):

    neighbors = []

    for new_direction in UDLR:

        new_pos = pos + new_direction

        # Out of Bounds
        if not in_bounds(graph=graph, pos=new_pos):
            continue

        # Forward
        if new_direction == direction :
            if forward_counter < 10:
                neighbors.append((new_pos, new_direction, forward_counter + 1))
            
            continue

        # Backwards not allowed
        if new_direction == -direction:
            continue

        # Right and Left
        if forward_counter >= 4 or forward_counter == 0:
            neighbors.append((new_pos, new_direction, 1))

    return neighbors


def get_neighbors_cubicle(graph: dict, pos: Position, direction: Position, forward_counter: int):

    neighbors = []

    for new_direction in UDLR:

        new_pos = pos + new_direction

        # Out of Bounds
        if not in_bounds(graph=graph, pos=new_pos):
            continue

        # Forward
        if new_direction == direction :
            if forward_counter < 3:
                neighbors.append((new_pos, new_direction, forward_counter + 1))
            
            continue

        # Backwards not allowed
        if new_direction == -direction:
            continue

        # Right and Left
        neighbors.append((new_pos, new_direction, 1))

    return neighbors

def dijsktra(graph: dict, start: Position, goal: Position, ultra_cubicle=False):

    # distance from start, node, current_direction, forward_counter
    q = [(0, start, Position(0, 0), 0)]
    distances = {(start, Position(0, 0), 0): 0}
    
    while q:

        current_distance, current_node, current_direction, forward_counter = heapq.heappop(q)

        if current_node == goal:
            if not ultra_cubicle: 
                return current_distance
            else:
                if forward_counter >= 4:
                    return current_distance
        
        if ultra_cubicle:
            neighbors = get_neighbors_ultra_cubicle(graph=graph, pos=current_node, direction=current_direction, forward_counter=forward_counter)
        else:
            neighbors = get_neighbors_cubicle(graph=graph, pos=current_node, direction=current_direction, forward_counter=forward_counter)

        for neighbor, new_direction, new_forward_counter  in neighbors:
            new_distance = current_distance + graph[neighbor]
            neighbor_state = (neighbor, new_direction, new_forward_counter)

            if new_distance < distances.get(neighbor_state, math.inf):
                distances[neighbor_state] = new_distance
                heapq.heappush(q, (new_distance, neighbor, new_direction, new_forward_counter))   

    
    return math.inf

def get_input():
    puzzle_input = ut.read_file()
    heat_map = {}
    for y, line in enumerate(puzzle_input):
        for x, row in enumerate(line):
            heat_map[Position(x, y)] = int(row)

    size_x = len(puzzle_input[0])
    size_y = len(puzzle_input)

    return heat_map, size_x, size_y


def part_one():

    heat_map, size_x, size_y = get_input()
    destination = Position(size_x - 1, size_y - 1)
    shortest_path_distance = dijsktra(graph=heat_map, start=Position(0, 0), goal=destination)
    ut.print_answer(part=1, day='template', answer=shortest_path_distance)


def part_two():

    heat_map, size_x, size_y = get_input()
    destination = Position(size_x - 1, size_y - 1)
    shortest_path_distance = dijsktra(graph=heat_map, start=Position(0, 0), goal=destination, ultra_cubicle=True)
    ut.print_answer(part=2, day='template', answer=shortest_path_distance)


part_one()
part_two()