from enum import Enum


class AttackResult(Enum):
    DAMAGE = 0
    DAMAGE_WITH_CRIT = 1
    DODGE = 2


class Attack:
    def __init__(self, result: AttackResult, damage: int):
        self.result = result
        self.damage = damage
