from datetime import date
from typing import Union

from vehicle.ground import AbstractGroundVehicle
from vehicle.engine import Engine
from vehicle.enginemixin import EngineMixin


class Train(EngineMixin, AbstractGroundVehicle):
    def __init__(self,
                 weight: Union[int, float],
                 date_built: date,
                 max_speed: Union[int, float],
                 engine: Engine):
        super().__init__(weight, date_built, max_speed)

        if not isinstance(engine, Engine):
            raise ValueError('engine must be type of Engine')
        self.engine = engine

    def make_sound(self):
        print(f'{self.__class__.__name__} makes "chuh-chuh-chuh"')

    def final_actions(self):
        print(f'{self.__class__.__name__} is closing all doors')


