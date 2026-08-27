import os
import re
import sys
from copy import deepcopy
import math
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Parent directory
sys.path.insert(0, parent_dir)

from ut.common import Vec2D, read_file, print_answer

day_name = Path(__file__).stem
day_nr = day_name[4:]
puzzle_input_path = Path(__file__).parent / 'input' / f'{day_name}.txt'

class Button:
    def __init__(self):
        self.indicators = []

    def print(self):
        print(self.indicators)

class Machine:
    def __init__(self, target_configuration, buttons: list[Button], target_joltage):
        self.target_configuration = target_configuration
        self.lights = list('.' * len(target_configuration))
        self.target_joltage = target_joltage
        self.joltage = [0 for i in range(len(target_joltage))]
        self.buttons = buttons
        self.presses = 0
    
    def convert_joltage_state_to_light_state(self):
        target_converted_light_state = ''

        for joltage in self.target_joltage:
            if joltage % 2 == 0:
                target_converted_light_state += '.'
            else:
                target_converted_light_state += '#'
        
        return target_converted_light_state

    def get_state(self):
        return ''.join(self.lights)

    def get_state_joltage(self):
        return ''.join([',' + str(el) for el in self.joltage])
    
    def is_configured(self):
        return ''.join(self.lights) == self.target_configuration

    def is_configured_joltage(self):
        return self.target_joltage == self.joltage
    
    def is_overcharged(self):
        for index, joltage in enumerate(self.joltage):
            if joltage > self.target_joltage[index]: return True
        return False

    def press_button(self, button: Button):
        for indicator in button.indicators:
            current_state = self.lights[indicator]
            new_state = '.' if current_state == '#' else '#'
            self.lights[indicator] = new_state
            self.joltage[indicator] = self.joltage[indicator] + 1
        self.presses += 1
        

    def print(self):

        print('MACHINE')
        print('Target Configuration: ', self.target_configuration)
        print('Lights: ', self.lights)
        print('Target Joltage: ', self.target_joltage)
        print('Joltage: ', self.joltage)
        print('Buttons: ') 
        for button in self.buttons:
            button.print()
        print('------------------')

def find_shortest_configuration(machine: Machine):
    
    previous_states = {machine.get_state() : True}
    current_min = math.inf
    
    searching_machines = [machine]

    while searching_machines:
        
        new_searching_machines = []

        for searching_machine in searching_machines:

            if searching_machine.is_configured():
                current_min = searching_machine.presses
                continue

            for button in searching_machine.buttons:
                new_searching_machine = deepcopy(searching_machine)
                new_searching_machine.press_button(button)

                # Only add machine if it is an unexplored machine state, and if it was reached with a shorter path
                if previous_states.get(new_searching_machine.get_state(), False):
                    continue
                elif new_searching_machine.presses > current_min:
                    continue
                else:
                    new_searching_machines.append(new_searching_machine)
                    previous_states[new_searching_machine.get_state()] = True
        
        searching_machines = new_searching_machines
    
    return current_min

def find_shortest_configuration_joltage(machine: Machine):
    
    print('NEW MACHINE JOLTAGE COUNTING')
    machine.print()
    
    previous_states = {machine.get_state_joltage() : True}
    current_min = math.inf
    print('I AM ACTUALLY GETTING HERE')
    print('current min: ', current_min)
    searching_machines = [machine]

    while searching_machines:
        
        new_searching_machines = []

        for searching_machine in searching_machines:
        
            print('current machine joltage: ', searching_machine.joltage)

            if searching_machine.is_configured_joltage():
                current_min = searching_machine.presses
                print(current_min, ', ', end='')
                continue
            
            if searching_machine.is_overcharged():
                continue

            for button in searching_machine.buttons:
                new_searching_machine = deepcopy(searching_machine)
                new_searching_machine.press_button(button)

                # Only add machine if it is an unexplored machine state, and if it was reached with a shorter path
                if previous_states.get(new_searching_machine.get_state_joltage(), False):
                    continue
                elif new_searching_machine.presses > current_min:
                    continue
                else:
                    new_searching_machines.append(new_searching_machine)
                    previous_states[new_searching_machine.get_state_joltage()] = True
        
        searching_machines = new_searching_machines
    
    return current_min

def get_input():
    puzzle_input = read_file(puzzle_input_path)

    machines = []

    for line in puzzle_input:

        split_line = line.split()
        raw_lights = split_line[0]
        raw_buttons = split_line[1:-1]
        raw_joltage = split_line[-1]

        # Target configuration
        target_configuration = raw_lights[1:-1]

        # Available buttons
        buttons = []
        for button_line in raw_buttons:
            actual_buttons = [int(el) for el in button_line[1:-1].split(',')]
            button = Button()
            button.indicators = actual_buttons
            buttons.append(button)
        
        # Joltage
        target_joltage =  [int(el) for el in raw_joltage[1:-1].split(',')]

        # Machines
        new_machine = Machine(target_configuration=target_configuration, buttons=buttons, target_joltage=target_joltage)
        machines.append(new_machine)

    return machines

def part_one():

    answer = 0
    machines = get_input()

    for machine in machines:
        answer += find_shortest_configuration(machine)

    print_answer(part=1, day=day_nr, answer=answer)


def part_two():

    answer = 0
    machines = get_input()
    print('total machines: ', len(machines))
    for i, machine in enumerate(machines):
        print('converted jolt state: ', machine.convert_joltage_state_to_light_state())
        machine.print()
        
        
        #answer += find_shortest_configuration_joltage(machine)
    
    print_answer(part=2, day=day_nr, answer=answer)

part_one()
part_two()