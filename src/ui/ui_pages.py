from src.game.Game import Game
from src.location.locations import locations
from src.ui.CharacterPage import CharacterPage
from src.ui.FightFinishedPage import FightFinishedPage
from src.ui.FightPage import FightPage
from src.ui.MenuSelect import MenuSelect


def mk_main_menu_page(game: Game):
    return MenuSelect(game, "[Main Menu]", (
        ("Hunt", game.go_to_hunt),
        ("Character", game.go_to_character),
        ("Quit", game.quit_game)
    ))


def mk_hunt_locations_page(game: Game):
    options = list(map(lambda location: (
        "{0} ({1}-{2} Level)".format(location.name, location.recommended_level_from, location.recommended_level_to),
        lambda: game.go_to_fight(location)), locations))
    options.append(("Back", game.go_to_main_menu))

    return MenuSelect(game, "[Hunt Locations]", tuple(options))


def mk_character_page(game: Game):
    return CharacterPage(game)


def mk_fight_page(game: Game):
    return FightPage(game)


def mk_fight_finished_page(game: Game):
    return FightFinishedPage(game)
