from src.game.Game import Game
from src.location.locations import locations
from src.ui.CharacterPage import CharacterPage
from src.ui.MenuSelect import MenuSelect


def mk_main_menu_page(game: Game):
    return MenuSelect(game, "[Main Menu]", (
        ("Hunt", game.go_to_hunt),
        ("Character", game.go_to_character),
        ("Quit", game.quit_game)
    ))


def mk_hunt_locations_page(game: Game):
    options = list(map(lambda location: (location.name, lambda: game.go_to_fight(location)), locations))
    options.append(("Back", game.go_to_main_menu))

    return MenuSelect(game, "[Hunt Locations]", tuple(options))


def mk_character_page(game: Game):
    return CharacterPage(game)
