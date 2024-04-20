from src.chances.validate_if_chance_is_valid import validate_if_chance_is_valid


def validate_if_chances_add_up_to_one(chances: tuple[float, ...]):
    for chance in chances:
        validate_if_chance_is_valid(chance)

    if round(sum(chances), 10) != 1.0:
        raise ValueError("Chances must add up to 1")
