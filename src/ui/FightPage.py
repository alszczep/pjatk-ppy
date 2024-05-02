from enum import Enum

from src.game.Game import Game
from src.ui.UiPage import UiPage


class AttackOptions(Enum):
    HEAD = 0
    LEFT_ARM = 1
    CHEST = 2
    RIGHT_ARM = 3
    LEFT_LEG = 4
    RIGHT_LEG = 5


class FightPage(UiPage):
    def __init__(self, game: Game):
        self.__game = game

        self.__in_fight_player_health = self.__game.get_player().health
        self.__in_fight_enemy_health = self.__game.get_enemy().health

        self.__last_round_player_log = ""
        self.__last_round_enemy_log = ""

        self.__current_option_index = AttackOptions.HEAD

    def handle_key(self, key: str):
        if key == "\n":
            # attack
            self.__in_fight_enemy_health -= 10

        match self.__current_option_index:
            case AttackOptions.HEAD:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = AttackOptions.CHEST
                    case "KEY_RIGHT":
                        self.__current_option_index = AttackOptions.RIGHT_ARM
                    case "KEY_LEFT":
                        self.__current_option_index = AttackOptions.LEFT_ARM
                    case "KEY_UP":
                        self.__current_option_index = AttackOptions.LEFT_LEG
            case AttackOptions.LEFT_ARM:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = AttackOptions.LEFT_LEG
                    case "KEY_RIGHT":
                        self.__current_option_index = AttackOptions.CHEST
                    case "KEY_LEFT":
                        self.__current_option_index = AttackOptions.RIGHT_ARM
                    case "KEY_UP":
                        self.__current_option_index = AttackOptions.HEAD
            case AttackOptions.CHEST:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = AttackOptions.LEFT_LEG
                    case "KEY_RIGHT":
                        self.__current_option_index = AttackOptions.RIGHT_ARM
                    case "KEY_LEFT":
                        self.__current_option_index = AttackOptions.LEFT_ARM
                    case "KEY_UP":
                        self.__current_option_index = AttackOptions.HEAD
            case AttackOptions.RIGHT_ARM:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = AttackOptions.RIGHT_LEG
                    case "KEY_RIGHT":
                        self.__current_option_index = AttackOptions.LEFT_ARM
                    case "KEY_LEFT":
                        self.__current_option_index = AttackOptions.CHEST
                    case "KEY_UP":
                        self.__current_option_index = AttackOptions.HEAD
            case AttackOptions.LEFT_LEG:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = AttackOptions.HEAD
                    case "KEY_RIGHT":
                        self.__current_option_index = AttackOptions.RIGHT_LEG
                    case "KEY_LEFT":
                        self.__current_option_index = AttackOptions.RIGHT_LEG
                    case "KEY_UP":
                        self.__current_option_index = AttackOptions.CHEST
            case AttackOptions.RIGHT_LEG:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = AttackOptions.HEAD
                    case "KEY_RIGHT":
                        self.__current_option_index = AttackOptions.LEFT_LEG
                    case "KEY_LEFT":
                        self.__current_option_index = AttackOptions.LEFT_LEG
                    case "KEY_UP":
                        self.__current_option_index = AttackOptions.CHEST

    def render(self, screen):
        def write_from_the_back(row_index: int, text: str):
            screen.addstr(row_index, 59 - len(text), text)

        player = self.__game.get_player()
        enemy = self.__game.get_enemy()

        screen.addstr(0, 0, player.name)
        screen.addstr(1, 0, "Health: {0}/{1}".format(str(self.__in_fight_player_health), str(player.health)))

        write_from_the_back(0, enemy.name)
        write_from_the_back(1, "Health: {0}/{1}".format(str(self.__in_fight_enemy_health), str(enemy.health)))

        screen.addstr(3, 0, self.__last_round_player_log)
        screen.addstr(4, 0, self.__last_round_enemy_log)

        #               ╭─────╮
        #               │  X  │
        #               ╰─────╯
        #       ╭─────╮ ╭─────╮ ╭─────╮
        #       │  X  │ │  X  │ │  X  │
        #       ╰─────╯ ╰─────╯ ╰─────╯
        #          ╭─────╮   ╭─────╮
        #          │  X  │   │  X  │
        #          ╰─────╯   ╰─────╯

        head_sign = "X" if self.__current_option_index == AttackOptions.HEAD else " "
        left_arm_sign = "X" if self.__current_option_index == AttackOptions.LEFT_ARM else " "
        chest_sign = "X" if self.__current_option_index == AttackOptions.CHEST else " "
        right_arm_sign = "X" if self.__current_option_index == AttackOptions.RIGHT_ARM else " "
        left_leg_sign = "X" if self.__current_option_index == AttackOptions.LEFT_LEG else " "
        right_leg_sign = "X" if self.__current_option_index == AttackOptions.RIGHT_LEG else " "

        screen.addstr(6, 27, "╭─────╮")
        screen.addstr(7, 27, "│  {0}  │".format(head_sign))
        screen.addstr(8, 27, "╰─────╯")
        screen.addstr(9, 19, "╭─────╮ ╭─────╮ ╭─────╮")
        screen.addstr(10, 19, "│  {0}  │ │  {1}  │ │  {2}  │".format(left_arm_sign, chest_sign, right_arm_sign))
        screen.addstr(11, 19, "╰─────╯ ╰─────╯ ╰─────╯")
        screen.addstr(12, 22, "╭─────╮   ╭─────╮")
        screen.addstr(13, 22, "│  {0}  │   │  {1}  │".format(left_leg_sign, right_leg_sign))
        screen.addstr(14, 22, "╰─────╯   ╰─────╯")
