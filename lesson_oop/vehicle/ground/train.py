from datetime import date

from vehicle.ground import AbstractGroundVehicle
from vehicle.engine import Engine


class Train(AbstractGroundVehicle):
    def __init__(self, weight: float, date_built: date, max_speed: float, engine: Engine):
        super().__init__(weight, date_built, max_speed)

        if not isinstance(engine, Engine):
            raise ValueError('engine must be type of Engine')
        self.engine = engine

    def prepare(self):
        self.engine.start()

    def sleep(self):
        self.engine.stop()

    def make_sound(self):
        print(f'{self.__class__.__name__} makes "chuh-chuh-chuh"')

    def turn_off_all(self):
        print(f'{self.__class__.__name__} closes all doors')

    def __str__(self):
        output = super().__str__()
        output += f'\n{self.__class__.__name__} characteristics. Engine [{self.engine}]'
        return output
