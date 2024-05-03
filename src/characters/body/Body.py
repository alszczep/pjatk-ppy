from typing import Generic, TypeVar

from src.characters.body.BodyParts import BodyParts

T = TypeVar('T')


class Body(Generic[T]):
    def __init__(self, head: T, left_arm: T, chest: T, right_arm: T, left_leg: T, right_leg: T):
        self.values = {
            BodyParts.HEAD: head,
            BodyParts.LEFT_ARM: left_arm,
            BodyParts.CHEST: chest,
            BodyParts.RIGHT_ARM: right_arm,
            BodyParts.LEFT_LEG: left_leg,
            BodyParts.RIGHT_LEG: right_leg
        }

    def get_tuple_of_values(self) -> tuple[T, T, T, T, T, T]:
        return (self.values[BodyParts.HEAD], self.values[BodyParts.LEFT_ARM], self.values[BodyParts.CHEST],
                self.values[BodyParts.RIGHT_ARM], self.values[BodyParts.LEFT_LEG], self.values[BodyParts.RIGHT_LEG])
