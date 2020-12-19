from datetime import date
from abc import ABC, abstractmethod
from typing import Union

from vehicle import AbstractVehicle


class AbstractGroundVehicle(AbstractVehicle, ABC):
    def __init__(self, weight: float, date_built: date, max_speed: Union[float, None] = None):
        super().__init__(weight, date_built)

        if float is None:
            raise ValueError('max speed cannot be None')
        self.max_speed = max_speed  # km/h

    def stop(self):
        self.sleep()
        self.turn_off_all()

    @abstractmethod
    def turn_off_all(self):
        pass

    def __str__(self):
        output = super().__str__()
        output += f'\nGround characteristics. Max speed: {self.max_speed} km/h'
        return output
