"""This module defines the Rectangle class."""

__author__ = "Jaskarandeep kaur"
__version__ = "25.09.25"

from .shape import Shape

class Rectangle(Shape):
    """
    Rectangle class with length and width in centimeters.
    """

    def __init__(self, color: str, length: int, width: int):
        super().__init__(color)

        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")

        self._length = length
        self._width = width

    def __str__(self) -> str:
        base = super().__str__()
        return (f"{base}\n"
                f"This rectangle has four sides with the lengths of "
                f"{self._length}, {self._width}, {self._length} and {self._width} centimeters.")

    def calculate_area(self) -> int:
        return self._length * self._width

    def calculate_perimeter(self) -> int:
        return 2 * (self._length + self._width)
