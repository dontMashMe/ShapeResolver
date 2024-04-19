from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def check_if_valid(self) -> bool:
        pass

    @abstractmethod
    def check_if_contains_x(self) -> bool:
        pass

    @abstractmethod
    def sanitize_input(self, input_coordinates: str) -> list[tuple]:
        pass
