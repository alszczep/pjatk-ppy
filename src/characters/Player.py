from src.characters.Body import Body
from src.characters.Character import Character
from src.characters.leveling import exp_to_level
from src.utils.fix_round_off import fix_round_off

HEALTH_PER_LEVEL = 10
ATTACK_PER_LEVEL = 2
DEFENSE_PER_LEVEL = 1

HEALTH_PER_SKILL_POINT = 15
ATTACK_PER_SKILL_POINT = 4
DEFENSE_PER_SKILL_POINT = 2
CRIT_CHANCE_PER_SKILL_POINT = 0.01


class Player(Character):
    def __init__(self, name: str, health: int, attack: int, defense: int,
                 crit_chance: float, exp: int, skill_points: int):
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
            self.health += (HEALTH_PER_LEVEL * levels_up)
            self.attack += (ATTACK_PER_LEVEL * levels_up)
            self.defense += (DEFENSE_PER_LEVEL * levels_up)
            self.skill_points += (1 * levels_up)

    def spend_skill_points(self, amount_to_spend: int = 1):
        if amount_to_spend <= 0:
            return

        if self.skill_points < amount_to_spend:
            raise ValueError("Not enough skill points")

        self.skill_points -= amount_to_spend

    def upgrade_health(self, amount_to_spend: int = 1):
        if amount_to_spend <= 0:
            return

        self.spend_skill_points(amount_to_spend)
        self.health += (HEALTH_PER_SKILL_POINT * amount_to_spend)

    def upgrade_attack(self, amount_to_spend: int = 1):
        if amount_to_spend <= 0:
            return

        self.spend_skill_points(amount_to_spend)
        self.attack += (ATTACK_PER_SKILL_POINT * amount_to_spend)

    def upgrade_defense(self, amount_to_spend: int = 1):
        if amount_to_spend <= 0:
            return

        self.spend_skill_points(amount_to_spend)
        self.defense += (DEFENSE_PER_SKILL_POINT * amount_to_spend)

    def upgrade_crit_chance(self, amount_to_spend: int = 1):
        if amount_to_spend <= 0:
            return

        if self.crit_chance >= 0.5:
            raise ValueError("Crit chance is already maxed out")

        self.spend_skill_points(amount_to_spend)
        self.crit_chance = fix_round_off(self.crit_chance + CRIT_CHANCE_PER_SKILL_POINT * amount_to_spend)

    def gain_exp(self, exp: int):
        if exp <= 0:
            raise ValueError("Experience reward must be greater than 0")

        self.exp += exp
        self.recalculate_level()


def create_new_player(name: str):
    return Player(name, 200, 50, 10, 0.05, 0, 0)
