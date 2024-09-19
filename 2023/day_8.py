import ut


def get_instructions():

    puzzle_input = ut.read_file()
    instructions = puzzle_input[0]

    return instructions

def get_map():

    puzzle_input = ut.read_file()
    links = [el.split() for el in puzzle_input[2:]]
    wasteland_map = {}

    

    for link in links:
        source_node = link[0]
        left_node = link[2].replace('(', '').replace(',', '')
        right_node = link[3].replace(')', '')

        wasteland_map[source_node] = (left_node, right_node)

    return wasteland_map

def is_start_node(node):
    return node[-1] == 'A'

def is_end_node(node):
    return node[-1] == 'Z'

def find_starting_nodes(wasteland_map: dict):

    starting_nodes = []

    for node in wasteland_map.keys():
        if is_start_node(node):
            starting_nodes.append(node)

    return starting_nodes

def traverse_parallel(instructions, wasteland_map):

    current_nodes = find_starting_nodes(wasteland_map)
    steps = 0
    instruction_index = 0

    while not all(is_end_node(node) for node in current_nodes):

        instruction = instructions[instruction_index]

        new_current_nodes = []

        if instruction == 'L':
            for current_node in current_nodes:
                new_current_nodes.append(wasteland_map[current_node][0])

        elif instruction == 'R':
            for current_node in current_nodes:
                new_current_nodes.append(wasteland_map[current_node][1])

        steps += 1
        if (steps % 1000) == 0:
            print('steps: ', steps)
        current_nodes = new_current_nodes
        instruction_index = (instruction_index + 1) % len(instructions)   
        
    return steps

def find_loop(instructions, wasteland_map):
    starting_node = find_starting_nodes(wasteland_map)[0]
    steps = 0
    instruction_index = 0

    while not is_end_node(starting_node):

        print(current_node)

        instruction = instructions[instruction_index]

        new_current_nodes = []

        if instruction == 'L':
            for current_node in current_nodes:
                new_current_nodes.append(wasteland_map[current_node][0])

        elif instruction == 'R':
            for current_node in current_nodes:
                new_current_nodes.append(wasteland_map[current_node][1])

        steps += 1
        current_nodes = new_current_nodes
        instruction_index = (instruction_index + 1) % len(instructions)   
        
    return steps

def traverse(instructions, wasteland_map):
    current_node = 'AAA'
    goal = 'ZZZ'
    steps = 0
    
    instruction_index = 0

    while not current_node == goal:
        instruction = instructions[instruction_index]

        if instruction == 'L':
            current_node = wasteland_map[current_node][0]

        elif instruction == 'R':
            current_node = wasteland_map[current_node][1]

        steps += 1
        instruction_index = (instruction_index + 1) % len(instructions)

    return steps



def part_one():

    instructions = get_instructions()
    wasteland_map = get_map()

    steps = traverse(instructions, wasteland_map)

    ut.print_answer(part=1, day='8', answer=steps)


def part_two():

    instructions = get_instructions()
    wasteland_map = get_map()

    steps = traverse_parallel(instructions, wasteland_map)

    ut.print_answer(part=2, day='8', answer=steps)



#part_one()
part_two()