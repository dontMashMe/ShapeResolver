from shapes.shape import Shape


class Rectangle(Shape):
    def __init__(self, input_coordinates: str):
        self.sanitized_input = self.sanitize_input(input_coordinates)

    def sanitize_input(self, input_coordinates: str) -> list[tuple]:
        pass

    def check_if_valid(self) -> bool:
        pass

    def check_if_contains_x(self) -> bool:
        pass
