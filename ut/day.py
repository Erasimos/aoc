import sys
import pygame
from ut.constants import Colors
pygame.init()
from ut.screen import AoCScreen
from typing import Callable
import threading

from ut.simulation_state import SimulationState
simulation_state = SimulationState()

font = pygame.font.Font(None, 36)

class Button():
        def __init__(self, x: int, y: int, w: int, h: int, text: str, effect: Callable):
            self.text = text    
            self.rect = pygame.Rect(x, y, w, h)
            self.effect = effect


class Day:
    
    def __init__(self, part_one: Callable, part_two: Callable, pixel_map: dict):
        self.part_one = part_one
        self.part_two = part_two
        self.part_one_thread = None
        self.part_two_thread = None
        self.simulation_running = False
        self.pixel_map = pixel_map
        self.aoc_screen = AoCScreen(pixel_map=pixel_map, update_frequence=1)
        self.input_active = False
        self.input_value = 'Update Frequency'
        self.input_button = None
        self.running = False
        self.init_buttons()

    def init_buttons(self):

        quit_button = Button(x=self.aoc_screen.w - 130, y=self.aoc_screen.h - 60, w=120, h=50, text='Quit', effect=self.quit_button)
        part_one_button = Button(x=10, y=self.aoc_screen.h - 60, w=120, h=50, text='Part One', effect=self.part_one_button)
        button_part_two = Button(x=140, y=self.aoc_screen.h - 60, w=120, h=50, text='Part Two', effect=self.part_two_button)
        update_frequency_button = Button(x=10, y=self.aoc_screen.h - 130, w=120, h=50, text=self.input_value, effect=self.update_frequency_button)
        self.input_button = update_frequency_button
        self.buttons = [quit_button, part_one_button, button_part_two, update_frequency_button]

    def part_one_button(self):
        if self.simulation_running:
            print('Error: Simulation already running')
            return
        
        self.simulation_running = True
        self.part_one_thread = threading.Thread(target=self.part_one)
        self.part_one_thread.start()

    def part_two_button(self):
        if self.simulation_running:
            print('Error: Simulation already running')
            return
        
        self.simulation_running = True
        self.part_two_thread = threading.Thread(target=self.part_two)
        self.part_two_thread.start()
        

    def quit_button(self):
        self.running = False

    def update_frequency_button(self):
        self.input_active = True

    def draw_button(self, button: Button):
        pygame.draw.rect(self.aoc_screen.screen, Colors.BLUE, button.rect)
        pygame.draw.rect(self.aoc_screen.screen, Colors.BLACK, button.rect, 1)
        text_surface = font.render(button.text, True, Colors.WHITE)
        text_rect = text_surface.get_rect(center=button.rect.center)
        self.aoc_screen.screen.blit(text_surface, text_rect)

    def draw_buttons(self):
        self.input_button.text = self.input_value
        for button in self.buttons:
            self.draw_button(button)

    def draw_grid(self, grid: dict):

        if not grid == {}:
            self.aoc_screen.render_grid(grid=grid)

    def draw(self):

        self.draw_buttons()

        if self.simulation_running:
            self.draw_grid(grid=simulation_state.state)

        

    def handle_events(self):
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:

                    for button in self.buttons:
                        if button.rect.collidepoint(event.pos): button.effect()
                
                if event.type == pygame.KEYDOWN and self.input_active:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_value = self.input_value[:-1]  # Remove last character
                    elif event.key == pygame.K_RETURN:  # Press Enter to submit
                        new_update_frequency = 0 if not str.isnumeric(self.input_value) else int(self.input_value)
                        self.aoc_screen.update_frequency = new_update_frequency  # Update the class variable
                        self.input_active = False  # Disable further input
                    else:
                        self.input_value += event.unicode  # Append typed character

    def handle_simulation(self):
        if self.simulation_running:
            if self.part_one_thread and not self.part_one_thread.is_alive(): 
                self.simulation_running = False
            if self.part_two_thread and not self.part_two_thread.is_alive():
                self.simulation_running = False
            

    def run(self):
        self.running  = True
        self.aoc_screen.screen.fill(Colors.WHITE)
        
        while self.running:
            
            self.draw()

            self.handle_events()
            
            self.handle_simulation()

            pygame.display.flip()
        
        pygame.quit()
        sys.exit()()