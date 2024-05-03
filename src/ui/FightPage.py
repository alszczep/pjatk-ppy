from src.characters.BodyParts import BodyParts
from src.game.Game import Game
from src.game.handle_fight_turn import handle_fight_turn, FightTurnResult
from src.ui.UiPage import UiPage


class FightPage(UiPage):
    def __init__(self, game: Game):
        self.__game = game

        self.__in_fight_player_health = self.__game.get_player().health
        self.__in_fight_enemy_health = self.__game.get_enemy().health

        self.__last_round_player_log = ""
        self.__last_round_enemy_log = ""

        self.__current_option_index = BodyParts.HEAD

        self.__turn = 0

    def handle_key(self, key: str):
        if key == "\n":
            player = self.__game.get_player()
            enemy = self.__game.get_enemy()

            handle_fight_turn_result = handle_fight_turn(player, enemy, self.__in_fight_player_health,
                                                         self.__in_fight_enemy_health, self.__current_option_index)

            if handle_fight_turn_result.result == FightTurnResult.ENEMY_KILLED:
                self.__game.go_to_fight_finished(enemy.exp_reward)
            elif handle_fight_turn_result.result == FightTurnResult.PLAYER_KILLED:
                self.__game.go_to_fight_finished(None)
            else:
                self.__last_round_player_log = handle_fight_turn_result.player_turn.log
                self.__in_fight_enemy_health -= handle_fight_turn_result.player_turn.damage_dealt
                self.__last_round_enemy_log = handle_fight_turn_result.enemy_turn.log
                self.__in_fight_player_health -= handle_fight_turn_result.enemy_turn.damage_dealt

            self.__turn += 1
            return

        match self.__current_option_index:
            case BodyParts.HEAD:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = BodyParts.CHEST
                    case "KEY_RIGHT":
                        self.__current_option_index = BodyParts.RIGHT_ARM
                    case "KEY_LEFT":
                        self.__current_option_index = BodyParts.LEFT_ARM
                    case "KEY_UP":
                        self.__current_option_index = BodyParts.LEFT_LEG
            case BodyParts.LEFT_ARM:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = BodyParts.LEFT_LEG
                    case "KEY_RIGHT":
                        self.__current_option_index = BodyParts.CHEST
                    case "KEY_LEFT":
                        self.__current_option_index = BodyParts.RIGHT_ARM
                    case "KEY_UP":
                        self.__current_option_index = BodyParts.HEAD
            case BodyParts.CHEST:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = BodyParts.LEFT_LEG
                    case "KEY_RIGHT":
                        self.__current_option_index = BodyParts.RIGHT_ARM
                    case "KEY_LEFT":
                        self.__current_option_index = BodyParts.LEFT_ARM
                    case "KEY_UP":
                        self.__current_option_index = BodyParts.HEAD
            case BodyParts.RIGHT_ARM:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = BodyParts.RIGHT_LEG
                    case "KEY_RIGHT":
                        self.__current_option_index = BodyParts.LEFT_ARM
                    case "KEY_LEFT":
                        self.__current_option_index = BodyParts.CHEST
                    case "KEY_UP":
                        self.__current_option_index = BodyParts.HEAD
            case BodyParts.LEFT_LEG:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = BodyParts.HEAD
                    case "KEY_RIGHT":
                        self.__current_option_index = BodyParts.RIGHT_LEG
                    case "KEY_LEFT":
                        self.__current_option_index = BodyParts.RIGHT_LEG
                    case "KEY_UP":
                        self.__current_option_index = BodyParts.CHEST
            case BodyParts.RIGHT_LEG:
                match key:
                    case "KEY_DOWN":
                        self.__current_option_index = BodyParts.HEAD
                    case "KEY_RIGHT":
                        self.__current_option_index = BodyParts.LEFT_LEG
                    case "KEY_LEFT":
                        self.__current_option_index = BodyParts.LEFT_LEG
                    case "KEY_UP":
                        self.__current_option_index = BodyParts.CHEST

    def render(self, screen):
        def write_from_the_back(row_index: int, text: str):
            screen.addstr(row_index, 60 - len(text), text)

        player = self.__game.get_player()
        enemy = self.__game.get_enemy()

        screen.addstr(0, 0, player.name)
        screen.addstr(1, 0, "Health: {0}/{1}".format(str(self.__in_fight_player_health), str(player.health)))

        write_from_the_back(0, enemy.name)
        write_from_the_back(1, "Health: {0}/{1}".format(str(self.__in_fight_enemy_health), str(enemy.health)))

        if self.__turn > 0:
            screen.addstr(3, 0, "Turn {0}:".format(self.__turn))
            screen.addstr(4, 0, self.__last_round_player_log)
            screen.addstr(5, 0, self.__last_round_enemy_log)

        #               ╭─────╮
        #               │  X  │
        #               ╰─────╯
        #       ╭─────╮ ╭─────╮ ╭─────╮
        #       │  X  │ │  X  │ │  X  │
        #       ╰─────╯ ╰─────╯ ╰─────╯
        #          ╭─────╮   ╭─────╮
        #          │  X  │   │  X  │
        #          ╰─────╯   ╰─────╯

        head_sign = "X" if self.__current_option_index == BodyParts.HEAD else " "
        left_arm_sign = "X" if self.__current_option_index == BodyParts.LEFT_ARM else " "
        chest_sign = "X" if self.__current_option_index == BodyParts.CHEST else " "
        right_arm_sign = "X" if self.__current_option_index == BodyParts.RIGHT_ARM else " "
        left_leg_sign = "X" if self.__current_option_index == BodyParts.LEFT_LEG else " "
        right_leg_sign = "X" if self.__current_option_index == BodyParts.RIGHT_LEG else " "

        screen.addstr(7, 27, "╭─────╮")
        screen.addstr(8, 27, "│  {0}  │".format(head_sign))
        screen.addstr(9, 27, "╰─────╯")
        screen.addstr(10, 19, "╭─────╮ ╭─────╮ ╭─────╮")
        screen.addstr(11, 19, "│  {0}  │ │  {1}  │ │  {2}  │".format(left_arm_sign, chest_sign, right_arm_sign))
        screen.addstr(12, 19, "╰─────╯ ╰─────╯ ╰─────╯")
        screen.addstr(13, 22, "╭─────╮   ╭─────╮")
        screen.addstr(14, 22, "│  {0}  │   │  {1}  │".format(left_leg_sign, right_leg_sign))
        screen.addstr(15, 22, "╰─────╯   ╰─────╯")
