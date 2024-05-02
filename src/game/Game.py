from src.characters.Player import Player
from src.game.GameState import GameState
from src.game.InvalidStateChangeError import InvalidStateChangeError
from src.location.Location import Location


class Game:
    def __init__(self, player: Player):
        self.__state = GameState.MAIN_MENU
        self.__player = player
        self.__current_location: Location | None = None

    def get_state(self):
        return self.__state

    def get_player(self):
        return self.__player

    def go_to_hunt(self):
        if self.__state != GameState.MAIN_MENU:
            raise InvalidStateChangeError(self.__state.name, GameState.HUNT_LOCATIONS.name)

        self.__state = GameState.HUNT_LOCATIONS

    def go_to_fight(self, location: Location):
        if self.__state != GameState.HUNT_LOCATIONS:
            raise InvalidStateChangeError(self.__state.name, GameState.FIGHT.name)

        self.__state = GameState.FIGHT
        self.__current_location = location

    def go_to_fight_finished(self):
        if self.__state != GameState.FIGHT:
            raise InvalidStateChangeError(self.__state.name, GameState.FIGHT_FINISHED.name)

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

        self.__state = GameState.MAIN_MENU

    def quit_game(self):
        if self.__state != GameState.MAIN_MENU:
            raise InvalidStateChangeError(self.__state.name, "QUIT")
        exit(0)
