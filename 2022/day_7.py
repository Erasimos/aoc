import os
import sys
from pathlib import Path
sys.path.append(os.getcwd() + '/ut')
import ut

day = Path(__file__).stem
puzzle_input_path = Path(__file__).parent / 'input' / f'{day}.txt'

class Directory:
    def __init__(self, name, parent=None):
        self.files = {} 
        self.parent = parent
        self.children = {}
        self.name = name

    def add_file(self, filename, filesize):
        self.files[filename] = filesize

    def add_directory(self, directory_name):
        self.children[directory_name] = Directory(parent=self, name=directory_name)

    def get_size(self):
        return sum(self.files.values()) + sum([child.get_size() for child in self.children.values()])

    def get_directories_lt(self, size_limit):
        
        directories = []
        if self.get_size() < size_limit:
            directories.append(self)
        
        for child in self.children.values():
            directories.extend(child.get_directories_lt(size_limit))
        
        return directories

    def get_directories_gt(self, size_limit):
        
        directories = []
        if self.get_size() > size_limit:
            directories.append(self)
        
        for child in self.children.values():
            directories.extend(child.get_directories_gt(size_limit))
        
        return directories

    def print_directory(self):
        for file in self.files.keys():
            print('file: ', file, ', size: ', self.files[file])
        
        for child in self.children.keys():
            print('child: ', child)
            self.children[child].print_directory()
        

def get_input():
    puzzle_input = ut.read_file(puzzle_input_path)
    terminal_output = [line.split() for line in puzzle_input]
    return terminal_output


def cd(filesystem, current_directory: Directory, d):
    
    if d == '/':
        return filesystem
    elif d == '..':
        return current_directory.parent
    else:
        return current_directory.children[d]


def parse_output(terminal_output):
    
    filesystem = Directory('/')
    current_directoy: Directory = None

    for line in terminal_output:
        sym_1 = line[0]
        sym_2 = line[1]
                
        if sym_1 == '$':
            if sym_2 == 'cd':
                current_directoy = cd(filesystem=filesystem, current_directory=current_directoy, d=line[2])
        else:
            if sym_1 == 'dir':
                current_directoy.add_directory(directory_name=sym_2)
            else:
                current_directoy.add_file(filename=sym_2, filesize=int(sym_1))

    return filesystem


def part_one():

    terminal_output = get_input()
    filesystem = parse_output(terminal_output=terminal_output)
    target_directories = filesystem.get_directories_lt(size_limit=100000)
    answer = sum([target_directory.get_size() for target_directory in target_directories])

    ut.print_answer(part=1, day=day, answer=answer)


def part_two():

    total_disk_space = 70000000
    required_disk_space = 30000000

    terminal_output = get_input()
    filesystem = parse_output(terminal_output=terminal_output)

    used_disk_space = filesystem.get_size()
    unused_disk_space = total_disk_space - used_disk_space
    required_disk_space_to_free_up = required_disk_space - unused_disk_space
    target_directories = filesystem.get_directories_gt(size_limit=required_disk_space_to_free_up)
    answer = answer = min([target_directory.get_size() for target_directory in target_directories])

    ut.print_answer(part=2, day=day, answer=answer)


part_one()
part_two()