import unittest
from shapes.rectangle import Rectangle  # Assuming Rectangle class is defined in rectangle.py


class TestRectangle(unittest.TestCase):
    def test_find_fourth_vertex(self):
        input_coordinates = "0,0\n5,0\n0,3"
        rectangle = Rectangle(input_coordinates)
        expected_point_d = (5, 3)
        actual_point_d = rectangle.all_points[len(rectangle.all_points) - 1]
        self.assertEqual(actual_point_d, expected_point_d)

    def test_valid_rectangle(self):
        input_coordinates = "0,0\n5,0\n0,3"
        rectangle = Rectangle(input_coordinates)
        self.assertTrue(rectangle.check_if_valid())

    def test_invalid_rectangle(self):
        input_coordinates = "0,0\n5,0\n1,3"
        rectangle = Rectangle(input_coordinates)
        self.assertFalse(rectangle.check_if_valid())

    def test_check_if_contains_x_inside(self):
        # Test to check if a point inside the rectangle is correctly detected (should return True)
        input_coordinates = "0,0\n5,0\n0,3\n2,2"  # Rectangle with vertices (0,0), (5,0), (0,3), (5,3)
        rectangle = Rectangle(input_coordinates)
        self.assertTrue(rectangle.check_if_contains_x())

    def test_check_if_contains_x_outside(self):
        # Test to check if a point outside the rectangle is correctly detected (should return False)
        input_coordinates = "0,0\n5,0\n0,3\n5,3\n6,2"  # Rectangle with vertices (0,0), (5,0), (0,3), (5,3)
        rectangle = Rectangle(input_coordinates)
        self.assertFalse(rectangle.check_if_contains_x())
