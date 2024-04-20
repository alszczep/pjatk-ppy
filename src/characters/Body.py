from typing import Generic, TypeVar

T = TypeVar('T')


class Body(Generic[T]):
    def __init__(self, head: T, left_arm: T, chest: T, right_arm: T, left_leg: T, right_leg: T):
        self.head = head
        self.left_arm = left_arm
        self.chest = chest
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg

    def get_array_of_values(self) -> tuple[T, T, T, T, T, T]:
        return self.head, self.left_arm, self.chest, self.right_arm, self.left_leg, self.right_leg
