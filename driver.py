from input_reader import InputReader
from shapes.shape import Shape
from shapes.shape_factory import ShapeFactory


class Driver:
    def __init__(self, input_file: str):
        self.input_file = input_file

    def do_run(self) -> None:
        """
        1. load the input
        2. check if edges form a valid shape
            return with error if not.
        3. check if shape contains edge 'x'
        4. calc the diagonal
        :return:
        """
        input_coordinates = self.__get_input(self.input_file)
        shape = self.__get_shape_type(input_coordinates)
        if not shape.check_if_valid():
            print("Ulazne koordinate ne sačinjavaju pravilan lik!")
            exit(0)
        print(shape.check_if_contains_x())

    def __get_input(self, input_file: str) -> str:
        temp_input_var = InputReader(input_file).load_file()
        print("Učitane koordinate: ")
        for line in temp_input_var.split("\n"):
            print(line)
        return temp_input_var

    def __get_shape_type(self, input_coordinates: str) -> Shape:
        shape_factory = ShapeFactory(input_coordinates)
        return shape_factory.create()
