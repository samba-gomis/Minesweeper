import random
from utils.constants import *


class Difficulty:
    """
    Defines the grid size and mine count based on the chosen difficulty level
    """

    def __init__(self, level: str):
        self.level = level

        if level == "EASY":
            self.cols, self.rows = SMALL_GRID
        elif level == "INTERMEDIATE":
            self.cols, self.rows = MEDIUM_GRID
        else:
            self.cols, self.rows = BIG_GRID

        self.mine_count = random.randint(MIN_BOMB[level], MAX_BOMB[level])