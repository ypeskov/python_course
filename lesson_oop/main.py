from datetime import date
import pudb

from vehicle import AbstractVehicle
from vehicle.engine import Engine
from vehicle.water.sailboat import SailBoat
from vehicle.water.motorboat import MotorBoat
from vehicle.ground.train import Train
from vehicle.noownerexception import NoOwnerException


def demo(vehicle: AbstractVehicle, char: str = '-',):
    heading_width = 80

    print()
    print(f' [{vehicle.__class__.__name__}] Demo '.center(heading_width, char))
    print(vehicle)
    print()

    vehicle.start()
    vehicle.make_sound()
    vehicle.stop()

    print(f'{char * heading_width}\n')


if __name__ == '__main__':
    date_built = date(1991, 12, 31)
    sail_boat = SailBoat(10000, date_built, 5000, 150)
    demo(sail_boat)
    pudb.set_trace()
    engine = Engine(power=500, volume=5, fuel_consumption=20)
    motor_boat = MotorBoat(weight=1000, date_built=date_built, displacement=550, engine=engine) # noqa
    engine.set_carrier(motor_boat)
    try:
        demo(motor_boat)
    except NoOwnerException as ex:
        print(ex)

    engine = Engine(power=5000, volume=30, fuel_consumption=200)
    try:
        train = Train(weight=100_000, date_built=date(2001, 1, 15), max_speed=120, engine=engine) # noqa
        engine.set_carrier(train)
        try:
            demo(train)
        except NoOwnerException as ex:
            print(ex)
    except ValueError as ex:
        print(ex)
