import time
import pygame
import numpy as np

from model.models import GRID_COLOR, Cell


class Game:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Game of Life - hold LMB to draw and press TAB to START or PAUSE the game')
        """setting size of a window"""
        self.screen = pygame.display.set_mode((600, 600))
        """defining cells size"""
        self.cells = np.zeros((60, 60))
        """setting color for screen"""
        self.screen.fill(GRID_COLOR)
        """setting up size of cells"""
        self.size = 10
        """updating color of cells and screen in given size"""
        self.with_progress = False
        Cell.rules(self, self.screen, self.cells, self.size, self.with_progress)
        """updating part/whole screen"""
        pygame.display.flip()
        pygame.display.update()
        self.running = False

    def game_simulation(self):
        """assigning keys to start and quit game of life: tab - starts/stop the game"""
        cell = Cell(self.screen, self.cells, self.size)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        self.running = not self.running
                        cell.rules(self, self.screen, self.cells, self.size, self.with_progress)
                        pygame.display.update()
                """assigning left mouse key to activate/create cells """
                if pygame.mouse.get_pressed()[0]:
                    position = pygame.mouse.get_pos()
                    self.cells[position[1] // self.size, position[0] // self.size] = 1
                    cell.rules(self, self.screen, self.cells, self.size, self.with_progress)
                    pygame.display.update()

            self.screen.fill(GRID_COLOR)

            if self.running:
                self.cells = cell.rules(self, self.screen, self.cells, self.size, True)
                pygame.display.update()
            time.sleep(0.001)
