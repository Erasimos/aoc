import os
import sys
import math
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, Vec3D, read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

def get_input():
    puzzle_input = read_file(puzzle_input_path)
    junction_boxes = set()
    for line in puzzle_input:
        x,y,z = line.split(',')
        junction_boxes.add(Vec3D(int(x),int(y),int(z)))
    return junction_boxes

def generate_junction_boxes_dist_table(junction_boxes: set[Vec3D]):

    dist_table = {}
    for junction_box in junction_boxes:
        dists = {}
        for other_junction_box in junction_boxes:

            if junction_box == other_junction_box: continue

            else:
                euclidean_distance = junction_box.euclidian_distance(other_junction_box)
                dists[other_junction_box] = euclidean_distance
        dist_table[junction_box] = dists
    return dist_table


def connect(junction_boxes: set[Vec3D], times):

    circuits = []
    dist_table = generate_junction_boxes_dist_table(junction_boxes)
    cunrrent_junction_boxes = junction_boxes

    compared_pairs = {}

    i = times
    while i > 0:

        for circuit in circuits:
            print('circuits: ', circuits)
            print('---------------------')

        min_dist = math.inf
        box_a = None
        box_b = None

        for junction_box in cunrrent_junction_boxes:
            for other_junction_box in cunrrent_junction_boxes:

                # Skip if pair already added
                if compared_pairs.get(junction_box, {}).get(other_junction_box, False):
                    continue

                if junction_box == other_junction_box: continue
                junction_dist = dist_table[junction_box][other_junction_box]
                
                if junction_dist < min_dist:
                    box_a = junction_box
                    box_b = other_junction_box
                    min_dist = junction_dist
        
        # Add to the circuits
        circuit_a = {box_a}
        circuit_b = {box_b}

        for circuit in circuits:
            
            if box_a in circuit:
                circuit_a = circuit
                
            if box_b in circuit:
                circuit_b = circuit 
        
        # Already in the same sircuit
        if circuit_a == circuit_b:
            #i -= 1
            print('Im here')

        new_circuit = circuit_a | circuit_b

        new_circuits = []
        for circuit in circuits:
            if not circuit == circuit_a and not circuit == circuit_b:
                new_circuits.append(circuit)
        new_circuits.append(new_circuit) 

        circuits = new_circuits
        i -= 1

        stuff = compared_pairs.get(box_a, {})
        stuff[box_b] = True
        compared_pairs[box_a] = stuff

    return sorted(circuits, key=len, reverse=True)

def part_one():

    junction_boxes = get_input()
    circuits = connect(junction_boxes, 10)
    print(circuits)
    
    answer = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    input = get_input()

    answer = 0
    
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
#part_two()