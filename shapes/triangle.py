from shapes.shape import Shape
import math


class Triangle(Shape):
    def __init__(self, input_coordinates: str):
        self.sanitized_input = self.sanitize_input(input_coordinates)

    def check_if_valid(self) -> bool:
        """
            Calculate the distances between the points, and then apply the Pythagorean theorem.

            return True if Triangle is a "right" triangle, false otherwise.
        """
        point_one = self.sanitized_input[0]  # 0, 0
        point_two = self.sanitized_input[1]  # 5, 0
        point_three = self.sanitized_input[2]  # 2, 2

        side1_sq = (point_two[0] - point_one[0]) ** 2 + (point_two[1] - point_one[1]) ** 2
        side2_sq = (point_three[0] - point_two[0]) ** 2 + (point_three[1] - point_two[1]) ** 2
        side3_sq = (point_one[0] - point_three[0]) ** 2 + (point_one[1] - point_three[1]) ** 2

        sides_sq = sorted([side1_sq, side2_sq, side3_sq])
        return math.isclose(sides_sq[0] + sides_sq[1], sides_sq[2])

    def check_if_contains_x(self) -> bool:
        pass

    def sanitize_input(self, input_coordinates: str) -> list[tuple]:
        lines = input_coordinates.strip().split('\n')

        tuple_list = []
        for i in range(min(len(lines), 3)):
            parts = lines[i].strip().split(',')

            if len(parts) == 2:
                x = int(parts[0].strip())
                y = int(parts[1].strip())
                tuple_list.append((x, y))

        return tuple_list
