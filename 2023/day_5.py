import ut
import math

def get_input():
    
    seeds = ut.read_file('input2.txt')
    seeds = [int(item) for item in seeds[0].split()[1:]]

    puzzle_input = ut.read_file_raw().split('\n\n')
    plant_maps = {}

    for chunk in puzzle_input:
        
        split_line = chunk.split('\n')
        split_line = split_line[0].split('-')
        source = split_line[0]

        plant_map = {
            'source': source,
            'to': split_line[-1].split()[0]
        }

        ranges = []
        for line in chunk.split('\n')[1:]:
            split_line = line.split()
            map_range = {
                'source_start': int(split_line[1]),
                'destination_start': int(split_line[0]),
                'range_length': int(split_line[2])
            }
            ranges.append(map_range)    

        plant_map['ranges'] = ranges
        plant_maps[source] = plant_map


    return seeds, plant_maps


def get_seed_location(plant_maps: dict, seed):

    current_map = 'seed'
    source = seed

    while not current_map == 'location':

        for map_range in plant_maps[current_map]['ranges']:
            if source >= map_range['source_start'] and source <= (map_range['source_start'] + map_range['range_length']):
                offset = source - map_range['source_start']
                source = map_range['destination_start'] + offset
                break

        current_map = plant_maps[current_map]['to']

    return source

def part_one():

    seeds, plant_maps = get_input()
    seed_locations = [get_seed_location(plant_maps=plant_maps, seed=seed) for seed in seeds]    
    answer = min(seed_locations)

    ut.print_answer(part=1, day=5, answer=answer)


def part_two():

    seeds, plant_maps = get_input()
    seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

    answer = math.inf

    for seed_start, seed_range in seed_ranges:
        print(seed_range)
        for i in range(seed_range):
            seed = seed_start + i
            seed_location = get_seed_location(plant_maps=plant_maps, seed=seed)
            print('SEED: ', seed_location)
            answer = min(answer, seed_location)
            
    
    ut.print_answer(part=2, day=5, answer=answer)


part_one()
part_two()