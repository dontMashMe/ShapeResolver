from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def check_if_valid(self, input_coordinates: str) -> bool:
        pass

    @abstractmethod
    def check_if_contains_x(self) -> bool:
        pass