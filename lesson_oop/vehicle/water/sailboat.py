from vehicle.water import AbstractWaterVehicle
from datetime import date


class SailBoat(AbstractWaterVehicle):
    def __init__(self, weight: float, date_built: date, displacement: float, sails_area: float):
        super().__init__(weight, date_built, displacement)
        self.sails_area = sails_area

    def prepare(self):
        print(f'{self.__class__.__name__} is raising sails up')

    def sleep(self):
        print(f'{self.__class__.__name__} is taking sails down')

    def make_sound(self):
        print(f'{self.__class__.__name__} goes in silence')

    def __str__(self):
        output = super().__str__()
        output += f'\n{self.__class__.__name__} characteristics. Sails area: {self.sails_area} m2'
        return output
