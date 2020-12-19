from dataclasses import dataclass
from typing import Optional

from vehicle import AbstractVehicle
from vehicle.noownerexception import NoOwnerException


@dataclass
class Engine:
    power: int  # horse powers
    volume: float  # litres
    fuel_consumption: float  # litres/hour
    owner: Optional[AbstractVehicle] = None  # carrier of this engine

    def set_owner(self, owner: AbstractVehicle):
        self.owner = owner

    def _check_owner(self):
        if not isinstance(self.owner, AbstractVehicle):
            raise NoOwnerException(f'{self.__class__.__name__} must have a carrier')

    def start(self):
        self._check_owner()
        print(f'{self.owner.__class__.__name__} starts engine')

    def stop(self):
        self._check_owner()
        print(f'{self.owner.__class__.__name__} stops engine')

    def __str__(self):
        return f'power: {self.power} hp, engine volume: {self.volume} l, fuel consumption: {self.fuel_consumption} l/h'
