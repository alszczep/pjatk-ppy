from curses import wrapper  # type: ignore
from typing import Any

from src.characters.Player import Player
from src.game.Game import Game
from src.game.GameState import GameState
from src.ui.UiPage import UiPage
from src.ui.ui_pages import mk_main_menu_page, mk_hunt_locations_page


def main(screen: Any):
    player = Player("Player", 500, 50, 20, 0.1, 0, 0)
    game = Game(player)

    current_page: UiPage | None = None
    current_state: GameState | None = None

    while True:
        screen.clear()
        state = game.get_state()

        if state != current_state:
            current_state = state
            current_page = None

            if current_state == GameState.MAIN_MENU:
                current_page = mk_main_menu_page(game)
            elif current_state == GameState.HUNT_LOCATIONS:
                current_page = mk_hunt_locations_page(game)

        if current_page is None:
            raise ValueError("Page has to be set")

        current_page.render(screen)
        screen.refresh()

        key = screen.getkey()
        current_page.handle_key(key)


wrapper(main)
