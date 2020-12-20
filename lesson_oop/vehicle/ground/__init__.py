from datetime import date
from abc import ABC, abstractmethod
from typing import Union
from numbers import Real

from vehicle import AbstractVehicle


class AbstractGroundVehicle(AbstractVehicle, ABC):
    def __init__(self, weight: Real, date_built: date, max_speed: Union[Real, None] = None):
        super().__init__(weight, date_built)

        if max_speed is None or not isinstance(max_speed, Real):
            raise ValueError('max speed cannot be None')
        self.max_speed = max_speed  # km/h

    def stop(self):
        self.prepare_stop()
        self.final_actions()

    @abstractmethod
    def final_actions(self):
        pass

    def __str__(self):
        output = super().__str__()
        output += f'\nGround characteristics. Max speed: {self.max_speed} km/h'
        return output
