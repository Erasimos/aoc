import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)
from copy import deepcopy
from ut.common import Vec2D, read_file_raw, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

class Harddrive():
    def __init__(self, data: list):
        self.drive = []
        self.init_drive(data=data)

    def init_drive(self, data: list):

        self.drive = []
        file_mode = True
        file_id = 0

        free_space = 0
        occupied_space = 0        

        for val in data:

            if file_mode:
                
                for _ in range(val):
                    self.drive.append(file_id)
                    occupied_space += 1
                file_id += 1
                file_mode = False

            else:

                for _ in range(val):
                    self.drive.append('.')
                    free_space += 1
                file_mode = True
        
        self.free_space = free_space
        self.occupied_space = occupied_space
        self.size = free_space + occupied_space
        self.file_id_count = file_id - 1

    def defrag(self):
        
        print('occupied_space: ', self.occupied_space)

        for a in range(self.occupied_space):

            if a % 1000 == 0:
                print(a)

            # Find righmost
            for i in range(self.size - 1, -1, -1):
                if self.drive[i] == '.':
                    continue
                else:
                    # Move leftmost
                    for j in range(self.size):
                        if self.drive[j] == '.':
                            self.drive[j] = self.drive[i]
                            self.drive[i] = '.'
                            break
                    break

    def defrag_2(self):

        print('ids: ', self.file_id_count)


            

        for id in range(self.file_id_count, -1, -1):

            if id % 1000 == 0:
                print(id)

            # Find id block
            block_end = None
            block_start = None
            for i in range(self.size - 1, -1, -1):
                if self.drive[i] == id:
                    block_end = i

                    for j in range(i - 1, -1, -1):
                        if self.drive[j] == id:
                            if j == 0:
                                block_start = j
                            continue
                        else:
                            block_start = j + 1
                            break
                    break
            
            block_size = block_end - block_start + 1

            # Find leftmost free block
            free_block_size = 0
            for i in range(block_start):
                
                if self.drive[i] == '.':
                    free_block_size += 1

                    if free_block_size == block_size:

                        # Move block
                        for j in range(block_size):
                            self.drive[i - j] = id
                            self.drive[block_start + j] = '.' 
                        break
                else:
                    free_block_size = 0 


    def get_checksum(self):
        checksum = 0
        for i in range(self.size):
            val = self.drive[i]
            if val == '.':
                continue
            else:
                checksum += i * val
        return checksum

def get_input():
    return [int(el) for el in read_file_raw(puzzle_input_path)]


def part_one():

    data = get_input()
    hdr = Harddrive(data=data)
    hdr.defrag()

    answer = hdr.get_checksum()

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    data = get_input()
    hdr = Harddrive(data=data)
    hdr.defrag_2()

    answer = hdr.get_checksum()
    
    print_answer(part=2, day=day_nr, answer=answer)

#part_one()
part_two()




## OPTINAL PY GAME VISUALIZATION
###
###
### ---------------------------------------------------------------
from ut.day import Day
from ut.constants import Colors
from ut.simulation_state import SimulationState
simulation_state = SimulationState()

def run_day():
    pixel_map = {'#': Colors.GRAY, '': Colors.WHITE}
    day = Day(part_one=part_one, part_two=part_two, pixel_map=pixel_map)
    day.run()

# run_day()