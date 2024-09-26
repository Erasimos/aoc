import pygame
import time
from constants import Colors
from ut import Vec2D


default_pixel_map = {
    '#': Colors.BLACK,
    '': Colors.WHITE 
}

default_w = 1000
default_h = 1000

class AoCScreen():
    def __init__(self, w = default_w, h = default_h, speed = 0, pixel_map: dict = default_pixel_map, update_frequence: int = 1):
        self.screen = pygame.display.set_mode((w, h))
        self.speed = speed
        self.w = w
        self.h = h
        self.pixel_map = pixel_map
        self.step = 0
        self.update_frequency = update_frequence
        pygame.display.set_caption("AoC")


    def render_grid(self, grid: dict):

        self.step += 1
        if not self.step % self.update_frequency == 0: 
            return

        x_positions = [pos.x for pos in grid.keys()]
        y_positions = [pos.y for pos in grid.keys()]
        min_x, max_x = min(x_positions), max(x_positions)
        min_y, max_y = min(y_positions), max(y_positions)

        cell_size = max(1, int(self.h / (max_y - min_y))) 
        
        grid_surface = pygame.Surface((self.w, self.h))

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                tile_type = grid.get(Vec2D(x, y), '')
                tile_color = self.pixel_map[tile_type]
                screen_x = (x - min_x) * cell_size + (self.w / 2) - (((max_x - min_x) * cell_size) / 2)
                screen_y = (y - min_y) * cell_size + (self.h / 2) - (((max_y - min_y) * cell_size) / 2)
                tile = pygame.Rect(screen_x, screen_y, cell_size, cell_size)
                pygame.draw.rect(grid_surface, tile_color, tile)
                # Outline

                if not tile_type == '':
                    pygame.draw.rect(grid_surface, Colors.BLACK, tile, 1)

        self.screen.blit(grid_surface, (0, 0))
        pygame.display.flip()