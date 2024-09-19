import ut
from ut import Position, UDLR
import copy
from collections import deque

DIRECTION_MAP = {
    'U': Position(0, -1),
    'R': Position(1, 0),
    'D': Position(0, 1),
    'L': Position(-1, 0)
}

DIRECTION_MAP_2 = {
    '0': Position(1, 0),
    '1': Position(0, 1),
    '2': Position(-1, 0),
    '3': Position(0, -1)
}

def get_input():
    puzzle_input = ut.read_file()
    dig_plan = []
    for line in puzzle_input:
        split_line = line.split()
        dig_insctruction = {
            'direction': DIRECTION_MAP[split_line[0]],
            'size': int(split_line[1]),
            'hex': split_line[2]
        }

        dig_plan.append(dig_insctruction)

    return dig_plan


def get_input_part_two():
    puzzle_input = ut.read_file()
    dig_plan = []
    for line in puzzle_input:
        split_line = line.split()
        hex_code = split_line[2][-2]
        dist_hex = split_line[2][2:-2]

        dig_insctruction = {
            'direction': DIRECTION_MAP_2[hex_code],
            'size': int(dist_hex, 16)
        }

        dig_plan.append(dig_insctruction)

    return dig_plan


def print_terrain(terrain, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            tile = terrain.get(Position(x, y), '.')
            print(tile, end='')
        print()


def dig(dig_plan):

    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0

    position = Position(0, 0)
    terrain = {}
    
    for dig_instruction in dig_plan:
        direction = dig_instruction['direction']
        size = dig_instruction['size']

        for i in range(size):
            position = position + direction
            terrain[position] = '#'

            max_x = max(max_x, position.x)
            min_x = min(min_x, position.x)
            max_y = max(max_y, position.y)
            min_y = min(min_y, position.y)

    terrain_size = {
        'max_x': max_x,
        'min_x': min_x,
        'max_y': max_y,
        'min_y': min_y
    }

    terrain[Position(0, 0)] = '#'
    return terrain, terrain_size


def get_lagoon_size(terrain: dict, min_x, max_x, min_y, max_y):

    filled_terrain_min_x = min_x - 1
    filled_terrain_max_x = max_x + 1

    filled_terrain_min_y = min_y - 1
    filled_terrain_max_y = max_y + 1

    start_pos = Position(filled_terrain_min_x, filled_terrain_min_y)

    unfilled_spaces = deque([start_pos])
    filled_spaces = 0

    while unfilled_spaces:
        
        current_pos = unfilled_spaces.popleft()
        terrain[current_pos] = 'F'
        filled_spaces += 1

        for direction in UDLR:
            neighbor = current_pos + direction
            if terrain.get(neighbor, '.') in ['#', 'F'] or neighbor.x < filled_terrain_min_x or neighbor.x > filled_terrain_max_x or neighbor.y < filled_terrain_min_y or neighbor.y > filled_terrain_max_y:
                continue
            else:
                if neighbor not in unfilled_spaces:
                    unfilled_spaces.append(neighbor)

    filled_spaces = abs(filled_terrain_max_x - filled_terrain_min_x + 1) * abs(filled_terrain_max_y - filled_terrain_min_y  + 1) - filled_spaces
    
    return filled_spaces
    


def part_one():

    dig_plan = get_input()
    terrain, terrain_size = dig(dig_plan=dig_plan)
    answer = get_lagoon_size(terrain=terrain, min_x=terrain_size['min_x'], max_x=terrain_size['max_x'], min_y=terrain_size['min_y'], max_y=terrain_size['max_y'])

    ut.print_answer(part=1, day='template', answer=answer)


def part_two():

    dig_plan = get_input_part_two()
    terrain, terrain_size = dig(dig_plan=dig_plan)
    answer = get_lagoon_size(terrain=terrain, min_x=terrain_size['min_x'], max_x=terrain_size['max_x'], min_y=terrain_size['min_y'], max_y=terrain_size['max_y'])
    ut.print_answer(part=2, day='template', answer=answer)


part_one()

part_two()