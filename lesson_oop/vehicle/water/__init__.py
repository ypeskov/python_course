from datetime import date
from abc import ABC
from numbers import Number
from typing import Union

from vehicle import AbstractVehicle


class AbstractWaterVehicle(AbstractVehicle, ABC):
    def __init__(self,
                 weight: Union[int, float],
                 date_built: date,
                 displacement: Union[int, float]):
        super().__init__(weight, date_built)

        if not isinstance(displacement, Number):
            raise ValueError('displacement must be float')
        self.displacement = displacement

    def stop(self):
        self.prepare_stop()
        self.drop_anchor()

    def drop_anchor(self):
        print(f'{self.__class__.__name__} drops an anchor')

    def __str__(self):
        output = super().__str__()
        output += f'\nMarine characteristics. Displacement: {self.displacement} kg'
        return output
