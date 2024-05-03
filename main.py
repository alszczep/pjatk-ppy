from curses import wrapper  # type: ignore
from curses.textpad import rectangle, Textbox  # type: ignore
from typing import Any

from _curses import curs_set, newwin  # type: ignore

from src.characters.Player import Player
from src.game.Game import Game
from src.game.GameState import GameState
from src.persistence.load_player import load_player
from src.persistence.save_player import save_player
from src.ui.UiPage import UiPage
from src.ui.ui_pages import mk_main_menu_page, mk_hunt_locations_page, mk_character_page, mk_fight_page, \
    mk_fight_finished_page


def main(screen: Any):
    loader_player = load_player()
    if loader_player is None:
        screen.addstr(0, 0, "Tell me your name traveller:")

        rectangle(screen, 2, 1, 4, 30)
        win = newwin(1, 28, 3, 2)
        box = Textbox(win)

        screen.refresh()

        box.edit()
        name = box.gather().strip()

        loader_player = Player("Player" if name == "" else name, 500, 40, 20, 0.1, 0, 0)

    game = Game(loader_player)
    save_player(loader_player)

    current_page: UiPage | None = None
    current_state: GameState | None = None

    curs_set(0)

    while True:
        screen.clear()
        state = game.get_state()

        if state != current_state:
            current_state = state
            current_page = None

            match current_state:
                case GameState.MAIN_MENU:
                    current_page = mk_main_menu_page(game)
                case GameState.HUNT_LOCATIONS:
                    current_page = mk_hunt_locations_page(game)
                case GameState.CHARACTER:
                    current_page = mk_character_page(game)
                case GameState.FIGHT:
                    current_page = mk_fight_page(game)
                case GameState.FIGHT_FINISHED:
                    current_page = mk_fight_finished_page(game)

        if current_page is None:
            raise ValueError("Page has to be set")

        current_page.render(screen)
        screen.refresh()

        key = screen.getkey()
        current_page.handle_key(key)

        save_player(game.get_player())


wrapper(main)
