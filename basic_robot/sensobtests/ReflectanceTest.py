from basic_robot.sensobs.Reflectance_sensors import ReflectanceSensors
from basic_robot.actuation.Motob import Motob
from basic_robot.sensobs.Zumo_button import ZumoButton
from time import sleep

sens = ReflectanceSensors()
m = Motob()


def adjustLine(err):
    if err[0] < 0.1 or err[1] < 0.1:
        m.turn_left(5)

    elif err[4] < 0.1 or err[5] < 0.1:
        m.turn_right(5)


if __name__ == '__main__':
    while True:
        ZumoButton().wait_for_press()
        m.forward()
        while True:
            arr = sens.update()
            adjustLine(arr)
            m.forward()
            sleep(0.1)
