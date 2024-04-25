from shapes.shape import Shape
from shapes.shape_type import ShapeType


class Cuboid(Shape):
    def __init__(self, input_coordinates: str):
        self.sanitized_input = self.sanitize_input(input_coordinates)
        self.all_points = self.sanitized_input[:4]  # take the first 4 points, ignoring the X

    def check_if_valid(self) -> bool:
        pass

    def check_if_contains_x(self) -> bool:
        pass

    def get_diagonal(self) -> float:
        pass

    def sanitize_input(self, input_coordinates: str) -> list[tuple[int, int, int]]:
        lines = input_coordinates.strip().split('\n')

        tuple_list = []
        for i in range(len(lines)):
            parts = lines[i].strip().split(',')

            if len(parts) == 3:
                x = int(parts[0].strip())
                y = int(parts[1].strip())
                z = int(parts[2].strip())
                tuple_list.append((x, y, z))

        return tuple_list

    def get_type(self) -> ShapeType:
        pass
