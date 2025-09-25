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

import unittest
from shape import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r = Rectangle("red", 5, 6)

    def test_str(self):
        expected = ("The shape color is red.\n"
                    "This rectangle has four sides with the lengths of 5, 6, 5 and 6 centimeters.")
        self.assertEqual(str(self.r), expected)

    def test_area(self):
        self.assertEqual(self.r.calculate_area(), 30)

    def test_perimeter(self):
        self.assertEqual(self.r.calculate_perimeter(), 22)

    def test_non_numeric_length_raises(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle("green", "five", 6)
        self.assertEqual(str(cm.exception), "Length must be numeric.")

    def test_non_numeric_width_raises(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle("green", 5, "six")
        self.assertEqual(str(cm.exception), "Width must be numeric.")

if __name__ == '__main__':
    unittest.main()