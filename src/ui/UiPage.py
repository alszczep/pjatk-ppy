from abc import ABC, abstractmethod


class UiPage(ABC):
    @abstractmethod
    def handle_key(self, key: str):
        pass

    @abstractmethod
    def render(self, screen):
        pass
