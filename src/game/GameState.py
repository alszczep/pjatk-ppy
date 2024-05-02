from enum import Enum


class GameState(Enum):
    MAIN_MENU = 0
    HUNT_LOCATIONS = 1
    FIGHT = 11
    FIGHT_FINISHED = 111
    CHARACTER = 2
