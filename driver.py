from input_reader import InputReader
from shapes.shape import Shape
from shape_factory import ShapeFactory


class Driver:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.input_coordinates = self.get_input()
        self.shape = self.get_shape_type()

    def get_input(self) -> str:
        temp_input_var = InputReader(self.input_file).load_file()
        print("Učitane koordinate: ")
        for line in temp_input_var.split("\n"):
            print(line)
        return temp_input_var

    def get_shape_type(self) -> Shape:
        shape_factory = ShapeFactory(self.input_coordinates)
        return shape_factory.create()

    def check_if_valid(self) -> bool:
        pass
