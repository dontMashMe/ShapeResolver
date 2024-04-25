import unittest
from shapes.rectangle import Rectangle
from shapes.polygon import Polygon
from shapes.cuboid import Cuboid


class TestShape(unittest.TestCase):
    """
    Mainly testing the input sanitation method,
    """

    def test_sanitize_input_rectangle(self):
        # Test input sanitation for Rectangle
        input_coordinates = "0,0\n5,0\n5,3\n0,3\n"
        expected_tuple_list = [(0, 0), (5, 0), (5, 3), (0, 3)]
        rectangle = Rectangle(input_coordinates)
        actual_tuple_list = rectangle.sanitize_input(input_coordinates)
        self.assertEqual(actual_tuple_list, expected_tuple_list)

    def test_sanitize_input_cuboid(self):
        """
        0, 0, 0
        5, 0, 0
        0, 3, 0
        0, 0, 1
        1, 1, 2
        :return:
        """
        input_coordinates = "0,0,0\n5,0,0\n0,3,0\n0,0,1\n1,1,2\n"
        expected_tuple_list = [(0, 0, 0), (5, 0, 0), (0, 3, 0), (0, 0, 1), (1, 1, 2)]
        cuboid = Cuboid(input_coordinates)
        actual_tuple_list = cuboid.sanitize_input(input_coordinates)
        self.assertEqual(actual_tuple_list, expected_tuple_list)

    """
    def test_sanitize_input_polygon(self):
        # Test input sanitation for Polygon
        input_coordinates = "0,0\n3,0\n3,3\n0,3\n1,1\n2,2\n"
        expected_tuple_list = [(0, 0), (3, 0), (3, 3), (0, 3), (1, 1), (2, 2)]
        polygon = Polygon(input_coordinates)
        actual_tuple_list = polygon.sanitize_input(input_coordinates)
        self.assertEqual(actual_tuple_list, expected_tuple_list)
    """