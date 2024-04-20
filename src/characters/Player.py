from src.characters.Body import Body
from src.characters.Character import Character
from src.characters.leveling import exp_to_level


class Player(Character):
    def __init__(self, name: str, health: int, attack: int, defense: int,
                 crit_chance: float, exp: int, skill_points: int):
        if exp <= 0:
            raise ValueError("Experience reward must be greater than 0")
        if skill_points < 0:
            raise ValueError("Skill points must be greater or equal to 0")

        dodge_chances = Body(0.2, 0.1, 0.0, 0.1, 0.1, 0.1)

        self.exp = exp
        self.level = exp_to_level(exp)
        self.skill_points = skill_points
        Character.__init__(self, name, health, attack, defense, dodge_chances, crit_chance)

    def recalculate_level(self):
        new_level = exp_to_level(self.exp)

        if new_level > self.level:
            levels_up = new_level - self.level

            self.level = new_level
            self.health += (10 * levels_up)
            self.attack += (3 * levels_up)
            self.defense += (1 * levels_up)
            self.skill_points += (1 * levels_up)

    def spend_skill_point(self):
        if self.skill_points == 0:
            raise ValueError("Not enough skill points")

        self.skill_points -= 1

    def upgrade_health(self):
        self.spend_skill_point()
        self.health += 20

    def upgrade_attack(self):
        self.spend_skill_point()
        self.attack += 6

    def upgrade_defense(self):
        self.spend_skill_point()
        self.defense += 2

    def upgrade_crit_chance(self):
        if self.crit_chance >= 0.5:
            raise ValueError("Crit chance is already maxed out")

        self.spend_skill_point()
        self.crit_chance += 0.01

    def gain_exp(self, exp: int):
        if exp <= 0:
            raise ValueError("Experience reward must be greater than 0")

        self.exp += exp
        self.recalculate_level()


def create_new_player(name: str):
    return Player(name, 200, 50, 10, 0.05, 0, 0)
