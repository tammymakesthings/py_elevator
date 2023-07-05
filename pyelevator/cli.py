# -*- coding: utf-8 -*-
"""Console script for pyelevator."""
import functools
import logging
import sys
from typing import List
from typing import Optional

import click

from .direction import Direction
from .elevator import Elevator

# +: A type alias for the selected button lists.
SelectedButtonList = Optional[List[int]]

# +: Default number of floors for the simulation.
DEFAULT_FLOORS: int = 12

# +: Default number of idle iterations before the simulation ends.
DEFAULT_IDLE_ITERATIONS: int = 10


@click.command()
@click.option(
    "--num-floors",
    "-n",
    default=DEFAULT_FLOORS,
    help="Number of floors for the Elevator to service",
)
@click.option(
    "--max-idle-iterations",
    "-i",
    default=DEFAULT_IDLE_ITERATIONS,
    help="Maximum idle cycles before the simulation stops",
)
@click.option("--verbose", default=False, help="enable verbose logging")
@click.option(
    "--up-on",
    "-u",
    multiple=True,
    help="Press the UP buttons on floors",
    default=[],
)
@click.option(
    "--down-on",
    "-d",
    multiple=True,
    help="Press the DOWN buttons on floors",
    default=[],
)
@click.option(
    "--car-on",
    "-c",
    multiple=True,
    help="Press the CAR buttons on floors",
    default=[],
)
def simulation(
    num_floors,
    max_idle_iterations,
    verbose,
    up_on,
    down_on,
    car_on,
):
    """
    Command Line Driver for the Elevator Simulation.
    """

    if len(up_on) == 0 and len(down_on) == 0 and len(car_on) == 0:
        click.echo("the simulation won't run because no buttons were pressed.")
        click.exit(1)

    if verbose:
        logging.basicConfig(level=logging.DEBUG, encoding="utf-8")
    else:
        logging.basicConfig(level=logging.INFO, encoding="utf-8")

    click.echo(f"Creating Elevator simulation with {floors} floors...")
    elevator = Elevator(number_of_floors=num_floors)

    up_buttons = list()
    down_buttons = list()
    car_buttons = list()

    for floor_num in up_on:
        try:
            if 1 <= int(floor_num) <= num_floors:
                click.echo(f"    Pressing UP button on floor number {floor_num}...")
                elevator.press_up(int(floor_num))
            else:
                click.echo(f"    Ignoring invalid floor number {floor_num}")
        except TypeError:
            click.echo(f"    Ignoring invalid floor number '{repr(floor_num)}'")

    for floor_num in down_on:
        try:
            if 1 <= int(floor_num) <= num_floors:
                click.echo(f"    Pressing DOWN button on floor number {floor_num}...")
                elevator.press_down(int(floor_num))
            else:
                click.echo(f"    Ignoring invalid floor number {floor_num}")
        except TypeError:
            click.echo(f"    Ignoring invalid floor number '{repr(floor_num)}'")

    for floor_num in car_on:
        try:
            if 1 <= int(floor_num) <= num_floors:
                click.echo(f"    Pressing CAR button on floor number {floor_num}...")
                elevator.press_car(int(floor_num))
            else:
                click.echo(f"    Ignoring invalid floor number {floor_num}")
        except TypeError:
            click.echo(f"    Ignoring invalid floor number '{repr(floor_num)}'")

    click.echo(
        f"Running Elevator simulation with max_idle_iterations={max_idle_iterations}...",
    )
    elevator.go(max_idle_iterations)
