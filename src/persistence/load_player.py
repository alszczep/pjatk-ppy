import json
from pathlib import Path

from src.characters.Player import Player


def load_player() -> Player | None:
    if not Path("player.json").exists():
        return None

    with open("player.json", "r") as file:
        data = json.load(file)
        return Player(
            data["name"],
            data["health"],
            data["attack"],
            data["defense"],
            data["crit_chance"],
            data["exp"],
            data["skill_points"],
        )
