from shapes.shape import Shape
from shapes.triangle import Triangle
from shapes.rectangle import Rectangle
from shapes.polygon import Polygon


class ShapeFactory:
    def __init__(self, shape_input: str):
        self.input = shape_input

    def create(self) -> Shape:
        coordinate_count = self.input.count("\n")
        match coordinate_count:
            case 3:
                print("Detektiran trokut!")
                return Triangle(self.input)
            case 4:
                print("Detektiran kvadar!")
                return Rectangle(self.input)
            case _:
                print("Detektiran poligon!")
                return Polygon(self.input)
