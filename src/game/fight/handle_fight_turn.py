from enum import Enum

from src.characters.Character import Character
from src.characters.Player import Player
from src.characters.body.BodyParts import BodyParts
from src.characters.enemies.Enemy import Enemy
from src.game.fight.Attack import AttackResult


class FightSingleTurn:
    def __init__(self, damage_dealt: int, log: str):
        self.damage_dealt = damage_dealt
        self.log = log


class FightTurnResult(Enum):
    FIGHT_CONTINUES = 0
    ENEMY_KILLED = 1
    PLAYER_KILLED = 2


class FightTurn:
    def __init__(self, result: FightTurnResult, player_turn: FightSingleTurn, enemy_turn: FightSingleTurn):
        self.result = result
        self.player_turn = player_turn
        self.enemy_turn = enemy_turn


def get_dodge_log(attacker: Character, attacked: Character) -> str:
    return "{0} attacked, but {1} dodged".format(attacker.name, attacked.name)


def get_damage_log(attacker: Character, attacked: Character, damage: int, with_crit: bool) -> str:
    crit_text = " critically" if with_crit else ""
    return "{0} attacked {1}{2} for {3} damage".format(attacker.name, attacked.name, crit_text, damage)


def handle_fight_turn(player: Player, enemy: Enemy, player_health: int, enemy_health: int,
                      player_attack_body_part: BodyParts) -> FightTurn:
    player_attack_result = player.calculate_attack(enemy, player_attack_body_part)

    player_turn = FightSingleTurn(0, "")
    enemy_turn = FightSingleTurn(0, "")

    if player_attack_result.result == AttackResult.DODGE:
        player_turn.log = get_dodge_log(player, enemy)
    else:
        enemy_health -= player_attack_result.damage
        player_turn.damage_dealt = player_attack_result.damage
        player_turn.log = get_damage_log(player, enemy, player_attack_result.damage,
                                         player_attack_result.result == AttackResult.DAMAGE_WITH_CRIT)

    if enemy_health <= 0:
        return FightTurn(FightTurnResult.ENEMY_KILLED, player_turn, enemy_turn)

    attacked_body_part = enemy.get_attacked_body_part()
    enemy_attack_result = enemy.calculate_attack(player, attacked_body_part)

    if enemy_attack_result.result == AttackResult.DODGE:
        enemy_turn.log = get_dodge_log(enemy, player)
    else:
        player_health -= enemy_attack_result.damage
        enemy_turn.damage_dealt = enemy_attack_result.damage
        enemy_turn.log = get_damage_log(enemy, player, enemy_attack_result.damage,
                                        enemy_attack_result.result == AttackResult.DAMAGE_WITH_CRIT)

    if player_health <= 0:
        return FightTurn(FightTurnResult.PLAYER_KILLED, player_turn, enemy_turn)

    return FightTurn(FightTurnResult.FIGHT_CONTINUES, player_turn, enemy_turn)
