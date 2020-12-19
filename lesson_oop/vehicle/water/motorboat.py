from datetime import date
from numbers import Real

from vehicle.water import AbstractWaterVehicle
from vehicle.engine import Engine
from vehicle.enginemixin import EngineMixin


class MotorBoat(EngineMixin, AbstractWaterVehicle):
    def __init__(self, weight: Real, date_built: date, displacement: Real, engine: Engine):
        super().__init__(weight, date_built, displacement)
        self.engine = engine

    def make_sound(self):
        print(f'{self.__class__.__name__} sounds like "Drrrr  Drrrrrrrr"')
