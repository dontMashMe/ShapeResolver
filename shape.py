from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def check_if_valid(self):
        pass

    @abstractmethod
    def check_if_contains_x(self):
        pass


class Triangle(Shape):
    def check_if_valid(self):
        pass

    def check_if_contains_x(self):
        pass


class Rectangle(Shape):

    def check_if_valid(self):
        pass

    def check_if_contains_x(self):
        pass


class Polygon(Shape):
    def check_if_valid(self):
        pass

    def check_if_contains_x(self):
        pass
