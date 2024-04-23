from abc import ABC, abstractmethod
from shapes.shape_type import ShapeType


class Shape(ABC):
    @abstractmethod
    def check_if_valid(self) -> bool:
        pass

    @abstractmethod
    def check_if_contains_x(self) -> bool:
        pass

    def sanitize_input(self, input_coordinates: str) -> list[tuple[int, int]]:
        lines = input_coordinates.strip().split('\n')

        tuple_list = []
        for i in range(len(lines)):
            parts = lines[i].strip().split(',')

            if len(parts) == 2:
                x = int(parts[0].strip())
                y = int(parts[1].strip())
                tuple_list.append((x, y))

        return tuple_list

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
