import ut

def anlalyze_sequence(sequence):

    layers = [sequence]

    while not all(el == 0 for el in layers[-1]):
        new_layer = []
        old_layer = layers[-1]

        for i in range(len(old_layer) - 1):
            new_el = old_layer[i + 1] - old_layer[i]
            new_layer.append(new_el)

        layers.append(new_layer)
    

    return layers

def extrapolate_sequence(layers):

    bottom_layer = layers[-1]
    new_bottom_layer = bottom_layer + [0]
    new_layers = [new_bottom_layer]

    for layer_index in reversed(range(len(layers) - 1)):
        new_element = new_layers[0][-1] + layers[layer_index][-1]
        new_layer = layers[layer_index] + [new_element]
        new_layers = [new_layer] + new_layers

    return new_layers

def extrapolate_sequence_backwards(layers):

    bottom_layer = layers[-1]
    new_bottom_layer = [0] + bottom_layer
    new_layers = [new_bottom_layer]

    for layer_index in reversed(range(len(layers) - 1)):

        new_element = layers[layer_index][0] - new_layers[0][0]
        new_layer = [new_element] + layers[layer_index]
        new_layers = [new_layer] + new_layers

    return new_layers


def get_sequences():
    puzzle_input = ut.read_file('new_input.txt')
    sequences = [[int(el) for el in line.split()] for line in puzzle_input]
    return sequences

def part_one():

    sequences = get_sequences()
    
    answer = 0

    for sequence in sequences:
        layers = anlalyze_sequence(sequence)
        new_layers = extrapolate_sequence(layers)

        answer += new_layers[0][-1]

    ut.print_answer(part=1, day='template', answer=answer)


def part_two():
   
    sequences = get_sequences()
    
    answer = 0

    for sequence in sequences:
        layers = anlalyze_sequence(sequence)
        new_layers = extrapolate_sequence_backwards(layers)

        answer += new_layers[0][0]

    ut.print_answer(part=2, day='template', answer=answer)

part_one()
part_two()