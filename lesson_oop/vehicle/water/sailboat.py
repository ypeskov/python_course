from datetime import date

from vehicle.water import AbstractWaterVehicle
from numbers import Real


class SailBoat(AbstractWaterVehicle):
    def __init__(self, weight: Real, date_built: date, displacement: Real, sails_area: Real):
        super().__init__(weight, date_built, displacement)

        if not isinstance(sails_area, Real):
            raise ValueError(f'sails_area must be Real number for {self.__class__.__name__}')
        self.sails_area = sails_area

    def prepare_start(self):
        print(f'{self.__class__.__name__} is raising sails up')

    def prepare_stop(self):
        print(f'{self.__class__.__name__} is taking sails down')

    def make_sound(self):
        print(f'{self.__class__.__name__} goes in silence')

    def __str__(self):
        output = super().__str__()
        output += f'\n{self.__class__.__name__} characteristics. Sails area: {self.sails_area} m2'
        return output
