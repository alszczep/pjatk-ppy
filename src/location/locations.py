from src.characters.enemies.enemies import wolf, elfArcher, bear, elfAssassin
from src.location.Location import Location

forest = Location(
    "Forest",
    1,
    10,
    [(0.5, wolf), (0.4, bear), (0.1, elfArcher)])

elvenFortress = Location(
    "Elven Fortress",
    11,
    20,
    [(0.7, elfArcher), (0.3, elfAssassin)])

locations = (forest, elvenFortress)
