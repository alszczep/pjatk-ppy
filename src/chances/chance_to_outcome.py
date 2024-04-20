from random import random


def chance_to_outcome(chance: float) -> bool:
    return random() < chance
