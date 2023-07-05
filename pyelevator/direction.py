# -*- coding: utf-8 -*-
"""
Elevator Exercise in Python
Tammy Cravit - tammy@tammymakesthings.com - 2023-06-28
"""
from enum import auto
from enum import IntEnum


class Direction(IntEnum):
    """
    Defines the current direction of movement of the Elevator.
    """

    STOPPED = auto()
    UP = auto()
    DOWN = auto()

    @classmethod
    def as_string(cls, d) -> str:
        """
        A helper to convert a Direction enum to a more human friendly form.

        Args:
            d (Direction) - a Direction enum value.

        Returns:
            string - a human-friendly string representation of the Direction.
        """
        match d:
            case Direction.STOPPED:
                return "stopped"
            case Direction.UP:
                return "going up"
            case Direction.DOWN:
                return "going down"
        return "unkown state"
