from shapes.shape import Shape
from shapes.shape_type import ShapeType
import math


class Cuboid(Shape):
    def __init__(self, input_coordinates: str):
        self.sanitized_input = self.sanitize_input(input_coordinates)
        self.all_points = self.sanitized_input[:4]  # take the first 4 points, ignoring the X

    def check_if_valid(self) -> bool:
        edge_lengths = []
        for i in range(4):
            for j in range(i + 1, 4):
                dist = math.sqrt(sum((self.all_points[i][k] - self.all_points[j][k]) ** 2 for k in range(3)))
                edge_lengths.append(dist)

        # Check if there are exactly 6 unique edge lengths (4 edges for the sides and 2 diagonals)
        unique_edge_lengths = set(edge_lengths)
        if len(unique_edge_lengths) != 6:
            return False

        # Check if opposite edges are perpendicular (dot product of vectors is zero for perpendicularity)
        # We check if AB is perpendicular to AD and AC is perpendicular to AD
        # Vector AB = B - A, Vector AD = D - A, Vector AC = C - A
        vector_ab = tuple(self.all_points[1][k] - self.all_points[0][k] for k in range(3))
        vector_ad = tuple(self.all_points[3][k] - self.all_points[0][k] for k in range(3))
        vector_ac = tuple(self.all_points[2][k] - self.all_points[0][k] for k in range(3))

        # Calculate dot products to check perpendicularity
        dot_product_ab_ad = sum(vector_ab[k] * vector_ad[k] for k in range(3))
        dot_product_ac_ad = sum(vector_ac[k] * vector_ad[k] for k in range(3))

        epsilon = 1e-6  # Small value for floating-point comparison
        if (not math.isclose(dot_product_ab_ad, 0.0, abs_tol=epsilon)
                or not math.isclose(dot_product_ac_ad, 0.0, abs_tol=epsilon)):
            return False

        return True

    def check_if_contains_x(self) -> bool:
        # coordinates of the X
        x, y, z = self.sanitized_input[len(self.sanitized_input) - 1]

        x_values = [vertex[0] for vertex in self.all_points]
        y_values = [vertex[1] for vertex in self.all_points]
        z_values = [vertex[2] for vertex in self.all_points]

        x_min, x_max = min(x_values), max(x_values)
        y_min, y_max = min(y_values), max(y_values)
        z_min, z_max = min(z_values), max(z_values)

        # Check if the point (x, y, z) is inside the cuboid's bounding box
        if (x_min <= x <= x_max) and (y_min <= y <= y_max) and (z_min <= z <= z_max):
            return True
        else:
            return False

    def get_diagonal(self) -> float:
        a = math.dist(self.all_points[0], self.all_points[1])  # Distance between all_points A and B
        b = math.dist(self.all_points[0], self.all_points[2])  # Distance between all_points A and C
        c = math.dist(self.all_points[0], self.all_points[3])  # Distance between all_points A and D

        # Calculate the spatial diagonal using the formula: d = sqrt(a^2 + b^2 + c^2)
        d = math.sqrt(a ** 2 + b ** 2 + c ** 2)

        return d

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
        return ShapeType.CUBOID
