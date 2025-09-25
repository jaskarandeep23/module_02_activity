"""This module defines the Triangle class."""

__author__ = "Jaskarandeep kaur"
__version__ = "25.09.25"

from .shape import Shape
import math

class Triangle(Shape):
    """
    Triangle with three integer side lengths (cm).
    """

    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):
        """
        Initialize Triangle.

        Raises ValueError with exact messages required by the spec on validation failure.
        """
        super().__init__(color)

        if not isinstance(side_1, int):
            raise ValueError("Side 1 must be numeric.")
        if not isinstance(side_2, int):
            raise ValueError("Side 2 must be numeric.")
        if not isinstance(side_3, int):
            raise ValueError("Side 3 must be numeric.")

        a, b, c = side_1, side_2, side_3
        
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")

        self._side_1 = a
        self._side_2 = b
        self._side_3 = c

    def __str__(self) -> str:
        base = super().__str__()
        return (f"{base}\n"
                f"This triangle has three sides with the lengths of "
                f"{self._side_1}, {self._side_2} and {self._side_3} centimeters.")

    def calculate_area(self) -> float:
        a = self._side_1
        b = self._side_2
        c = self._side_3
        s = (a + b + c) / 2.0
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

    def calculate_perimeter(self) -> int:
        return self._side_1 + self._side_2 + self._side_3
    
    
import unittest
import math
from shape import Triangle

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.t = Triangle("red", 5, 6, 7)

    def test_str(self):
        expected = "The shape color is red.\nThis triangle has three sides with the lengths of 5, 6 and 7 centimeters."
        self.assertEqual(str(self.t), expected)

    def test_area(self):
        expected_area = math.sqrt(9 * (9 - 5) * (9 - 6) * (9 - 7))  # for 5,6,7 -> s=9
        self.assertAlmostEqual(self.t.calculate_area(), expected_area, places=6)

    def test_perimeter(self):
        self.assertEqual(self.t.calculate_perimeter(), 18)

    def test_non_numeric_side1_raises(self):
        with self.assertRaises(ValueError) as cm:
            Triangle("blue", "a", 2, 3)
        self.assertEqual(str(cm.exception), "Side 1 must be numeric.")

    def test_triangle_inequality_raises(self):
        with self.assertRaises(ValueError) as cm:
            Triangle("green", 1, 2, 3)
        self.assertEqual(str(cm.exception), "The sides do not satisfy the Triangle Inequality Theorem.")

if __name__ == '__main__':
    unittest.main()