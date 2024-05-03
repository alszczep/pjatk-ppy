from src.characters.body.Body import Body
from src.characters.enemies.Enemy import Enemy

wolf = Enemy(
    "Wolf",
    150,
    35,
    0,
    Body(1.0, 0.3, 0.1, 0.3, 0.1, 0.1),
    0,
    Body(0.0, 0.1, 0.1, 0.1, 0.35, 0.35),
    20)

bear = Enemy(
    "Bear",
    300,
    60,
    0,
    Body(1.0, 0.1, 0.1, 0.1, 0.0, 0.0),
    0,
    Body(0.0, 0.15, 0.2, 0.15, 0.25, 0.25),
    50)

elfArcher = Enemy(
    "Elf Archer",
    200,
    100,
    10,
    Body(0.4, 0.3, 0.2, 0.4, 0.2, 0.2),
    0.2,
    Body(0.5, 0.1, 0.2, 0.1, 0.05, 0.05),
    150)

elfAssassin = Enemy(
    "Elf Assassin",
    200,
    200,
    15,
    Body(0.4, 0.4, 0.4, 0.4, 0.2, 0.2),
    0.5,
    Body(0.5, 0.05, 0.4, 0.05, 0.0, 0.0),
    250)
