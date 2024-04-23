from shapes.shape import Shape
from shapes.shape_type import ShapeType


class Rectangle(Shape):
    def __init__(self, input_coordinates: str):
        self.sanitized_input = self.sanitize_input(input_coordinates)
        self.point_d = self.find_fourth_vertex(
            self.sanitized_input[0], self.sanitized_input[1], self.sanitized_input[2]
        )

    def find_fourth_vertex(self, point_a: tuple, point_b: tuple, point_c: tuple) -> tuple[int, int]:
        # Calculate the midpoint between point_b and point_c
        mid_point = ((point_b[0] + point_c[0]) / 2, (point_b[1] + point_c[1]) / 2)

        # Calculate the coordinates of point_d using the formula:
        # point_d = 2 * mid_point - point_a
        point_d_x = int(2 * mid_point[0] - point_a[0])
        point_d_y = int(2 * mid_point[1] - point_a[1])

        return point_d_x, point_d_y

    def check_if_valid(self) -> bool:
        all_points: list[tuple[int, int]] = self.sanitized_input[:3]  # take the first three points, ignoring the X
        all_points.append(self.point_d)

        (x1, y1), (x2, y2), (x3, y3), (x4, y4) = all_points

        cx = (x1 + x2 + x3 + x4) / 4
        cy = (y1 + y2 + y3 + y4) / 4

        dd1 = (cx - x1) ** 2 + (cy - y1) ** 2
        dd2 = (cx - x2) ** 2 + (cy - y2) ** 2
        dd3 = (cx - x3) ** 2 + (cy - y3) ** 2
        dd4 = (cx - x4) ** 2 + (cy - y4) ** 2
        return dd1 == dd2 == dd3 == dd4

    def check_if_contains_x(self) -> bool:
        pass

    def get_type(self):
        return ShapeType.RECTANGLE
