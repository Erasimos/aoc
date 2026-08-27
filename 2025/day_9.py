import os
import sys
import math
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

def get_input():
    puzzle_input = read_file(puzzle_input_path)
    red_tiles = []
    for line in puzzle_input:
        x, y = line.split(',')
        red_tiles.append(Vec2D(int(x), int(y)))
    return red_tiles

def get_square_size(p1: Vec2D, p2: Vec2D):
    width = abs(p1.x - p2.x) + 1
    height = abs(p1.y -p2.y) + 1
    return width * height

def is_in_box(box_p1: Vec2D, box_p2: Vec2D, p: Vec2D):



    x_min = min(box_p1.x, box_p2.x)
    x_max = max(box_p1.x, box_p2.x)
    y_min = min(box_p1.y, box_p2.y)
    y_max = max(box_p1.y, box_p2.y)


    print('box_p1: ', box_p1)
    print('box_p2: ', box_p2)

    print('x_min: ', x_min)
    print('x_max: ', x_max)
    print('y_min: ', y_min)
    print('y_max: ', y_max)

    print('p: ', p)

    

    if p.x > x_min and p.x < x_max and p.y > y_min and p.y < y_max: 
        print('In the box')
        print('----------------------------------')
        return True
        
    else:
        print('----------------------------------')
        return False

def is_vertical(line_p1: Vec2D, line_p2: Vec2D):
    delta_x = line_p1.x - line_p2.x
    delta_y = line_p1.y - line_p2.y

    if delta_x == 0 and not delta_y == 0:
        return True
    elif not delta_x == 0 and delta_y == 0:
        return False
    else:
        raise(Exception('ERRRORORORO'))

def intersects_box(box_p1: Vec2D, box_p2: Vec2D, line_p1: Vec2D, line_p2: Vec2D):

    # if any line point in box
    if is_in_box(box_p1=box_p1, box_p2=box_p2, p=line_p1) or is_in_box(box_p1=box_p1, box_p2=box_p2, p=line_p2):
        return True



    pass



def is_valid_square(red_tiles: list[Vec2D], box_p1, box_p2):
    
    # Test all line segments
    for i, red_tile in enumerate(red_tiles):
        tile_index = (i + 1) % len(red_tiles)
        other_red_tile = red_tiles[tile_index]

        if intersects_box(box_p1=box_p1, box_p2=box_p2, line_p1=red_tile, line_p2=other_red_tile):
            
            return False
    return True

def get_largest_square_2(red_tiles: list[Vec2D]):
    largest_area = -math.inf
    for i, red_tile in enumerate(red_tiles):
        for other_red_tile in red_tiles[i+1:]:
            area = get_square_size(red_tile, other_red_tile)
            if area > largest_area and is_valid_square(red_tiles=red_tiles, box_p1=red_tile, box_p2=other_red_tile):
                largest_area = area
                print('largest area: ', largest_area)
                print('box_p1: ', red_tile)
                print('box_p2: ', other_red_tile)
    return largest_area

def get_largest_square(red_tiles: list[Vec2D]):
    largest_area = -math.inf

    for i, red_tile in enumerate(red_tiles):
        for other_red_tile in red_tiles[i+1:]:
            area = get_square_size(red_tile, other_red_tile)
            largest_area = max(largest_area, area)
    return largest_area

def part_one():

    red_tiles = get_input()
    answer = get_largest_square(red_tiles)

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    red_tiles = get_input()
    answer = get_largest_square_2(red_tiles)
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()