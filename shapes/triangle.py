from shapes.shape import Shape
from shapes.shape_type import ShapeType
import math


def area(x1, y1, x2, y2, x3, y3) -> int:
    """
    Helper function for calculating area of a triangle.
    """
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


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
        point_three = self.sanitized_input[2]  # 0, 5

        side1_sq = (point_two[0] - point_one[0]) ** 2 + (point_two[1] - point_one[1]) ** 2
        side2_sq = (point_three[0] - point_two[0]) ** 2 + (point_three[1] - point_two[1]) ** 2
        side3_sq = (point_one[0] - point_three[0]) ** 2 + (point_one[1] - point_three[1]) ** 2

        sides_sq = sorted([side1_sq, side2_sq, side3_sq])
        return math.isclose(sides_sq[0] + sides_sq[1], sides_sq[2])

    def check_if_contains_x(self) -> bool:
        """
        Let the coordinates of the three corners be (x1, y1), (x2, y2), and (x3, y3). And coordinates of the given point
        P be (x, y)

        Calculate the area of the given triangle, i.e., the area of the triangle ABC in the above diagram.
        Area A = [ x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2)]/2

        Calculate the area of the triangle PAB. We can use the same formula for this. Let this area be A1.
        Calculate the area of the triangle PBC. Let this area be A2.
        Calculate the area of the triangle PAC. Let this area be A3.
        If P lies inside the triangle, then A1 + A2 + A3 must be equal to A.

        :return: True if triangle contains point, else False
        """
        point_x = self.sanitized_input[len(self.sanitized_input) - 1]

        # Extract the vertices out of sanitized input
        x1 = self.sanitized_input[0][0]
        x2 = self.sanitized_input[1][0]
        x3 = self.sanitized_input[2][0]

        y1 = self.sanitized_input[0][1]
        y2 = self.sanitized_input[1][1]
        y3 = self.sanitized_input[2][1]

        abc_triangle_area = area(x1, y1, x2, y2, x3, y3)
        pbc_triangle_area = area(point_x[0], point_x[1], x2, y2, x3, y3)
        pac_triangle_area = area(x1, y1, point_x[0], point_x[1], x3, y3)
        pab_triangle_area = area(x1, y1, x2, y2, point_x[0], point_x[1])

        # Check if sum of PBC, PAC, PAB triangles equals ABC
        return abc_triangle_area == (pbc_triangle_area + pac_triangle_area + pab_triangle_area)

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

    def get_type(self):
        return ShapeType.TRIANGLE
