def validate_if_chance_is_valid(chance: float):
    if chance < 0 or chance > 1:
        raise ValueError("Chances must be between 0 and 1")
