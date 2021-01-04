from abc import ABC, abstractmethod
from datetime import date
from numbers import Number
from typing import Union


class AbstractVehicle(ABC):
    def __init__(self, weight: Union[int, float], date_built: date):
        if not isinstance(weight, Number):
            raise ValueError(f'weight of {self.__class__.__name__} must be a real number') # noqa
        self.weight = weight  # kg

        if not isinstance(date_built, date):
            raise ValueError('date_built must be of type datetime.date')
        self.date_built = date_built

    def start(self):
        self.prepare_start()
        self.move()

    @abstractmethod
    def prepare_start(self):
        pass

    @abstractmethod
    def prepare_stop(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        print(f'{self.__class__.__name__} starts moving forward')

    @abstractmethod
    def stop(self):
        pass

    def __str__(self):
        return f'General characteristics. Built date: {self.date_built}, weight: {self.weight} kg' # noqa
