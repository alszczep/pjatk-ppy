import json

from src.characters.Player import Player


def save_player(player: Player):
    with open("player.json", "w") as file:
        json.dump({
            "name": player.name,
            "health": player.health,
            "attack": player.attack,
            "defense": player.defense,
            "crit_chance": player.crit_chance,
            "exp": player.exp,
            "skill_points": player.skill_points,
        }, file)
