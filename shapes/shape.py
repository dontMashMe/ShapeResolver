from abc import ABC, abstractmethod
from shapes.shape_type import ShapeType


class Shape(ABC):
    @abstractmethod
    def check_if_valid(self) -> bool:
        pass

    @abstractmethod
    def check_if_contains_x(self) -> bool:
        pass

    @abstractmethod
    def sanitize_input(self, input_coordinates: str):
        pass

    @abstractmethod
    def get_diagonal(self) -> float:
        pass

    @abstractmethod
    def get_type(self) -> ShapeType:
        """
        This method is only used for assertions in Unit testing.
        :return: ShapeType
        """
        pass
