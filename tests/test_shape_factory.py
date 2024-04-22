from unittest import TestCase
from shapes.shape_factory import ShapeFactory
from shapes.triangle import Triangle
from shapes.rectangle import Rectangle
from shapes.polygon import Polygon


class TestShapeFactory(TestCase):
    def test_create_triangle(self):
        # Test creating a Triangle with 3 coordinates
        input_data = "0,0\n3,0\n0,4\n"
        expected_shape = Triangle(input_data)
        shape_factory = ShapeFactory(input_data)
        actual_shape = shape_factory.create()
        self.assertIsInstance(actual_shape, Triangle)
        self.assertEqual(actual_shape.get_type(), expected_shape.get_type())

    def test_create_rectangle(self):
        # Test creating a Rectangle with 4 coordinates
        input_data = "0,0\n5,0\n5,3\n0,3\n"
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
