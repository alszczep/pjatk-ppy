from random import random
from typing import TypeVar

from src.chances.validate_if_chances_add_up_to_one import validate_if_chances_add_up_to_one

T = TypeVar('T')


def element_by_chance(chances: tuple[tuple[float, T], ...]):
    validate_if_chances_add_up_to_one(tuple(chance for chance, _ in chances))
    random_number = random()
    current_chance = 0.0

    for chance, element in chances:
        current_chance += chance
        if random_number < current_chance:
            return element

    return chances[0][1]
