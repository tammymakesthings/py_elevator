#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `pyelevator` package."""
import pytest
from click.testing import CliRunner

from pyelevator.cli import simulation
from pyelevator.direction import Direction
from pyelevator.elevator import Elevator


class TestElevatorCLI:
    @pytest.fixture()
    def runner(self):
        return CliRunner()

    def test_simulation_aborts_if_no_buttons_pressed(self, runner):
        result = runner.invoke(simulation)
        assert result.exit_code == 1
        assert "no buttons were pressed" in result.output

    def test_help_message_contains_all_options(self, runner):
        help_result = runner.invoke(simulation, ["--help"])
        assert help_result.exit_code == 0
        for cmd_opt in [
            "max-idle-iterations",
            "num-floors",
            "up-on",
            "down-on",
            "car-on",
            "verbose",
        ]:
            assert f"--{cmd_opt}" in help_result.output
