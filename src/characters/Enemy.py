from src.chances.do_chances_add_up_to_one import validate_if_chances_add_up_to_one
from src.characters.Body import Body
from src.characters.Character import Character


class Enemy(Character):
    def __init__(self, name: str, health: int, attack: int, defense: int, dodge_chances: Body[float],
                 crit_chance: float, attack_chances: Body[float], exp_reward: int):
        validate_if_chances_add_up_to_one(attack_chances.get_tuple_of_values())
        if exp_reward <= 0:
            raise ValueError("Experience reward must be greater than 0")

        self.attack_chances = attack_chances
        self.exp_reward = exp_reward
        Character.__init__(self, name, health, attack, defense, dodge_chances, crit_chance)
