from datetime import date

from abc import ABC
from vehicle import AbstractVehicle


class AbstractWaterVehicle(AbstractVehicle, ABC):
    def __init__(self, weight: float, date_built: date, displacement: float):
        super().__init__(weight, date_built)

        if not isinstance(displacement, float):
            raise ValueError('displacement must be float')
        self.displacement = displacement

    def stop(self):
        self.sleep()
        self.drop_anchor()

    def drop_anchor(self):
        print(f'{self.__class__.__name__} drops an anchor')

    def __str__(self):
        output = super().__str__()
        output += f'\nMarine characteristics. Displacement: {self.displacement} kg'
        return output
