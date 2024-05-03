from src.game.Game import Game
from src.ui.UiPage import UiPage


class FightFinishedPage(UiPage):
    def __init__(self, game: Game):
        self.__game = game

    def handle_key(self, key: str):
        if key == "\n":
            self.__game.go_to_main_menu()

    def render(self, screen):
        def render_continue(row_index: int = 2):
            screen.addstr(row_index, 0, "Press enter to continue")

        exp_gained = self.__game.get_exp_gained()
        if exp_gained is None:
            screen.addstr(0, 0, "You died!")
            render_continue()
            return

        screen.addstr(0, 0, "You won! Gained {0} experience points.".format(exp_gained))

        old_level = self.__game.get_player().level
        self.__game.get_player().gain_exp(exp_gained)
        new_level = self.__game.get_player().level

        if new_level > old_level:
            screen.addstr(1, 0, "You leveled up from {0} to {1}!".format(old_level, new_level))
            render_continue(3)
        else:
            render_continue()
