from src.chances.validate_if_chances_add_up_to_one import validate_if_chances_add_up_to_one
from src.characters.enemies.Enemy import Enemy


class Location:
    def __init__(self, name: str, recommended_level_from: int, recommended_level_to: int,
                 enemies: list[tuple[float, Enemy]]):
        if recommended_level_from < 0:
            raise ValueError("Recommended level from must be greater or equal to 0")
        if recommended_level_to < 0:
            raise ValueError("Recommended level to must be greater or equal to 0")
        if recommended_level_from > recommended_level_to:
            raise ValueError("Recommended level from must be less than recommended level to")
        if len(enemies) == 0:
            raise ValueError("Location must have at least one enemy")

        chances = tuple(chance for chance, _ in enemies)
        validate_if_chances_add_up_to_one(chances)

        self.name = name
        self.recommended_level_from = recommended_level_from
        self.recommended_level_to = recommended_level_to
        self.enemies = enemies
