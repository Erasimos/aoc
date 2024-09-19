import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut
from ut import Vec2D, UDLR
from operator import mul
from functools import reduce


day = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day}.txt'


def get_input():
    puzzle_input = ut.read_file(puzzle_input_path)
    tree_map = {Vec2D(x, y): tree for y, line in enumerate(puzzle_input) for x, tree in enumerate(line)}
    return tree_map


def is_edge(tree_map: dict, pos: Vec2D):
    return any([tree_map.get(npos) == None for npos in pos.neighbors_orthogonal()])


def get_scenic_score(tree_map: dict[Vec2D, int], pos: Vec2D):

    viewing_distances = []

    for n_dir in UDLR:
        
        tree_height = tree_map.get(pos)
        current_pos = pos + n_dir
        viewing_distance = 0

        while not tree_map.get(current_pos, None) == None:
            viewing_distance += 1

            if tree_height <= tree_map[current_pos]:
                break

            current_pos += n_dir

        viewing_distances.append(viewing_distance)

    a = reduce(mul, viewing_distances, 1)
    return a


def count_visible_trees(tree_map: dict[Vec2D, int]):
    
    num_visible_trees = 0

    for tree_pos, tree_height in tree_map.items():

        for n_dir in UDLR:
            
            current_pos = tree_pos
            visible = True

            while True:

                current_pos += n_dir

                if tree_map.get(current_pos, None) == None:
                    break
                elif tree_map.get(current_pos, None) >= tree_height:
                    visible = False
                    break

            if visible:
                num_visible_trees += 1
                break

    return num_visible_trees

def part_one():

    tree_map = get_input()

    answer = count_visible_trees(tree_map=tree_map)
    ut.print_answer(part=1, day=day, answer=answer)

def part_two():

    tree_map = get_input()

    answer = max([get_scenic_score(tree_map=tree_map, pos=tree_pos) for tree_pos in tree_map.keys()])
    
    ut.print_answer(part=2, day=day, answer=answer)


part_one()
part_two()