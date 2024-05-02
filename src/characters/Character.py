from src.chances.validate_if_chance_is_valid import validate_if_chance_is_valid
from src.characters.Body import Body


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
