import sys
import pygame
from constants import Colors
pygame.init()
from screen import AoCScreen
from typing import Callable


font = pygame.font.Font(None, 36)

class Button():
        def __init__(self, x: int, y: int, w: int, h: int, text: str, effect: Callable):
            self.text = text    
            self.rect = pygame.Rect(x, y, w, h)
            self.effect = effect

class Day:
    
    def __init__(self, part_one: Callable, part_two: Callable, pixel_map: dict, update_frequency: int = 1):
        self.part_one = part_one
        self.part_two = part_two
        self.pixel_map = pixel_map
        self.aoc_screen = AoCScreen(pixel_map=pixel_map, update_frequence=update_frequency)
        self.running = False
        self.init_buttons()

    def init_buttons(self):

        button_quit = Button(x=self.aoc_screen.w - 130, y=self.aoc_screen.h - 60, w=120, h=50, text='Quit', effect=self.quit)
        button_part_one = Button(x=10, y=self.aoc_screen.h - 60, w=120, h=50, text='Part One', effect=self.part_one)
        button_part_two = Button(x=140, y=self.aoc_screen.h - 60, w=120, h=50, text='Part Two', effect=self.part_two)
        self.buttons = [button_quit, button_part_one, button_part_two]

    def part_one(self):
        self.part_one()

    def part_two(self):
        self.part_two()

    def quit(self):
        self.running = False

    def draw_button(self, button: Button):
        pygame.draw.rect(self.aoc_screen.screen, Colors.BLUE, button.rect)
        pygame.draw.rect(self.aoc_screen.screen, Colors.BLACK, button.rect, 1)
        text_surface = font.render(button.text, True, Colors.WHITE)
        text_rect = text_surface.get_rect(center=button.rect.center)
        self.aoc_screen.screen.blit(text_surface, text_rect)

    def draw_buttons(self):
        for button in self.buttons:
            self.draw_button(button)

    def draw_grid(self, grid: dict):

        self.aoc_screen.render_grid(grid=grid)

    def draw(self):
        
        self.draw_buttons()

    def handle_events(self):
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:

                    for button in self.buttons:
                        if button.rect.collidepoint(event.pos): button.effect()

    def run(self):
        self.running  = True
        self.aoc_screen.screen.fill(Colors.WHITE)
        while self.running:
            
            self.draw()

            self.handle_events()

            pygame.display.flip()
        
        pygame.quit()
        sys.exit()