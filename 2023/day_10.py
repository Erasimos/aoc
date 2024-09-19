import ut

pipe_map_size_y = None
pipe_map_size_x = None
original_map = None
S_type = '|'

def set_start_neighbours(start_pos, pipe_map: dict):

    global original_map
    
    neighbours = []

    for neighbour in ut.Neighbours_2D:

        start_neighbour = (start_pos[0] + neighbour[0], start_pos[1] + neighbour[1]) 
        
        if start_pos in pipe_map.get(start_neighbour, []):
            neighbours.append(start_neighbour)

    pipe_map[start_pos] = neighbours

def get_pipe_map():
    global original_map
    puzzle_input = ut.read_file('input.txt')
    original_map = puzzle_input
    start_pos = None
    pipe_map = {}

    global pipe_map_size_y, pipe_map_size_x
    pipe_map_size_y = (len(puzzle_input))
    pipe_map_size_x = len(puzzle_input[0])

    for row_index, row in enumerate(puzzle_input):

        for column_index, tile in enumerate(row):

            pos = (row_index, column_index)

            neighbours = []

            if tile == '|':
                neighbours = [(row_index + 1, column_index), (row_index - 1, column_index)]

            elif tile == '-':
                neighbours = [(row_index, column_index + 1), (row_index, column_index - 1)]

            elif tile == 'L':
                neighbours = [(row_index - 1, column_index), (row_index, column_index + 1)]

            elif tile == 'J':
                neighbours = [(row_index - 1, column_index), (row_index, column_index - 1)]

            elif tile == '7':
                neighbours = [(row_index + 1, column_index), (row_index, column_index - 1)]

            elif tile == 'F':
                neighbours = [(row_index + 1, column_index), (row_index, column_index + 1)]

            elif tile == '.':
                neighbours = []

            elif tile == 'S':
                start_pos = (row_index, column_index)

            pipe_map[pos] = neighbours

    set_start_neighbours(start_pos=start_pos, pipe_map=pipe_map)

    return pipe_map, start_pos

def traverse_loop(pipe_map: dict, start_pos):
    pipe_map_distances = {}
    pipe_map_distances[start_pos] = 0
    

    # Loop 1
    looped = False
    steps = 0
    current_pos = start_pos
    prev_pos = pipe_map[start_pos][0]

    while not looped:

        neighbours = pipe_map[current_pos]

        if not neighbours[0] == prev_pos:
            prev_pos = current_pos
            current_pos = neighbours[0]
            
        else:
            prev_pos = current_pos
            current_pos = neighbours[1]

        if current_pos == start_pos:
            looped = True        
        
        else:
            steps += 1
            pipe_map_distances[current_pos] = steps


    # Loop 2
    looped = False
    steps = 0
    current_pos = start_pos
    prev_pos = pipe_map[start_pos][1]

    while not looped:

        neighbours = pipe_map[current_pos]
        if not neighbours[0] == prev_pos:
            prev_pos = current_pos
            current_pos = neighbours[0]
            
        else:
            prev_pos = current_pos
            current_pos = neighbours[1]

        if current_pos == start_pos:
            looped = True   

        else:
            steps += 1
            if steps < pipe_map_distances[current_pos]: 
                pipe_map_distances[current_pos] = steps


    
    return pipe_map_distances


def out_of_bounds(pos):
    global pipe_map_size_y, pipe_map_size_x

    if pos[0] < 0 or pos[0] >= pipe_map_size_y:
        return True
    
    if pos[1] < 0 or pos[1] >= pipe_map_size_x:
        return True

    return False


def raycast(pipe_map: dict, pipe_map_distances: dict, current_pos, direction):

    global original_map
    intersections = 0
    previous_turn = None
    
    while True:

            new_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
            

            if out_of_bounds(new_pos):
                break
            else:


                # Check intersection
                
                tile_type = original_map[new_pos[0]][new_pos[1]]

                if tile_type == 'S':
                    tile_type = S_type

                if current_pos not in pipe_map[new_pos] and tile_type in ['-', '|'] and new_pos in pipe_map_distances.keys():
                    intersections += 1

                current_pos = new_pos

                if current_pos in pipe_map_distances.keys() and tile_type in ['L', 'J', '7', 'F']:
                    if previous_turn == 'L' and tile_type == '7' and direction in [(0, 1), (-1, 0)]:
                        intersections += 1
                    elif previous_turn == '7' and tile_type == 'L' and direction in [(0, -1), (1, 0)]:
                        intersections += 1
                    elif previous_turn == 'J' and tile_type == 'F' and direction in [(0, -1), (-1, 0)]:
                        intersections += 1
                    elif previous_turn == 'F' and tile_type == 'J' and direction in [(0, 1), (1, 0)]:
                        intersections += 1

                    previous_turn = tile_type                    

    return intersections

def find_eclosed_tiles(pipe_map: dict, pipe_map_distances: dict):

    enclosed_tiles = 0
    print(pipe_map_distances.keys())


    for tile in pipe_map.keys():

        

        if tile in pipe_map_distances.keys():
            continue

        print('tileDFGD: ', tile)

        enclosed = True
        
        

        for direction in ut.UDLR:
            
            intersections = raycast(pipe_map=pipe_map, pipe_map_distances=pipe_map_distances, direction=direction, current_pos=tile)
            if intersections % 2 == 0:
                enclosed = False
            
            print('intersections:', intersections)
        
        if enclosed:
            enclosed_tiles += 1
            print('tile: ', tile)

    return enclosed_tiles

def part_one():

    pipe_map, start_pos = get_pipe_map()

    pipe_map_distances: dict = traverse_loop(pipe_map=pipe_map, start_pos=start_pos)
    answer = max(pipe_map_distances.values())

    ut.print_answer(part=1, day='template', answer=answer)


def part_two():

    pipe_map, start_pos = get_pipe_map()

    pipe_map_distances: dict = traverse_loop(pipe_map=pipe_map, start_pos=start_pos)
    answer = find_eclosed_tiles(pipe_map=pipe_map, pipe_map_distances=pipe_map_distances)

    ut.print_answer(part=2, day='template', answer=answer)


part_one()
part_two()