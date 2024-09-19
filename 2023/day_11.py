import ut


def expand_galaxy(galaxy_map):
    
    expanded_galaxy_map = []

    # iterate rows
    for row in galaxy_map:

        expanded_galaxy_map.append(row)

        if row.count('.') == len(row):
            expanded_galaxy_map.append(''.join(['.' for i in range(len(row))]))

    # iterate columns
    transposed_map = [''.join([row[i] for row in expanded_galaxy_map]) for i in range(len(expanded_galaxy_map[0]))]


    expanded_galaxy_map = []

    for row in transposed_map:

        expanded_galaxy_map.append(row)

        if row.count('.') == len(row):
            expanded_galaxy_map.append(''.join(['.' for i in range(len(row))]))

    expanded_galaxy_map = [''.join([row[i] for row in expanded_galaxy_map]) for i in range(len(expanded_galaxy_map[0]))]

    return expanded_galaxy_map

def get_galaxies(galaxy_map):
    galaxies = []

    for y, row in enumerate(galaxy_map):
        for x, el in enumerate(row):
            if el == '#':
                galaxies.append((x, y))

    return galaxies

def galaxy_distance(galaxy_1, galaxy_2):

    x_dist = abs(galaxy_1[0] - galaxy_2[0])
    y_dist = abs(galaxy_1[1] - galaxy_2[1])

    return x_dist + y_dist



def galaxy_distance_2(galaxy_1, galaxy_2, galaxy_map):

    total_distance = 0
    
    # step x
    current_x = galaxy_1[0]
    x_diff = 1 if galaxy_1[0] < galaxy_2[0] else -1
    while not current_x == galaxy_2[0]:

        space_column = ''.join([row[current_x] for row in galaxy_map])
        if space_column.count('.') == len(space_column):
            
            total_distance += 1000000
        else:
            total_distance += 1
        
        current_x += x_diff

    # step y
    current_y = galaxy_1[1]
    y_diff = 1 if galaxy_1[1] < galaxy_2[1] else -1
    while not current_y == galaxy_2[1]:

        space_row = galaxy_map[current_y] 
        if space_row.count('.') == len(space_row):
            
            total_distance += 1000000
        else:
            total_distance += 1
        
        current_y += y_diff

    return total_distance


def part_one():

    puzzle_input = ut.read_file()
    expanded_galaxy_map = expand_galaxy(puzzle_input)
    galaxies = get_galaxies(expanded_galaxy_map)
    
    # sum of distances
    answer = 0
    for i, g_1 in enumerate(galaxies):
        for g_2 in galaxies[i+1:]:
            answer += galaxy_distance(g_1, g_2)
            


    ut.print_answer(part=1, day='template', answer=answer)


def part_two():

    galaxy_map = ut.read_file()
    galaxies = get_galaxies(galaxy_map)

    # sum of distances
    answer = 0
    for i, g_1 in enumerate(galaxies):
        for g_2 in galaxies[i+1:]:
            answer += galaxy_distance_2(galaxy_1=g_1, galaxy_2=g_2, galaxy_map=galaxy_map)
            
    ut.print_answer(part=2, day='template', answer=answer)


part_one()
part_two()