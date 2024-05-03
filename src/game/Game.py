from src.chances.element_by_chance import element_by_chance
from src.characters.Player import Player
from src.characters.enemies.Enemy import Enemy
from src.game.GameState import GameState
from src.game.InvalidStateChangeError import InvalidStateChangeError
from src.location.Location import Location


class Game:
    def __init__(self, player: Player):
        self.__state = GameState.MAIN_MENU
        self.__player = player
        self.__enemy: Enemy | None = None
        self.__exp_gained: int | None = None

    def get_state(self):
        return self.__state

    def get_player(self):
        return self.__player

    def get_enemy(self):
        if self.__enemy is None:
            raise ValueError("Enemy should be set before starting a fight")
        return self.__enemy

    def get_exp_gained(self):
        return self.__exp_gained

    def go_to_hunt(self):
        if self.__state != GameState.MAIN_MENU:
            raise InvalidStateChangeError(self.__state.name, GameState.HUNT_LOCATIONS.name)

        self.__state = GameState.HUNT_LOCATIONS

    def go_to_fight(self, location: Location):
        if self.__state != GameState.HUNT_LOCATIONS:
            raise InvalidStateChangeError(self.__state.name, GameState.FIGHT.name)

        self.__state = GameState.FIGHT
        self.__enemy = element_by_chance(tuple(location.enemies))

    def go_to_fight_finished(self, exp_gained: int | None):
        if self.__state != GameState.FIGHT:
            raise InvalidStateChangeError(self.__state.name, GameState.FIGHT_FINISHED.name)

        self.__exp_gained = exp_gained

        self.__state = GameState.FIGHT_FINISHED

    def go_to_character(self):
        if self.__state != GameState.MAIN_MENU:
            raise InvalidStateChangeError(self.__state.name, GameState.CHARACTER.name)

        self.__state = GameState.CHARACTER

    def go_to_main_menu(self):
        if (self.__state != GameState.CHARACTER
                and self.__state != GameState.HUNT_LOCATIONS
                and self.__state != GameState.FIGHT_FINISHED):
            raise InvalidStateChangeError(self.__state.name, GameState.MAIN_MENU.name)

        if self.__state == GameState.FIGHT_FINISHED:
            self.__exp_gained = None

        self.__state = GameState.MAIN_MENU

    def quit_game(self):
        if self.__state != GameState.MAIN_MENU:
            raise InvalidStateChangeError(self.__state.name, "QUIT")
        exit(0)
