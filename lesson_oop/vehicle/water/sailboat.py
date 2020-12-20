from datetime import date
from typing import Union
from numbers import Number

from vehicle.water import AbstractWaterVehicle


class SailBoat(AbstractWaterVehicle):
    def __init__(self,
                 weight: Union[int, float],
                 date_built: date,
                 displacement: Union[int, float],
                 sails_area: Union[int, float]):
        super().__init__(weight, date_built, displacement)

        if not isinstance(sails_area, Number):
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
