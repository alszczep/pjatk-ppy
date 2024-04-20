from math import floor


def level_to_exp(level: int):
    if level == 1:
        return 0
    if level < 10:
        return floor(((level - 1) * 10) ** 1.3)
    return floor(level ** 2.5 + 50)


def exp_to_level(exp: int):
    level = ((exp + 1) ** (10 / 13)) / 10 + 1

    if level < 10:
        return floor(level)

    return floor((exp - 50 + 1) ** (10 / 25))
