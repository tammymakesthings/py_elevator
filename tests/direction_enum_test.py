#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `pyelevator` package."""
import pytest
from click.testing import CliRunner

from pyelevator.cli import simulation
from pyelevator.direction import Direction
from pyelevator.elevator import Elevator


class TestDirectionsEnum:
    def test_has_proper_values(self):
        assert Direction.UP
        assert Direction.DOWN
        assert Direction.STOPPED

    def test_can_convert_to_string(self):
        assert Direction.as_string(Direction.UP) == "going up"
        assert Direction.as_string(Direction.DOWN) == "going down"
        assert Direction.as_string(Direction.STOPPED) == "stopped"
