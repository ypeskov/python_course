from datetime import date

from vehicle import AbstractVehicle
from vehicle.engine import Engine
from vehicle.water.sailboat import SailBoat
from vehicle.water.motorboat import MotorBoat
from vehicle.noownerexception import NoOwnerException


def demo(char: str, vehicle: AbstractVehicle):
    print()
    print(f'{char * 10} [{vehicle.__class__.__name__}] Demo {char * 10}')
    print(vehicle)
    print()

    vehicle.prepare()
    vehicle.move()
    vehicle.make_sound()
    vehicle.stop()

    print(f'{char * 25}\n')


if __name__ == '__main__':
    date_built = date(1991, 12, 31)
    heading_char = '-'

    sail_boat = SailBoat(10000, date_built, 5000, 150)
    demo(heading_char, sail_boat)

    engine = Engine(power=500, volume=5, fuel_consumption=20)
    motor_boat = MotorBoat(weight=1000, date_built=date_built, displacement=300, engine=engine)
    # engine.set_owner(motor_boat)
    try:
        demo(heading_char, motor_boat)
    except NoOwnerException as ex:
        print(ex)
