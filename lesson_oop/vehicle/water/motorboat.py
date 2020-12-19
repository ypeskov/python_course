from datetime import date

from vehicle.water import AbstractWaterVehicle
from vehicle.engine import Engine


class MotorBoat(AbstractWaterVehicle):
    def __init__(self, weight: float, date_built: date, displacement: float, engine: Engine):
        super().__init__(weight, date_built, displacement)
        self.engine = engine

    def prepare(self):
        self.engine.start()

    def make_sound(self):
        print(f'{self.__class__.__name__} sounds like "Drrrr  Drrrrrrrr"')

    def sleep(self):
        self.engine.stop()

    def __str__(self):
        output = super().__str__()
        output += f'\n{self.__class__.__name__} characteristics. Engine [{self.engine}]'
        return output
