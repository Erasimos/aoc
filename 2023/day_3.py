import ut
from ut import Position, LEFT, RIGHT, NEIGHBORS_2D


def get_input():
    puzzle_input = ut.read_file()
    return puzzle_input


def is_part_number(schematics:dict, pos: Position):

    if not schematics.get(pos, '').isnumeric():
        return [], 0

    part_number_positions = []
    part_number = ''
    current_position = pos
    
    # step left
    while schematics.get(current_position, '').isnumeric():
        part_number_positions.append(current_position)
        part_number = schematics[current_position] + part_number
        current_position = current_position + LEFT

    # step right    
    current_position = pos + RIGHT
    while schematics.get(current_position, '').isnumeric():
        part_number_positions.append(current_position)
        part_number = part_number + schematics[current_position]
        current_position = current_position + RIGHT


    for pos in part_number_positions:
        for neighbor in NEIGHBORS_2D:
            n_pos = pos + neighbor
            tile_type = schematics.get(n_pos, '.')
            if not tile_type.isnumeric() and not tile_type == '.':
                return part_number_positions, int(part_number)

    return [], 0


def get_schematics():
    puzzle_input = ut.read_file()
    schematics = {}
    gears = []
    for y, line in enumerate(puzzle_input):
        for x, element in enumerate(line):
            schematics[Position(x, y)] = element

            if element == '*':
                gears.append(Position(x, y))

    return schematics, gears


def get_part_numbers(schematics: dict):

    part_numbers = {}
    for pos in schematics.keys():
        part_number_positions, part_number = is_part_number(schematics=schematics, pos=pos)
        if part_number_positions:
            part_numbers[part_number] = part_number_positions        

    return part_numbers

def get_gear_ratio_sum(schematics, gears):

    gear_ratio_sum = 0
    
    for gear in gears:

        part_numbers = []
        neighbors = [gear + n_dir for n_dir in NEIGHBORS_2D]

        while neighbors:
            neighbor = neighbors.pop()

            part_number_positions, part_number = is_part_number(schematics=schematics, pos=neighbor)

            if part_number_positions:
                part_numbers.append(part_number)
                neighbors = [item for item in neighbors if item not in part_number_positions]

        if len(part_numbers) == 2:
            gear_ratio_sum += part_numbers[0] * part_numbers[1]  
    
    return gear_ratio_sum

    
def part_one():

    schematics, gears = get_schematics()
    part_numbers = get_part_numbers(schematics=schematics)
    answer = sum(part_numbers.keys())
    print(part_numbers.keys())
    ut.print_answer(part=1, day='template', answer=answer)


def part_two():

    schematics, gears = get_schematics()

    answer = get_gear_ratio_sum(schematics=schematics, gears=gears)
    
    ut.print_answer(part=2, day='template', answer=answer)


part_one()
part_two()