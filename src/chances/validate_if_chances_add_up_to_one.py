from src.chances.validate_if_chance_is_valid import validate_if_chance_is_valid
from src.utils.fix_round_off import fix_round_off


def validate_if_chances_add_up_to_one(chances: tuple[float, ...]):
    for chance in chances:
        validate_if_chance_is_valid(chance)

    if fix_round_off(sum(chances)) != 1.0:
        raise ValueError("Chances must add up to 1")
