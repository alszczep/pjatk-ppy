from src.chances.element_by_chance import element_by_chance
from src.chances.validate_if_chances_add_up_to_one import validate_if_chances_add_up_to_one
from src.characters.Character import Character
from src.characters.body.Body import Body
from src.characters.body.BodyParts import BodyParts


class Enemy(Character):
    def __init__(self, name: str, health: int, attack: int, defense: int, dodge_chances: Body[float],
                 crit_chance: float, attack_chances: Body[float], exp_reward: int):
        validate_if_chances_add_up_to_one(attack_chances.get_tuple_of_values())
        if exp_reward <= 0:
            raise ValueError("Experience reward must be greater than 0")

        self.attack_chances = attack_chances
        self.exp_reward = exp_reward
        Character.__init__(self, name, health, attack, defense, dodge_chances, crit_chance)

    def get_attacked_body_part(self) -> BodyParts:
        attack_chances = tuple(map(lambda i: (i[1], i[0]), self.attack_chances.values.items()))
        return element_by_chance(attack_chances)
