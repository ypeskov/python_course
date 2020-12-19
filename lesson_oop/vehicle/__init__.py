from abc import ABC, abstractmethod
from datetime import date


class AbstractVehicle(ABC):
    def __init__(self, weight: float, date_built: date):
        self.weight = weight

        if not isinstance(date_built, date):
            raise ValueError('date_built must be of type datetime.date')
        self.date_built = date_built

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        print(f'{self.__class__.__name__} is moving forward')

    @abstractmethod
    def stop(self):
        pass

    def __str__(self):
        return f'General characteristics. Built date: {self.date_built}, weight: {self.weight} kg'
