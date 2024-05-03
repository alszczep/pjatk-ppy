from enum import Enum

from src.characters.Player import HEALTH_PER_SKILL_POINT, CRIT_CHANCE_PER_SKILL_POINT, DEFENSE_PER_SKILL_POINT, \
    ATTACK_PER_SKILL_POINT
from src.characters.leveling import level_to_exp
from src.game.Game import Game
from src.persistence.save_player import save_player
from src.ui.UiPage import UiPage
from src.utils.fix_round_off import fix_round_off


class CharacterPageMenuOptions(Enum):
    HEALTH = 7
    ATTACK = 8
    DEFENSE = 9
    CRIT_CHANCE = 10
    SPEND = 12
    BACK = 13


options = (
    CharacterPageMenuOptions.HEALTH.value,
    CharacterPageMenuOptions.ATTACK.value,
    CharacterPageMenuOptions.DEFENSE.value,
    CharacterPageMenuOptions.CRIT_CHANCE.value,
    CharacterPageMenuOptions.SPEND.value,
    CharacterPageMenuOptions.BACK.value
)


class CharacterPage(UiPage):
    def __init__(self, game: Game):
        self.__game = game

        self.__skill_points_to_spend = 0
        self.__points_in_health = 0
        self.__points_in_attack = 0
        self.__points_in_defense = 0
        self.__points_in_crit_chance = 0

        self.__current_option_index = 0

    def handle_key(self, key: str):
        match key:
            case "\n":
                if options[self.__current_option_index] == CharacterPageMenuOptions.SPEND.value:
                    self.apply_state()
                elif options[self.__current_option_index] == CharacterPageMenuOptions.BACK.value:
                    self.__game.go_to_main_menu()
            case "KEY_DOWN":
                self.__current_option_index += 1
                if self.__current_option_index >= len(options):
                    self.__current_option_index = 0
            case "KEY_UP":
                self.__current_option_index -= 1
                if self.__current_option_index < 0:
                    self.__current_option_index = len(options) - 1
            case "KEY_RIGHT":
                if self.__skill_points_to_spend >= self.__game.get_player().skill_points:
                    return

                match options[self.__current_option_index]:
                    case CharacterPageMenuOptions.HEALTH.value:
                        self.__points_in_health += 1
                        self.__skill_points_to_spend += 1
                    case CharacterPageMenuOptions.ATTACK.value:
                        self.__points_in_attack += 1
                        self.__skill_points_to_spend += 1
                    case CharacterPageMenuOptions.DEFENSE.value:
                        self.__points_in_defense += 1
                        self.__skill_points_to_spend += 1
                    case CharacterPageMenuOptions.CRIT_CHANCE.value:
                        if not self.is_crit_chance_maxed():
                            self.__points_in_crit_chance += 1
                            self.__skill_points_to_spend += 1
            case "KEY_LEFT":
                match options[self.__current_option_index]:
                    case CharacterPageMenuOptions.HEALTH.value:
                        if self.__points_in_health > 0:
                            self.__points_in_health -= 1
                            self.__skill_points_to_spend -= 1
                    case CharacterPageMenuOptions.ATTACK.value:
                        if self.__points_in_attack > 0:
                            self.__points_in_attack -= 1
                            self.__skill_points_to_spend -= 1
                    case CharacterPageMenuOptions.DEFENSE.value:
                        if self.__points_in_defense > 0:
                            self.__points_in_defense -= 1
                            self.__skill_points_to_spend -= 1
                    case CharacterPageMenuOptions.CRIT_CHANCE.value:
                        if self.__points_in_crit_chance > 0:
                            self.__points_in_crit_chance -= 1
                            self.__skill_points_to_spend -= 1

    def render(self, screen):
        player = self.__game.get_player()

        screen.addstr(0, 0, "{0} - Level {1}".format(player.name, str(player.level)))

        screen.addstr(2, 0, "Experience: {0}".format(str(player.exp)))
        screen.addstr(3, 0, "Experience to next level: {0}".format(str(level_to_exp(player.level + 1))))

        if self.__skill_points_to_spend > 0:
            screen.addstr(5, 0, "Skill Points: {0} - {1} (use arrows to spend)".format(player.skill_points,
                                                                                       self.__skill_points_to_spend))
        else:
            screen.addstr(5, 0, "Skill Points: {0} (use arrows to spend)".format(player.skill_points))

        def write_row(row_index: int, name: str, value: float | int, points: int, value_per_point: float | int,
                      additional_text: str = ""):
            if points > 0:
                screen.addstr(row_index, 2,
                              "{0}: {1} + {2} ({3}){4}".format(name, str(value),
                                                               str(fix_round_off(points * value_per_point)),
                                                               str(points),
                                                               additional_text))
            else:
                screen.addstr(row_index, 2, "{0}: {1}{2}".format(name, str(value), additional_text))

        write_row(CharacterPageMenuOptions.HEALTH.value, "Health", player.health, self.__points_in_health,
                  HEALTH_PER_SKILL_POINT)
        write_row(CharacterPageMenuOptions.ATTACK.value, "Attack", player.attack, self.__points_in_attack,
                  ATTACK_PER_SKILL_POINT)
        write_row(CharacterPageMenuOptions.DEFENSE.value, "Defense", player.defense, self.__points_in_defense,
                  DEFENSE_PER_SKILL_POINT)
        write_row(CharacterPageMenuOptions.CRIT_CHANCE.value, "Crit Chance", player.crit_chance,
                  self.__points_in_crit_chance, CRIT_CHANCE_PER_SKILL_POINT,
                  " [MAXED]" if self.is_crit_chance_maxed() else "")

        screen.addstr(CharacterPageMenuOptions.SPEND.value, 2, "Spend assigned skill points")
        screen.addstr(CharacterPageMenuOptions.BACK.value, 2, "Go back to main menu")

        screen.addstr(options[self.__current_option_index], 0, ">")

    def reset_state(self):
        self.__skill_points_to_spend = 0
        self.__points_in_health = 0
        self.__points_in_attack = 0
        self.__points_in_defense = 0
        self.__points_in_crit_chance = 0

    def apply_state(self):
        player = self.__game.get_player()

        player.upgrade_health(self.__points_in_health)
        player.upgrade_attack(self.__points_in_attack)
        player.upgrade_defense(self.__points_in_defense)
        player.upgrade_crit_chance(self.__points_in_crit_chance)

        save_player(player)

        self.reset_state()

    def is_crit_chance_maxed(self):
        return fix_round_off(
            self.__game.get_player().crit_chance + CRIT_CHANCE_PER_SKILL_POINT * self.__points_in_crit_chance) >= 0.5
