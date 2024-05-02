from typing import Optional, Callable

from src.game.Game import Game
from src.ui.UiPage import UiPage

MenuItem = tuple[str, Callable[[Game], None]]


class MenuSelect(UiPage):
    # items - single item is a tuple of (item name to be displayed, callback to be called when item is selected)
    def __init__(self, game: Game, title: Optional[str], items: tuple[tuple[str, Callable[[], None]], ...],
                 line_offset: int = 0):
        self.__game = game
        self.title = title
        self.items = items
        self.line_offset = line_offset
        self.__currentItem = 0

    def handle_key(self, key: str):
        if key == "\n":
            self.items[self.__currentItem][1]()
            return
        if key == "KEY_DOWN":
            self.__currentItem += 1
            if self.__currentItem >= len(self.items):
                self.__currentItem = 0
        elif key == "KEY_UP":
            self.__currentItem -= 1
            if self.__currentItem < 0:
                self.__currentItem = len(self.items)

    def render(self, screen):
        items_offset = self.line_offset

        if self.title is not None:
            screen.addstr(self.line_offset, 0, self.title)
            items_offset += 2

        for i, (item, _) in enumerate(self.items):
            screen.addstr(i + items_offset, 2, item)

        screen.addstr(self.__currentItem + items_offset, 0, ">")
