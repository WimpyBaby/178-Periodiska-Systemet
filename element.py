"""A module for storing data value from elements."""

from dataclasses import dataclass


@dataclass
class Element:
    """A class representing an element."""

    symbol: str
    weight: float
    number: int
    row: int
    column: int
