from typing import TypeVar

from src.chances.chance_to_outcome import chance_to_outcome
from src.chances.validate_if_chance_is_valid import validate_if_chance_is_valid
from src.characters.Attack import Attack, AttackResult
from src.characters.Body import Body
from src.characters.BodyParts import BodyParts

TCharacter = TypeVar('TCharacter', bound='Character')


class Character:
    def __init__(self, name: str, health: int, attack: int, defense: int, dodge_chances: Body[float],
                 crit_chance: float):
        if health <= 0:
            raise ValueError("Health must be greater than 0")
        if attack <= 0:
            raise ValueError("Attack must be greater than 0")
        if defense < 0:
            raise ValueError("Defense must be greater or equal 0")
        for dodge_chance in dodge_chances.get_tuple_of_values():
            validate_if_chance_is_valid(dodge_chance)
        validate_if_chance_is_valid(crit_chance)

        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.dodge_chances = dodge_chances
        self.crit_chance = crit_chance

    def calculate_attack(self, target: TCharacter, body_part: BodyParts) -> Attack:
        dodge_chance: float = target.dodge_chances.get_tuple_of_values()[body_part.value]
        if chance_to_outcome(dodge_chance):
            return Attack(AttackResult.DODGE, 0)

        attack = self.attack

        with_crit = chance_to_outcome(self.crit_chance)
        if with_crit:
            attack *= 2

        attack -= target.defense
        if attack < 0:
            attack = 0

        return Attack(AttackResult.DAMAGE_WITH_CRIT if with_crit else AttackResult.DAMAGE, attack)
