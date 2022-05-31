import controller
from controller.controller import Game


def view_init():
    start = Game()
    start.game_simulation()
