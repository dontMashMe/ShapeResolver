import unittest
from shapes.cuboid import Cuboid
import math


class TestCuboid(unittest.TestCase):
    def test_valid_cuboid(self):
        # Test to check if given vertices form a valid cuboid (should return True)
        input_coordinates = "0, 0, 0\n 4, 0, 0\n 0, 3, 0\n 0, 0, 2\n 1, 1, 2"
        cuboid = Cuboid(input_coordinates)
        self.assertTrue(cuboid.check_if_valid())

    def test_invalid_cuboid(self):
        # Test to check if given vertices do not form a valid cuboid (should return False)
        input_coordinates = "0, 0, 0\n 5, 0, 0\n 1, 3, 0\n 0, 0, 2\n 1, 1, 1"
        cuboid = Cuboid(input_coordinates)
        self.assertFalse(cuboid.check_if_valid())

    def test_point_inside_cuboid(self):
        # Test to check if a point inside the cuboid is correctly detected (should return True)
        input_coordinates = "0, 0, 0\n4, 0, 0\n0, 3, 0\n0, 0, 2\n2, 1, 1"
        cuboid = Cuboid(input_coordinates)
        self.assertTrue(cuboid.check_if_contains_x())

    def test_point_outside_cuboid(self):
        # Test to check if a point outside the cuboid is correctly detected (should return False)
        vertices = "0, 0, 0\n 4, 0, 0\n 0, 3, 0\n 0, 0, 2\n 5, 5, 5"
        cuboid = Cuboid(vertices)
        self.assertFalse(cuboid.check_if_contains_x())

    def test_calculate_spatial_diagonal(self):
        vertices = "0, 0, 0\n 4, 0, 0\n 0, 3, 0\n 0, 0, 2\n1,1,1"
        cuboid = Cuboid(vertices)

        # Expected spatial diagonal length (calculated manually)
        expected_diagonal_length = math.sqrt(4 ** 2 + 3 ** 2 + 2 ** 2)
        actual_diagonal_length = cuboid.get_diagonal()
        self.assertAlmostEqual(actual_diagonal_length, expected_diagonal_length, places=6)


if __name__ == "__main__":
    unittest.main()
