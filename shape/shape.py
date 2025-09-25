"""This module defines the Shape class."""

__author__ = "Jaskarandeep Kaur"
__version__ = "25.09.25"

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class for shapes.

    Attributes:
        _color (str): protected color of the shape.
    """

    def __init__(self, color: str):
        """
        Initialize the Shape.

        Args:
            color (str): color of the shape (cannot be blank).

        Raises:
            ValueError: if color is blank or only whitespace.
        """
        
        color = color.strip() if isinstance(color, str) else ''
        if not color:
            raise ValueError("Color cannot be blank.")
        self._color = color

    def __str__(self) -> str:
        """
        Return a description that includes the shape's color.
        Format: "The shape color is {color}."
        """
        return f"The shape color is {self._color}."


    def calculate_area(self):
        """Return the area of the shape (implemented in subclasses)."""
        pass

  
    def calculate_perimeter(self):
        """Return the perimeter of the shape (implemented in subclasses)."""
        pass
