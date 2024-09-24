import pygame
import time
from constants import Colors
from ut import Vec2D

pygame.init()

default_pixel_map = {
    '#': Colors.BLACK,
    '': Colors.WHITE 
}

class AoCScreen():
    def __init__(self, w = 1600, h = 900, speed = 0.00005, pixel_map: dict = default_pixel_map):
        self.screen = pygame.display.set_mode((w, h))
        self.speed = speed
        self.pixel_map = pixel_map
        pygame.display.set_caption("AoC")

    def render_grid(self, grid: dict):
        
        self.screen.fill(Colors.WHITE)

        x_positions = [pos.x for pos in grid.keys()]
        y_positions = [pos.y for pos in grid.keys()]
        min_x, max_x = min(x_positions), max(x_positions)
        min_y, max_y = min(y_positions), max(y_positions)

        cell_size = 4

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                tile_type = grid.get(Vec2D(x, y), '')
                tile_color = self.pixel_map[tile_type]
                screen_x = (x - min_x) * cell_size
                screen_y = (y - min_y) * cell_size
                tile = pygame.Rect(screen_x, screen_y, cell_size, cell_size)
                pygame.draw.rect(self.screen, tile_color, tile)

        time.sleep(self.speed)
        pygame.display.flip()