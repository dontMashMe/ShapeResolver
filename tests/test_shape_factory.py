from unittest import TestCase
from shapes.shape_factory import ShapeFactory
from shapes.rectangle import Rectangle
from shapes.polygon import Polygon
from shapes.cuboid import Cuboid


class TestShapeFactory(TestCase):

    def test_create_rectangle(self):
        # Test creating a Rectangle with 4 coordinates
        input_data = "0,0\n5,0\n5,3\n0,3"
        expected_shape = Rectangle(input_data)
        shape_factory = ShapeFactory(input_data)
        actual_shape = shape_factory.create()
        self.assertIsInstance(actual_shape, Rectangle)
        self.assertEqual(actual_shape.get_type(), expected_shape.get_type())

    def test_create_polygon(self):
        # Test creating a Polygon with more than 4 coordinates
        input_data = "0,0\n3,0\n3,3\n0,3\n1,1\n2,2\n"
        expected_shape = Polygon(input_data)
        shape_factory = ShapeFactory(input_data)
        actual_shape = shape_factory.create()
        self.assertIsInstance(actual_shape, Polygon)
        self.assertEqual(actual_shape.get_type(), expected_shape.get_type())

    def test_create_cuboid(self):
        input_data = "0,0,0\n5,0,0\n0,3,0\n0,0,1\n1,1,2"
        expected_shape = Cuboid(input_data)
        shape_factory = ShapeFactory(input_data)
        actual_shape = shape_factory.create()
        self.assertIsInstance(actual_shape, Cuboid)
        self.assertEqual(actual_shape.get_type(), expected_shape.get_type())

    def test_create_polygon_with_less_than_3_coordinates(self):
        # Test creating a Polygon with less than 3 coordinates (invalid case)
        input_data = "0,0\n3,0"
        shape_factory = ShapeFactory(input_data)
        with self.assertRaises(ValueError):
            shape_factory.create()
