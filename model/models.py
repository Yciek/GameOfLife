import pygame
import numpy as np

"""setting up colors"""
ALIVE_COLOR = (240, 10, 100)
BACKGROUND_COLOR = (100, 30, 180)
GRID_COLOR = (0, 0, 0)
DYING_COLOR = (255, 255, 255)


class Cell:
    def __init__(self, screen, cells, size, with_progress=False):
        self.screen = screen
        self.cells = cells
        self.size = size
        self.with_progress = with_progress

    @staticmethod
    def rules(self, screen, cells, size, with_progress):
        self.screen = screen
        self.cells = cells
        self.size = size
        self.with_progress = with_progress

        """creating empty cells"""
        cell_updated = np.zeros((self.cells.shape[0], self.cells.shape[1]))

        """iteration through each row and column"""
        for row, column in np.ndindex(self.cells.shape):
            """calculation of alive cells in neighbour"""
            alive = np.sum(self.cells[row - 1: row + 2, column - 1: column + 2]) - self.cells[row, column]
            """coloring alive cells"""
            color = BACKGROUND_COLOR if self.cells[row, column] == 0 else ALIVE_COLOR

            """dying cell rule apply"""
            if self.cells[row, column] == 1:
                if alive < 2 or alive > 3:
                    if self.with_progress:
                        color = DYING_COLOR

                    """alive cell rule applied"""
                elif 2 <= alive <= 3:
                    cell_updated[row, column] = 1
                    if self.with_progress:
                        color = ALIVE_COLOR
            else:
                """next rule for alive cell applied"""
                if alive == 3:
                    cell_updated[row, column] = 1
                    if self.with_progress:
                        color = ALIVE_COLOR

            """plotting rectangle"""
            pygame.draw.rect(self.screen, color, (column * self.size, row * self.size, self.size - 1, self.size - 1))
        return cell_updated
