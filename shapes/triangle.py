from shapes.shape import Shape


class Triangle(Shape):
    def __init__(self, input_coordinates: str):
        self.sanitized_input = self.sanitize_input(input_coordinates)

    def check_if_valid(self) -> bool:
        for _tuple in self.sanitized_input:
            print(_tuple)
        return True

    def check_if_contains_x(self) -> bool:
        pass

    def sanitize_input(self, input_coordinates: str) -> list[tuple]:
        lines = input_coordinates.strip().split('\n')

        tuple_list = []
        for i in range(min(len(lines), 3)):
            parts = lines[i].strip().split(',')

            if len(parts) == 2:
                x = int(parts[0].strip())
                y = int(parts[1].strip())
                tuple_list.append((x, y))

        return tuple_list
