from shape import *


class ShapeFactory:
    def __init__(self, shape_input: str):
        self.input = shape_input

    def create(self) -> Shape:
        coordinate_count = self.input.count("\n")
        print(coordinate_count)
        match coordinate_count:
            case 3:
                print("Detektiran trokut!")
                return Triangle()
            case 4:
                print("Detektiran kvadar!")
                return Rectangle()
            case _:
                print("Detektiran poligon!")
                return Polygon()
