import ut
from ut import Position, ZERO_POS, UP, RIGHT, DOWN, LEFT


reflection_map = {
    UP: {
        '/': [RIGHT],
        '\\': [LEFT],
        '-': [RIGHT, LEFT],
        '|': [UP]
    },
    RIGHT: {
        '/': [UP],
        '\\': [DOWN],
        '-': [LEFT],
        '|': [UP, DOWN]
    },
    DOWN: {
        '/': [LEFT],
        '\\': [RIGHT],
        '-': [RIGHT, LEFT],
        '|': [DOWN]
    },
    LEFT: {
        '/': [UP],
        '\\': [DOWN],
        '-': [LEFT],
        '|': [UP, DOWN]
    }
}


def get_input():
    puzzle_input = ut.read_file()
    return [[el for el in row] for row in puzzle_input]


def in_bounds(mirror_map, pos: Position):
    in_bounds = True
    try:
        mirror_map[pos.y][pos.x]
    except:
        in_bounds = False

    return in_bounds


def reflect(direction: Position, mirror, current_pos: Position):
    return [[(current_pos + reflection), reflection] for reflection in reflection_map[direction][mirror]]

def beam(mirror_map, energized_map = {}, current_pos = ZERO_POS, direction = RIGHT):

    while in_bounds(mirror_map=mirror_map, pos=current_pos) and energized_map.get(current_pos + direction, '') == '' :
        tile_type = mirror_map[current_pos.y][current_pos.x]
        energized_map[current_pos] = 1

        if tile_type == '.':
            current_pos = current_pos + direction
        
        elif tile_type in ['|', '-', '\\', '/']:
            reflections = reflect(direction=direction, mirror=tile_type, current_pos=current_pos)

            for reflected_pos, reflected_direction in reflections:
                beam(mirror_map=mirror_map, energized_map=energized_map, current_pos=reflected_pos, direction=reflected_direction)
            
            return energized_map

    return energized_map



def print_map(energized_map):
    for x in range(9):
        for y in range(9):
            if energized_map.get(Position(x, y)) == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()    
        
        



def part_one():

    mirror_map = get_input()
    energized_map = beam(mirror_map)
    print_map(energized_map)
    answer = len(energized_map.keys())

    ut.print_answer(part=1, day='template', answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    ut.print_answer(part=2, day='template', answer=answer)


part_one()
part_two()