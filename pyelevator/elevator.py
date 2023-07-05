# -*- coding: utf-8 -*-
"""
Elevator Exercise in Python
Tammy Cravit - tammy@tammymakesthings.com - 2023-06-28
"""
import logging

logging.basicConfig(level=logging.DEBUG)

from enum import IntEnum, auto
from random import randint
from time import sleep

from .direction import Direction


class Elevator:
    """
    A simulation of an elevator in Python.
    """

    _current_floor: int
    _current_direction: Direction
    _number_of_floors: int

    _up_buttons: list[bool]
    _down_buttons: list[bool]
    _car_buttons: list[bool]
    _idle_count: int = 0

    def __init__(
        self,
        number_of_floors: int,
        *,
        current_floor: int = 1,
        direction: Direction = Direction.STOPPED,
    ):
        """
        Create a new Elevator instance.

        Args:
            number_of_floors (int) - The number of floors for the Elevator.
            current_floor (int, keyword only) - The floor the Elevator should start
                on. Defaults to 1 if not specified.
            direction (Direction, keyword only) - The initial direction for the Elevator.
                Defaults to Direction.STOPPED if not specified.

        Returns:
            The newly created Elevator instance.

        Raises:
            ValueError - Raised if the number of floors is less than 2, or greater than 100,
            if the current floor is out of range, or if the initial direction is invalid.
        """
        if number_of_floors < 2 or number_of_floors > 100:
            raise ValueError("invalid number of floors", number_of_floors)
        if direction not in [Direction.UP, Direction.DOWN, Direction.STOPPED]:
            raise ValueError("invalid direction", direction)
        if not 1 <= current_floor <= number_of_floors:
            raise ValueError("invalid initial floor", current_floor)

        self._current_direction = direction
        self._current_floor = current_floor
        self._number_of_floors = number_of_floors

        self._up_buttons = [False for _ in range(number_of_floors + 1)]
        self._down_buttons = [False for _ in range(number_of_floors + 1)]
        self._car_buttons = [False for _ in range(number_of_floors + 1)]

        self._idle_count = 0

    @property
    def idle_counter(self) -> int:
        """
        Get the current value of the idle counter.

        Returns:
            int - the current value of the idle counter.
        """
        return self._idle_count

    @idle_counter.setter
    def idle_counter(self, new_value: int) -> None:
        """
        Set the current value of the idle counter.

        Args:
            new_value (int) - the new value of the idle counter.
        """
        self._idle_count = new_value

    @property
    def number_of_floors(self) -> int:
        """
        Get the number of floors the Elevator can service.

        Returns:
            int - the number of floors the Elevator can service.
        """
        return self._number_of_floors

    @property
    def floor(self) -> int:
        """
        Get the current floor number for the Elevator.

        Returns:
            int - the current floor for the Elevator.
        """
        return self._current_floor

    @property
    def direction(self) -> Direction:
        """
        Get the current Elevator direction.

        Returns:
            Direction - the current direction of the Elevator.
        """
        return self._current_direction

    @direction.setter
    def direction(self, new_direction: Direction) -> None:
        """
        Set the current Elevator direction.

        If the direction is unchanged from its previous value, captures an idle
        state for the simulation. Otherwise also clears the idle counter.

        Args:
            new_direction (Direction) - The new direction for the Elevator.
        """
        if new_direction != self.direction:
            logging.info("elevator direction is now %s", str(new_direction))
            self._current_direction = new_direction
            self.idle_counter = 0

    @floor.setter
    def floor(self, new_floor: int) -> None:
        """
        Move the Elevator to a new floor.

        If the floor number is unchanged from its previous value, captures
        an idle state for the simulation. Otherwise also clears the idle
        counter.

        Args:
            new_floor (int) - The new floor for the Elevator to move to.

        Raises:
            ValueError - raised if the new floor number is out of bounds.
        """
        if not (1 <= new_floor <= self.number_of_floors):
            raise ValueError("new floor number is out of bounds", new_floor)

        old_floor = self.floor
        if old_floor != new_floor:
            logging.info("moving from floor %d to floor %d", old_floor, new_floor)
            self._current_floor = new_floor
            self.idle_counter = 0

    @property
    def up_buttons(self) -> list[bool]:
        """
        Gets the list of up buttons (on the floors) for the Elevator.

        Returns:
            list[bool] - The list of the up buttons for the Elevator.
        """
        return self._up_buttons

    @property
    def down_buttons(self) -> list[bool]:
        """
        Gets the list of down buttons (on the floors) for the Elevator.

        Returns:
            list[bool] - The list of the down buttons for the Elevator.
        """
        return self._down_buttons

    @property
    def car_buttons(self) -> list[bool]:
        """
        Gets the list of the floor buttons (in the Elevator car).

        Returns:
            list[bool] - The list of the floor buttons in the Elevator car.
        """
        return self._car_buttons

    def press_up(self, *floors) -> None:
        """
        Press one or more up buttons on the different floors.

        Args:
            floors (list[int]) - The list of floors to press.
        """
        for floor_num in floors:
            logging.info("pressing the UP button for floor %d", floor_num)
            self.up_buttons[floor_num] = True

    def press_down(self, *floors) -> None:
        """
        Press one or more down buttons on the different floors.

        Args:
            floors (list[int]) - the list of floors to press.
        """
        for floor_num in floors:
            logging.info("pressing the DOWN button for floor %d", floor_num)
            self.down_buttons[floor_num] = True

    def press_car(self, *floors) -> None:
        """
        Press one or more floor buttons in the Elevator car.

        Args:
            floors (list[int]) - the list of floors to press.
        """
        for floor_num in floors:
            logging.info("pressing the CAR button for floor %d", floor_num)
            self.car_buttons[floor_num] = True

    def clear_up(self, *floors) -> None:
        """
        Clear one or more up buttons on the different floors.

        Args:
            floors (list[int]) - the list of floors to clear.
        """
        for floor_num in floors:
            logging.info("clearing the UP button for floor %d", floor_num)
            self.up_buttons[floor_num] = False

    def clear_down(self, *floors) -> None:
        """
        Clear one or more down buttons on the different floors.

        Args:
            floors (list[int]) - the list of floors to clear.
        """
        for floor_num in floors:
            logging.info("clearing the DOWN button for floor %d", floor_num)
            self.down_buttons[floor_num] = False

    def clear_car(self, *floors) -> None:
        """
        Clear one or more floor buttons in the Elevator car.

        Args:
            floors (list[int]) - the list of floors to clear.
        """
        for floor_num in floors:
            logging.info("clearing the CAR button for floor %d", floor_num)
            self.car_buttons[floor_num] = False

    def clear_all(self, *floors) -> None:
        """
        Clear all buttons for a list of floors.

        Args:
            floors (list[int]) - the list of floors to clear.
        """
        self.clear_up(floors)
        self.clear_down(floors)
        self.clear_car(floors)

    def stop_needed_on_floor(self, floor_num: int) -> bool:
        """
        Determine whether the Elevator needs to stop on a particular floor.

        If the in-car button for the specified floor is pressed, we will stop there
        regardless of elevtor direction. If the Elevator is stopped and either floor
        button for the specified floor is pressed, we need to stop there. Otherwise,
        we need to stop there if the floor button matching the current direction of
        travel is pressed.

        Args:
            floor_num (int) - the floor number to check.

        Returns:
            bool - True if a stop is needed on the specified floor, False otherwise.

        Raises:
            ValueError - raised if the floor number specified is invalid.
        """
        if not (1 <= floor_num <= self.number_of_floors):
            raise ValueError("invalid floor number", floor_num)

        match self.direction:
            case Direction.STOPPED:
                return any(
                    [
                        self.up_buttons[floor_num],
                        self.down_buttons[floor_num],
                        self.car_buttons[floor_num],
                    ],
                )
            case Direction.UP:
                return any([self.up_buttons[floor_num], self.car_buttons[floor_num]])
            case Direction.DOWN:
                return any([self.down_buttons[floor_num], self.car_buttons[floor_num]])
            case _:
                return False

    def stops_needed_above_current_floor(self) -> list[int]:
        """
        Check the Elevator buttons and get a list of stops needed above the current floor.

        Returns:
            list[int] - THe list of floors on which a stop is needed above the current floor.
                If no stops are needed, an empty list is returned.
        """
        if self.on_top_floor():
            return []

        needed_stops = [
            floor
            for floor in range(self.floor, self.number_of_floors + 1)
            if self.stop_needed_on_floor(floor)
        ]
        return list(set(needed_stops))

    def stops_needed_below_current_floor(self) -> list[int]:
        """
        Check the Elevator buttons and get a list of stops needed below the current floor.

        Returns:
            list[int] - The list of floors on which a stop is needed below the current floor.
                If no stops are needed, an empty list is returned.
        """
        if self.on_first_floor():
            return []

        needed_stops = [
            floor
            for floor in range(1, self.number_of_floors)
            if self.stop_needed_on_floor(floor)
        ]
        return list(set(needed_stops))

    def reverse_direction_if_needed(self) -> None:
        """
        Reverse the direction of the Elevator if needed.
        """
        if self.direction == Direction.UP and (
            self.on_top_floor() or len(self.stops_needed_above_current_floor()) == 0
        ):
            logging.info("Reversing direction UP => DOWN")
            if len(self.stops_needed_below_current_floor()):
                logging.info(
                    "Stops are needed below the current floor - setting direction to DOWN",
                )
                self.direction = Direction.DOWN
            else:
                logging.info(
                    "No stops needed below the current floor - setting direction to STOPPED",
                )
                self.direction = Direction.STOPPED
        elif self.direction == Direction.DOWN and (
            self.on_first_floor() or len(self.stops_needed_below_current_floor()) == 0
        ):
            logging.info("Reversing direction DOWN => UP")
            if len(self.stops_needed_above_current_floor()):
                logging.info(
                    "Stops are needed above the current floor - setting direction to UP",
                )
                self.direction = Direction.UP
            else:
                logging, info(
                    "No stops needed below the current floor - setting direction to STOPPED",
                )
                self.direction = Direction.STOPPED

    def on_top_floor(self) -> bool:
        """
        Check if the Elevator is currently on the top floor.

        Returns:
            bool - True if the Elevator is on the top floor, False otherwise.
        """
        return self.floor == self.number_of_floors

    def on_first_floor(self) -> bool:
        """
        Check if the Elevator is currently on the first floor.

        Returns:
            bool - True if the Elevator is on the first floor, False otherwise.
        """
        return self.floor == 1

    def stop_on_floor(
        self,
        floor_num: int,
        moving_direction: Direction,
        *,
        max_wait_time_on_floor: int = 5,
        enable_sleep: bool = True,
    ) -> None:
        """
        Stop on the specified floor.

        If the value of ``moving_direction``  direction is ``UP``, also clears the up button and in-car button
        for the specified floor. If the value of ``moving_direction`` is ``DOWN``, also clears the up button
        and in-car button for the specified floor.

        Args:
            floor_num (int) - The floor number we're stopping on.
            moving_direction (Direction) - Which direction the Elevator is moving. This is used to clear the
                correct buttons.
            max_wait_time_on_floor (int, keyword only) - The maximum number of seconds the simulation should
                wait for passenger movement once the doors are open.
            enable_sleep (bool, keyword only) - whether to enable calls to :py:func:`time.sleep` in the
                simulation run.
        """
        logging.info("*** STOPPING on floor: %d", self.floor)
        self.clear_car(floor_num)
        match moving_direction:
            case Direction.UP:
                self.clear_up(floor_num)
            case Direction.DOWN:
                self.clear_down(floor_num)

        logging.info("    Doors are opening...")
        if enable_sleep:
            sleep(1)

        passenger_movement_time = randint(1, max_wait_time_on_floor)
        logging.info(
            "    Waiting %d seconds for for passenger movement",
            passenger_movement_time,
        )
        if enable_sleep:
            sleep(passenger_movement_time)

        logging.info("    Doors are closing...")
        if enable_sleep:
            sleep(1)

        logging.info("current Elevator state: %s", str(self))

    def move_up_one_floor(self) -> None:
        """
        Move up one floor if needed.
        """
        if not self.on_top_floor() and self.stops_needed_above_current_floor():
            self.floor = self.floor + 1
            if self.stop_needed_on_floor(self.floor):
                self.stop_on_floor(self.floor, Direction.UP)

    def move_down_one_floor(self) -> None:
        """
        Move down one floor if needed.
        """
        if not self.on_first_floor() and self.stops_needed_below_current_floor():
            self.floor = self.floor - 1
            if self.stop_needed_on_floor(self.floor):
                self.stop_on_floor(self.floor, Direction.DOWN)

    def increment_idle_counter(self) -> None:
        """
        Increment the idle counter used to end the simulation when the Elevator hasn't moved for
        :py:const:`IDLE_COUNTER_MAX_ITERATIONS` iterations.
        """
        self.idle_counter += 1
        logging.info("Elevator idling; idle count is now %d", self._idle_count)

    def simulation_move_one_step(self) -> None:
        """
        Run one iteration of the simulation.
        """
        match self.direction:
            case Direction.UP:
                if len(self.stops_needed_above_current_floor()):
                    self.move_up_one_floor()
                self.reverse_direction_if_needed()

            case Direction.DOWN:
                if len(self.stops_needed_below_current_floor()):
                    self.move_down_one_floor()
                self.reverse_direction_if_needed()

            case Direction.STOPPED:
                if self.simulation_can_move():
                    if (
                        len(self.stops_needed_above_current_floor())
                        and not self.on_top_floor()
                    ):
                        self.direction = Direction.UP
                        self.move_up_one_floor()
                elif (
                    len(self.stops_needed_below_current_floor())
                    and not self.on_first_floor()
                ):
                    self.direction = Direction.DOWN
                    self.move_down_one_floor()

    def simulation_can_move(self) -> bool:
        """
        Determine if the simulation can move at all.
        """
        return any(self.up_buttons) or any(self.down_buttons) or any(self.car_buttons)

    def go(self, max_idle_iterations: int) -> None:
        """
        The entrypoint for the simulation.

                Args:
                        max_idle_iterations (int) - The maximum number of successive idle iterations
                                before the simulation will stop.
        """
        self.idle_counter = 0
        logging.info("initial Elevator state is as follows: \n%s", str(self))

        while self.idle_counter <= max_idle_iterations:
            if self.simulation_can_move():
                self.idle_counter = 0
                self.simulation_move_one_step()
            else:
                self.increment_idle_counter()

        logging.info("Maximum idle count reached - simulation done.")

    def __str__(self) -> str:
        result: list[str] = list()
        result.append(
            f"An Elevator on floor {self.floor} of {self.number_of_floors}, Direction = {str(self.direction)}",
        )
        result.append(f"Idle counter = {self.idle_counter}")
        result.append(
            f"stops_needed_above_current_floor() = {self.stops_needed_above_current_floor!r}",
        )
        result.append(
            f"stops_needed_below_current_floor() = {self.stops_needed_above_current_floor!r}",
        )
        result.append("")
        result.append(
            "Floor #     Car Here     Up Button    Car Button     Down Button",
        )
        result.append(
            "-------     --------     ---------    ----------     -----------",
        )
        for floor in range(self.number_of_floors, 0, -1):
            car_here = "[HERE]" if self.floor == floor else ""
            up_pressed = "[PRESSED]" if self.up_buttons[floor] else ""
            car_pressed = "[PRESSED]" if self.car_buttons[floor] else ""
            down_pressed = "[PRESSED]" if self.down_buttons[floor] else ""
            result.append(
                f"{floor:^7}     {car_here:^8}     {up_pressed:^9}     {car_pressed:^10}     {down_pressed:^11}",
            )
        return "\n".join(result)

    def __repr__(self) -> str:
        return f"Elevator(number_of_floors={self.number_of_floors}, current_floor={self.floor}, direction={self.direction})"
